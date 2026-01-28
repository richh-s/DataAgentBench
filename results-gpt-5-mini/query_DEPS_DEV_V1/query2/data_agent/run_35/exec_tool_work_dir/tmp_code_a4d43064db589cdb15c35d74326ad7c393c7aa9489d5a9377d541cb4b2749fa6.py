code = """import json
# var_call_yLsAhTA5bdHMTrzlstkcUKhF is the storage variable holding the file path to the full JSON result
path = var_call_yLsAhTA5bdHMTrzlstkcUKhF
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# Extract unique (Name, Version) pairs
pairs = []
seen = set()
for r in records:
    name = r.get('Name')
    version = r.get('Version')
    key = (name, version)
    if key not in seen:
        seen.add(key)
        pairs.append({'Name': name, 'Version': version})
# Output JSON-serializable string
print('__RESULT__:')
import json
print(json.dumps(pairs))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json'}

exec(code, env_args)
