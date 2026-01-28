code = """import json, re
# var_call_o3PfwbtrF1Uq9E4KQ2atPaw9 is available in storage
path = var_call_o3PfwbtrF1Uq9E4KQ2atPaw9
with open(path, 'r') as f:
    data = json.load(f)
pubnums = set()
# regex patterns to catch publication numbers like US-2022074631-A1, TW-201925402-A, US-11421276-B2
patterns = [r'pub(?:lication)?\. number\s*([A-Z]{2}-[0-9A-Za-z-]+)',
            r'publication number\s*([A-Z]{2}-[0-9A-Za-z-]+)',
            r'has publication number\s*([A-Z]{2}-[0-9A-Za-z-]+)',
            r'with pub\. number\s*([A-Z]{2}-[0-9A-Za-z-]+)',
            r'has pub\. number\s*([A-Z]{2}-[0-9A-Za-z-]+)']
for rec in data:
    info = rec.get('Patents_info','')
    for pat in patterns:
        for m in re.findall(pat, info, flags=re.IGNORECASE):
            pubnums.add(m.strip().strip('.'))
# also try to find tokens like "pub. number" variations more generally
# fallback: find occurrences of two uppercase letters followed by dash and digits
for rec in data:
    info = rec.get('Patents_info','')
    for m in re.findall(r'\b[A-Z]{2}-\d{4,}[A-Za-z0-9-]*\b', info):
        pubnums.add(m)
pubnums = sorted(pubnums)
import json
print("__RESULT__:")
print(json.dumps(pubnums))"""

env_args = {'var_call_GHHlpoJLIGHealc6HCfay9RQ': ['publicationinfo'], 'var_call_3LJBg0Bx7wVqc6J2Bvzo7KKF': ['cpc_definition'], 'var_call_o3PfwbtrF1Uq9E4KQ2atPaw9': 'file_storage/call_o3PfwbtrF1Uq9E4KQ2atPaw9.json'}

exec(code, env_args)
