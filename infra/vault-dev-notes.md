# Vault Secrets Management (dev mode)

Vault runs in the `security-tools` namespace (excluded from the disallow-root Kyverno policy).

## Demonstrated secret lifecycle
- Store:    vault kv put secret/secureflow db_password=... api_key=...
- Retrieve: vault kv get secret/secureflow
- Rotate:   re-put with new value; Vault increments version (v1 -> v2)

## Production note
App authenticates to Vault via Kubernetes service-account identity and pulls
secrets at runtime — never hardcoded, never in the image, never in git.
Rotating in Vault propagates without redeploy.

Dev mode auto-unseals; production Vault uses sealed/unseal-key-shard ceremony.
