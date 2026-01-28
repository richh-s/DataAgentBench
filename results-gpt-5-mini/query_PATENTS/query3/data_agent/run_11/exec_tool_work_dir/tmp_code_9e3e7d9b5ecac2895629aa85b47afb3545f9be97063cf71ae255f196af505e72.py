code = """import json, re
# var_call_ReJ3NVyhOOs5Nt8RHKKt0m0w is available in environment as a variable (file path)
path = var_call_ReJ3NVyhOOs5Nt8RHKKt0m0w
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubs = set()
pat = re.compile(r"[A-Z]{2}-\d{4,}-[A-Z0-9]+")
for rec in data:
    info = rec.get('Patents_info','')
    for m in pat.findall(info):
        pubs.add(m)
# Also check if 'publication number' phrases with formats like 'US11421276-B2' without dash
pat2 = re.compile(r"[A-Z]{2}\-?\d{4,}[0-9A-Z\-]*[A-Z0-9]+")
for rec in data:
    info = rec.get('Patents_info','')
    for m in pat2.findall(info):
        pubs.add(m)
pubs_list = sorted(pubs)
import json
print("__RESULT__:")
print(json.dumps(pubs_list))"""

env_args = {'var_call_ReJ3NVyhOOs5Nt8RHKKt0m0w': 'file_storage/call_ReJ3NVyhOOs5Nt8RHKKt0m0w.json'}

exec(code, env_args)
