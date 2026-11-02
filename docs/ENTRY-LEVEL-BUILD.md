# Entry-level build

Requires Python 3.10+; no third-party packages are required.

```bash
python tools/starter_build.py
python -m unittest discover -s tests -v
```

The starter build validates the example integration profile, including source/target protocol declarations, input validation, per-call authorization, credential-forwarding prohibition, timeouts, and bounded retries.

**Next tiers**
- Developer: implement one adapter against a local mock endpoint and add contract tests.
- Production: add protocol conformance suites, workload identity, observability, rate limits, retry budgets, circuit breakers, and signed deployment artifacts.
