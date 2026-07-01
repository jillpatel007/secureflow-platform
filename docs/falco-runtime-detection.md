# Falco Runtime Threat Detection

Falco runs as a DaemonSet in the `security-tools` namespace, using the modern_ebpf
driver to monitor kernel syscalls across all containers.

## Demonstrated detection
Simulated an intrusion by spawning a shell inside the running secureflow-api pod:
  kubectl exec -it deploy/secureflow-api -- /bin/sh

Falco detected it in real time:
  "A shell was spawned in a container with an attached terminal"
  - captured: container name, pod name, namespace, user uid, process, command

## Why it matters
Prevention (Kyverno/RBAC/NetworkPolicy) can be bypassed; Falco provides the
detection layer — real-time alerts on suspicious runtime behavior (shells,
sensitive file access, unexpected processes) at the kernel level via eBPF.
