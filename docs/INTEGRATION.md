# Integration architecture

Use adapters at explicit protocol boundaries. Keep canonical internal contracts separate from transport encodings and vendor-specific APIs.

## Initial protocol map
- MCP: tool, resource, and prompt integration.
- A2A: agent-to-agent task and delegation workflows.
- OpenAPI: HTTP service contracts.
- JSON Schema 2020-12: payload validation.
- OpenTelemetry: traces, metrics, and logs.

These are integration targets, not claims of completed implementations.

## Adapter requirements
- Validate inbound and outbound payloads.
- Preserve identity, authorization context, correlation IDs, and provenance.
- Apply timeouts, bounded retries, backpressure, and idempotency keys where appropriate.
- Map errors explicitly; never convert denial or failure into success.
- Document lossy transformations and protocol-version constraints.
