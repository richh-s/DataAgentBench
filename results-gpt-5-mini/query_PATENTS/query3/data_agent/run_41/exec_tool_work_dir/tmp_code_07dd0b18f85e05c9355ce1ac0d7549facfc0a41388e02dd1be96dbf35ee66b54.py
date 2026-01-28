code = """import json, re
# var_call_jLvjv05XYdBAh8YEcyK3bTTF is provided by previous query_db call
path = var_call_jLvjv05XYdBAh8YEcyK3bTTF
with open(path, 'r') as f:
    data = json.load(f)
pubs = set()
pattern = re.compile(r"[A-Z]{2}-\d[A-Z0-9\-]*")
for rec in data:
    pi = rec.get('Patents_info','') or ''
    matches = pattern.findall(pi)
    for m in matches:
        pubs.add(m)
# Also check for patterns like US\d{7,}
pattern2 = re.compile(r"US-?\d{7,}(?:-[A-Z0-9]+)?")
for rec in data:
    pi = rec.get('Patents_info','') or ''
    for m in pattern2.findall(pi):
        pubs.add(m if m.startswith('US-') else 'US-'+m)
result = sorted(list(pubs))
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jLvjv05XYdBAh8YEcyK3bTTF': 'file_storage/call_jLvjv05XYdBAh8YEcyK3bTTF.json'}

exec(code, env_args)
