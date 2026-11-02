import json,sys
from pathlib import Path
def validate(d):
 e=[]
 if not isinstance(d,dict): return ["profile must be an object"]
 for k in ("profile_version","id","source","target","security","reliability"):
  if k not in d: e.append("missing "+k)
 for k in ("source","target"):
  x=d.get(k)
  if not isinstance(x,dict) or not isinstance(x.get("protocol"),str) or not x["protocol"].strip() or not isinstance(x.get("version"),str) or not x["version"].strip(): e.append(k+" must declare protocol and version")
 s=d.get("security")
 if not isinstance(s,dict): e.append("security must be an object")
 else:
  if s.get("validate_input") is not True: e.append("validate_input must be true")
  if s.get("authorize_each_call") is not True: e.append("authorize_each_call must be true")
  if s.get("forward_credentials") is True: e.append("credential forwarding is prohibited")
 r=d.get("reliability")
 if not isinstance(r,dict): e.append("reliability must be an object")
 else:
  if r.get("timeout_required") is not True: e.append("timeout_required must be true")
  if r.get("retries")!="bounded": e.append("retries must be bounded")
 return e
if __name__=="__main__":
 p=Path(sys.argv[1]) if len(sys.argv)>1 else Path("examples/integration-profile.json")
 try: d=json.loads(p.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as x: print(x,file=sys.stderr); sys.exit(2)
 e=validate(d)
 if e: print("\n".join(e),file=sys.stderr); sys.exit(1)
 print("valid integration profile: "+d["id"])
