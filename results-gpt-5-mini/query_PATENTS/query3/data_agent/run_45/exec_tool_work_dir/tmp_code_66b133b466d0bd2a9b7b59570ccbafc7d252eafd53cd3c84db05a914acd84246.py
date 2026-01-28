code = """import json, re
with open(var_call_1HEfWTTyAxtdte7bpVXwNGAy, 'r') as f:
    records = json.load(f)
pubnums = []
pattern = re.compile(r"[A-Z]{2}-[0-9][0-9A-Za-z-]+")
for rec in records:
    pi = rec.get('Patents_info','')
    # try to find near keywords
    m = re.search(r"(?:pub(?:lication)?\.?? number|publication number|publication no\.?|pub\. number|has pub\. number|has publication number)\s*([A-Z]{2}-[0-9][0-9A-Za-z-]+)", pi, re.IGNORECASE)
    if m:
        pubnums.append(m.group(1))
        continue
    # fallback: any match
    m2 = pattern.search(pi)
    if m2:
        pubnums.append(m2.group(0))
# unique
pubnums = sorted(set(pubnums))
print("__RESULT__:")
print(json.dumps(pubnums))"""

env_args = {'var_call_X55MlaZFDaGy31kjzwvu18Qb': ['publicationinfo'], 'var_call_RrwZKYjAfJZtUGwMqt28W4mJ': ['cpc_definition'], 'var_call_1HEfWTTyAxtdte7bpVXwNGAy': 'file_storage/call_1HEfWTTyAxtdte7bpVXwNGAy.json', 'var_call_ZmqIMvdppX0BFeOSlj81vzwf': 'file_storage/call_ZmqIMvdppX0BFeOSlj81vzwf.json'}

exec(code, env_args)
