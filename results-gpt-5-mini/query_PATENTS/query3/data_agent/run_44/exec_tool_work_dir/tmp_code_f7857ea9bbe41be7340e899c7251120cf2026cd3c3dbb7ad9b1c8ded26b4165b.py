code = """import json, re
# load data from storage variable
data_var = var_call_cc68Z6aX2MXH8DgcWXYV034B
# data_var may be a file path string or already a list
if isinstance(data_var, str):
    with open(data_var, 'r', encoding='utf-8') as f:
        records = json.load(f)
else:
    records = data_var

pubnums = set()
pat = re.compile(r"\b[A-Z]{2}-\d{4,}[A-Z0-9-]*\b")
for r in records:
    pi = r.get('Patents_info','') or ''
    matches = pat.findall(pi)
    for m in matches:
        pubnums.add(m)
# also try to extract from other fields if needed
# return sorted list
pub_list = sorted(pubnums)
import json
print("__RESULT__:")
print(json.dumps(pub_list))"""

env_args = {'var_call_cc68Z6aX2MXH8DgcWXYV034B': 'file_storage/call_cc68Z6aX2MXH8DgcWXYV034B.json'}

exec(code, env_args)
