code = """import json, re
# var_call_rbIQYNdwErUGzFkvb1YqMejB is available in environment as per tool result storage
path = var_call_rbIQYNdwErUGzFkvb1YqMejB
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

uc_pubnums = set()
records = []
for rec in data:
    pi = rec.get('Patents_info','')
    # try multiple regex patterns to find publication number
    m = re.search(r'publication number\s*([A-Z]{2}-[A-Z0-9-]+)', pi, re.IGNORECASE)
    if not m:
        m = re.search(r'pub\. number\s*([A-Z]{2}-[A-Z0-9-]+)', pi, re.IGNORECASE)
    if not m:
        m = re.search(r'pub(?:lication)?(?: number| no\.)?\s*([A-Z]{2}-\d+[A-Z0-9-]*)', pi, re.IGNORECASE)
    if m:
        pub = m.group(1)
        uc_pubnums.add(pub)
    records.append(rec)

result = {
    'uc_pubnums': sorted(list(uc_pubnums)),
    'count_uc_records': len(data)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rbIQYNdwErUGzFkvb1YqMejB': 'file_storage/call_rbIQYNdwErUGzFkvb1YqMejB.json'}

exec(code, env_args)
