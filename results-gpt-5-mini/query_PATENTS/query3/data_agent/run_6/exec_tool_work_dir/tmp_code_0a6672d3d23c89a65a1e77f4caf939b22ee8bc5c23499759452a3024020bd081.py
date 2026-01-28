code = """import json, re

# var_call_PZXE235Z20VYWoM0xEB6t9GU is provided by previous query_db call
path = var_call_PZXE235Z20VYWoM0xEB6t9GU
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

pub_nums = set()
pattern = re.compile(r"[A-Z]{2,}-[0-9A-Za-z\-]+")
for rec in data:
    pi = rec.get('Patents_info', '')
    matches = pattern.findall(pi)
    for m in matches:
        # skip plain words like 'UNIV' or 'CALIFORNIA' - ensure contains a hyphen and digits
        if '-' in m and re.search(r"\d", m):
            pub_nums.add(m)

pub_list = sorted(pub_nums)
import json
print("__RESULT__:")
print(json.dumps(pub_list))"""

env_args = {'var_call_PZXE235Z20VYWoM0xEB6t9GU': 'file_storage/call_PZXE235Z20VYWoM0xEB6t9GU.json'}

exec(code, env_args)
