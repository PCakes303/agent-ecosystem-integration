# Adapter contract

An adapter MUST declare source and target protocols, supported versions, data mappings, security assumptions, timeout/retry behavior, and known lossy transformations.

An adapter MUST NOT bypass authorization, forward credentials to untrusted destinations, treat successful serialization as semantic validity, claim exactly-once execution, or silently discard provenance.

Every adapter should include positive, negative, malformed-input, timeout, and partial-failure tests.
