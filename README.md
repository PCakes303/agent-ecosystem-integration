# Agent Ecosystem Integration

**MrCakes931 Agent Intelligence Ecosystem · Interoperability layer**

Defines adapters, integration profiles, and conformance expectations for connecting ecosystem repositories and external agent systems while preserving security and semantic meaning across protocol boundaries.

## Scope
- Explicit source and target protocols, versions, and data mappings.
- MCP, A2A, OpenAPI, JSON Schema, and OpenTelemetry integration profiles.
- Identity, authorization, provenance, correlation, and error propagation.
- Timeouts, bounded retries, backpressure, and idempotency requirements.

## Layout
- docs/INTEGRATION.md — integration architecture and protocol map.
- docs/ADAPTER-CONTRACT.md — adapter requirements.
- examples/integration-profile.json — illustrative integration profile.
- tools/validate_profile.py — schema-backed bounded profile validator.
- tests/ — automated validation tests.
- .github/workflows/validate.yml — CI validation.

## Validate locally
Requires Python 3.10+. Install the pinned development schema validator with `python -m pip install -r requirements-dev.txt`.

    python tools/validate_profile.py
    python -m unittest discover -s tests -v

## Adapter safety requirements
Adapters validate inbound and outbound payloads, authorize each call, preserve identity and provenance, apply timeouts and bounded retries, and map errors explicitly. They must not bypass authorization, forward credentials to untrusted destinations, silently discard security context, or claim exactly-once execution. Document every lossy transformation and protocol-version constraint.

MCP, A2A, OpenAPI, JSON Schema, and OpenTelemetry are integration targets—not claims that all adapters are implemented or certified.

## Status
Scaffolded, v0.1.0. Initial integration contracts, example, validator, tests, and CI are published. Production adapters and cross-repository conformance suites remain future work.

## Entry-level build

Start with the runnable starter build:

    python tools/starter_build.py
    python -m unittest discover -s tests -v

See [Entry-level build guide](docs/ENTRY-LEVEL-BUILD.md) for Starter → Developer → Production progression.

## Ecosystem
Master registry: https://github.com/PCakes303/agent-intelligence-ecosystem

Public project identity: **MrCakes931**  
GitHub owner: `PCakes303`

## Licensing

This repository documents the ecosystem's intended scoped mixed-license policy: Apache-2.0 for eligible original code and machine-readable contracts, and CC BY 4.0 for eligible original human-readable documentation. Its manifest remains `pending-review` until contributor authority, file-level provenance and third-party notices are checked. Do not assume every file is cleared for redistribution. Third-party material retains upstream terms; data, evidence, fixtures, sample payloads and media receive no blanket license. See [LICENSE.md](LICENSE.md).
