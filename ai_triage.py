#!/usr/bin/env python3
"""AI-powered security triage: rule-based scoring + local LLM (Ollama/llama3.2) reasoning."""
import json, sys, urllib.request

SEVERITY_BASE = {"CRITICAL": 10, "HIGH": 7, "MEDIUM": 4, "LOW": 1, "UNKNOWN": 0}
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"

def load_findings(path):
    data = json.load(open(path))
    out = []
    for result in data.get("Results", []):
        for v in result.get("Vulnerabilities", []) or []:
            out.append(v)
    return out

def score_finding(v):
    base = SEVERITY_BASE.get(v.get("Severity", "UNKNOWN"), 0)
    fixable = v.get("FixedVersion") is not None
    return base + 3 if fixable else base - 2

def ask_llm(prompt):
    """Call local Ollama LLM and return its text response."""
    payload = json.dumps({"model": MODEL, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read())["response"].strip()

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "trivy-results.json"
    findings = sorted(load_findings(path), key=score_finding, reverse=True)
    top = findings[:5]  # only top 5 -> keeps the LLM fast and focused

    # Build a compact summary of the top findings for the LLM
    summary = "\n".join(
        f"- {v.get('VulnerabilityID')} | {v.get('Severity')} | pkg={v.get('PkgName')} "
        f"| {'FIXABLE (patch available)' if v.get('FixedVersion') else 'no fix available'} "
        f"| {v.get('Title','')[:80]}"
        for v in top
    )

    prompt = f"""You are a security analyst. Below are the top-priority vulnerabilities
from a container image scan, already ranked by severity and fixability.

{summary}

For these findings, write a brief triage report:
1. Which to fix FIRST and why (prioritize ones with available fixes).
2. For each, one sentence on the real-world risk.
3. A short overall recommendation.
Keep it concise and practical."""

    print("\n=== AI SECURITY TRIAGE (local llama3.2) ===\n")
    print("Top findings (rule-scored):")
    for v in top:
        tag = "FIXABLE" if v.get("FixedVersion") else "no fix"
        print(f"  [{score_finding(v):3}] {v.get('Severity','?'):8} {v.get('VulnerabilityID')} ({tag})")
    print("\n--- Asking llama3.2 for analysis (may take ~30-60s)... ---\n")
    print(ask_llm(prompt))

if __name__ == "__main__":
    main()
