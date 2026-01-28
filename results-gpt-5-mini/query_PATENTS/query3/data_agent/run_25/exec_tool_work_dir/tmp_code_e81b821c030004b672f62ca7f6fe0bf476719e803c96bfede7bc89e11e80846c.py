code = """import json, re
# var_call_6s5RpImgm3iTcGaGq8ohXGZr is available in storage
path = var_call_6s5RpImgm3iTcGaGq8ohXGZr
with open(path, 'r') as f:
    data = json.load(f)
pubs = set()
pattern = re.compile(r"\b[A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+\b")
# Also match patterns like US-11421276-B2, TW-201925402-A
for rec in data:
    pis = rec.get('Patents_info','')
    # find all matches
    for m in pattern.findall(pis):
        pubs.add(m)
# Also look for patterns like US-4599677-A in citation fields inside this UC set (if any)
# But we just want UC publication numbers
pubs_list = sorted(pubs)
import json
print("__RESULT__:")
print(json.dumps(pubs_list))"""

env_args = {'var_call_6s5RpImgm3iTcGaGq8ohXGZr': 'file_storage/call_6s5RpImgm3iTcGaGq8ohXGZr.json'}

exec(code, env_args)
