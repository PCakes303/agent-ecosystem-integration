import unittest
from tools.validate_profile import validate
V={"profile_version":"1.0","id":"example.bridge","source":{"protocol":"MCP","version":"1"},"target":{"protocol":"internal","version":"1"},"security":{"validate_input":True,"authorize_each_call":True,"forward_credentials":False},"reliability":{"timeout_required":True,"retries":"bounded"}}
class Tests(unittest.TestCase):
 def test_valid(self): self.assertEqual(validate(V),[])
 def test_timeout(self): self.assertTrue(validate({**V,"reliability":{"timeout_required":False,"retries":"bounded"}}))
 def test_forwarding(self): self.assertTrue(validate({**V,"security":{**V["security"],"forward_credentials":True}}))
 def test_retries(self): self.assertTrue(validate({**V,"reliability":{"timeout_required":True,"retries":"unbounded"}}))
 def test_endpoint(self): self.assertTrue(validate({**V,"source":{"protocol":"MCP"}}))
if __name__=="__main__": unittest.main()
