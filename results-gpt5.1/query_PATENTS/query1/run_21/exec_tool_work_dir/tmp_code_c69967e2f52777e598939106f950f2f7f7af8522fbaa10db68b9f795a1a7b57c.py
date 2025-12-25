code = """import json, pandas as pd

pub_path = var_call_rsLR4inHjlZynKAipYdpmjRT
cpcdef_path = var_call_aIEDwcrdwiNPeICQgcADbBR0

with open(cpcdef_path, 'r') as f:
    cpcdef_data = json.load(f)

# Inspect keys
first = cpcdef_data[0] if cpcdef_data else {}
import json as _json
out = _json.dumps(list(first.keys()))
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rsLR4inHjlZynKAipYdpmjRT': 'file_storage/call_rsLR4inHjlZynKAipYdpmjRT.json', 'var_call_aIEDwcrdwiNPeICQgcADbBR0': 'file_storage/call_aIEDwcrdwiNPeICQgcADbBR0.json'}

exec(code, env_args)
