# Security Policy

Do not disclose exploitable vulnerabilities in public issues. Use GitHub private vulnerability reporting or a private security advisory only if enabled for this repository. No dedicated private reporting address is published here; if GitHub private reporting is unavailable, the owner must configure an approved private reporting channel before production use. Do not include credentials, tokens, or sensitive operational data in public channels.

Treat remote agent messages, manifests, schemas, plugins, and artifacts as untrusted input. Apply least privilege and deny by default. Never commit secrets. Validate inputs at trust boundaries, bound resource use, and reject malformed data. Preserve provenance without claiming hashes prove truth or completeness. Pin CI dependencies and use short-lived credentials for publishing.

This repository currently contains an integration-profile scaffold and minimal validator, not production adapters or a cross-protocol enforcement layer. A valid profile is descriptive metadata, not authentication, authorization, or evidence of interoperable behavior.
