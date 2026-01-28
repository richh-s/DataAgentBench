code = """import json, re
# var_call_mN0bvvlQgMe2C2VNhr5mLXV6 is a path to the JSON file with the earlier query results
path = var_call_mN0bvvlQgMe2C2VNhr5mLXV6
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pubnums = set()
pattern = re.compile(r'([A-Z]{2}-[0-9]{4,}[A-Z0-9\-]*)')
for rec in data:
    pi = rec.get('Patents_info','')
    for m in pattern.findall(pi):
        pubnums.add(m)
# Also check citation fields in these UC records for their own publication_number values (sometimes stored there)
pattern2 = re.compile(r'"publication_number"\s*:\s*"([A-Z]{2}-[0-9A-Z\-]+)"')
for rec in data:
    cit = rec.get('citation','')
    for m in pattern2.findall(cit):
        pubnums.add(m)
publist = sorted(pubnums)
print("__RESULT__:")
print(json.dumps(publist))"""

env_args = {'var_call_JkzVcUe9mStTDG8g0enUZ82T': 'file_storage/call_JkzVcUe9mStTDG8g0enUZ82T.json', 'var_call_mN0bvvlQgMe2C2VNhr5mLXV6': 'file_storage/call_mN0bvvlQgMe2C2VNhr5mLXV6.json'}

exec(code, env_args)
