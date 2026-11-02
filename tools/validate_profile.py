import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "integration-profile.schema.json"
MAX_BYTES = 1_048_576
MAX_DEPTH = 32


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result: raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _depth(raw):
    level = 0
    in_string = escaped = False
    for char in raw:
        if in_string:
            if escaped: escaped = False
            elif char == "\\": escaped = True
            elif char == '"': in_string = False
        elif char == '"': in_string = True
        elif char in "[{":
            level += 1
            if level > MAX_DEPTH: raise ValueError("JSON nesting exceeds depth limit")
        elif char in "]}":
            level -= 1
            if level < 0: raise ValueError("invalid JSON structure")


def load_profile(path):
    raw_bytes = Path(path).read_bytes()
    if len(raw_bytes) > MAX_BYTES: raise ValueError("profile exceeds byte limit")
    raw = raw_bytes.decode("utf-8")
    _depth(raw)
    return json.loads(raw, object_pairs_hook=_pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"invalid JSON number: {value}")))


def validate(document):
    if not isinstance(document, dict): return ["profile must be an object"]
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema).iter_errors(document),
                        key=lambda error: (tuple(str(part) for part in error.absolute_path), error.message))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return [f"normative schema unavailable or invalid: {type(exc).__name__}"]
    return [f"schema violation at {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}" for error in errors]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "examples" / "integration-profile.json"
    try: document = load_profile(path)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError, RecursionError) as exc:
        print(exc, file=sys.stderr); return 2
    errors = validate(document)
    if errors:
        print("\n".join(errors), file=sys.stderr); return 1
    print("valid integration profile: " + document["id"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
