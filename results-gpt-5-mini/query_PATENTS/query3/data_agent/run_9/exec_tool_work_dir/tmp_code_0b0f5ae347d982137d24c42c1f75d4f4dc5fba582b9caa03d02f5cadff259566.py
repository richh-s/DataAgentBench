code = """import json, re
# var_call_BfPoQrtpdZs8bOhuCak8YNnV is available in storage
path = var_call_BfPoQrtpdZs8bOhuCak8YNnV
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubnums = set()
pat = re.compile(r"[A-Z]{2}-[A-Z0-9]+(?:-[A-Z0-9]+)*")
for rec in data:
    pi = rec.get('Patents_info','')
    if pi:
        for m in pat.findall(pi):
            # filter out short tokens like 'US-'
            if '-' in m and len(m) > 5:
                pubnums.add(m)
pubnums = sorted(pubnums)
import json
print("__RESULT__:")
print(json.dumps(pubnums))"""

env_args = {'var_call_eg8rP1RmWgqRjk1wBHSbX67d': 'file_storage/call_eg8rP1RmWgqRjk1wBHSbX67d.json', 'var_call_BfPoQrtpdZs8bOhuCak8YNnV': 'file_storage/call_BfPoQrtpdZs8bOhuCak8YNnV.json'}

exec(code, env_args)
