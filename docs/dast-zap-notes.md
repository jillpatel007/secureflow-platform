# DAST — OWASP ZAP Dynamic Scan

ZAP baseline scan run against the live app (via kubectl port-forward -> host.docker.internal:8080).

## Result
PASS: 61, WARN: 6, FAIL: 0

## Findings (all HTTP-layer, fixable via Flask security headers)
- X-Content-Type-Options header missing
- Content-Security-Policy (CSP) not set
- Server leaks version information
- Permissions-Policy header not set
- Cross-Origin-Resource-Policy missing
- Storable/cacheable content

## Why DAST matters
These are runtime HTTP-response issues that static scanners (Semgrep/Trivy) cannot
find — they only appear when the app is actually running and serving requests.
Remediation: add security headers in Flask (deferred; documented as known findings).

Full report: zap-report.html
