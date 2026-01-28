code = """import json, re
# var_call_FWaq87obpvltPwUmTRpRaycV is available in storage
path = var_call_FWaq87obpvltPwUmTRpRaycV
with open(path, 'r') as f:
    records = json.load(f)
pubnums = set()
for rec in records:
    pinfo = rec.get('Patents_info','')
    # find patterns like US-2022074631-A1, TW-201925402-A, US-11421276-B2 etc.
    matches = re.findall(r"[A-Z]{2}-[0-9A-Za-z\-]+", pinfo)
    for m in matches:
        pubnums.add(m)
# Also check if publication numbers might be in title_localized or other fields? We'll also look for publication_number in citation entries
    cit = rec.get('citation','')
    # citation field may be JSON-like string; find publication numbers there too
    matches2 = re.findall(r"[A-Z]{2}-[0-9A-Za-z\-]+", cit)
    for m in matches2:
        pubnums.add(m)

pubnums_list = sorted(pubnums)
import json
print("__RESULT__:")
print(json.dumps(pubnums_list))"""

env_args = {'var_call_FWaq87obpvltPwUmTRpRaycV': 'file_storage/call_FWaq87obpvltPwUmTRpRaycV.json'}

exec(code, env_args)
