import json
import tempfile
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator
from tools.validate_profile import load_profile, validate, SCHEMA_PATH

V={"profile_version":"1.0","id":"example.bridge","source":{"protocol":"MCP","version":"1"},"target":{"protocol":"internal","version":"1"},"status":"illustrative","security":{"validate_input":True,"authorize_each_call":True,"forward_credentials":False},"reliability":{"timeout_required":True,"retries":"bounded","idempotency":"required-for-non-idempotent-effects"}}
SCHEMA=json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
CHECK=Draft202012Validator(SCHEMA)

class Tests(unittest.TestCase):
 def test_valid_and_schema_agreement(self):
  self.assertEqual(validate(V),[])
  self.assertEqual(list(CHECK.iter_errors(V)),[])
 def assert_rejected(self,doc):
  self.assertTrue(validate(doc))
  self.assertTrue(list(CHECK.iter_errors(doc)))
 def test_security_requirements_fail_closed(self):
  for key,value in (("validate_input",False),("authorize_each_call",False),("forward_credentials",True)):
   doc=json.loads(json.dumps(V));doc["security"][key]=value;self.assert_rejected(doc)
 def test_reliability_requirements(self):
  doc=json.loads(json.dumps(V));doc["reliability"]["timeout_required"]=False;self.assert_rejected(doc)
  doc=json.loads(json.dumps(V));doc["reliability"]["retries"]="unbounded";self.assert_rejected(doc)
 def test_unknown_fields_rejected_at_all_levels(self):
  for mutate in (lambda d:d.update(extra=True),lambda d:d["source"].update(extra=True),lambda d:d["target"].update(extra=True),lambda d:d["security"].update(extra=True),lambda d:d["reliability"].update(extra=True)):
   doc=json.loads(json.dumps(V));mutate(doc);self.assert_rejected(doc)
 def test_types_and_lengths(self):
  for mutate in (lambda d:d.update(id="x"*129),lambda d:d["source"].update(protocol="p"*129),lambda d:d["target"].update(version="v"*65),lambda d:d["reliability"].update(idempotency="i"*129),lambda d:d["source"].update(protocol=7)):
   doc=json.loads(json.dumps(V));mutate(doc);self.assert_rejected(doc)
 def test_missing_required_fields(self):
  doc=dict(V);del doc["source"];self.assert_rejected(doc)
 def test_duplicate_json_keys_nonfinite_depth_and_size(self):
  with tempfile.TemporaryDirectory() as tmp:
   path=Path(tmp)/"profile.json"
   for raw in ('{"id":"a","id":"b"}','{"x":NaN}','{"x":'+("["*33)+"0"+("]"*33)+"}"):
    path.write_text(raw,encoding="utf-8")
    with self.assertRaises(ValueError):load_profile(path)
   path.write_bytes(b" "*(1_048_577))
   with self.assertRaisesRegex(ValueError,"byte limit"):load_profile(path)

if __name__=="__main__":unittest.main()
