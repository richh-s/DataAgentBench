code = """import re, json
# var_call_SpSHlWc9Wvw6XBIPzo9P5Jzs is the storage key for the previous query result file path
p = var_call_SpSHlWc9Wvw6XBIPzo9P5Jzs
# load the JSON file
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
texts = [rec.get('Patents_info','') for rec in data]
pattern = re.compile(r"(?:pub(?:lication)?\. ?number|pub\. number|publication number)\s*([A-Z]{2}-?\d+[A-Z0-9\-]*)", re.IGNORECASE)
ids = []
for t in texts:
    for m in pattern.finditer(t):
        ids.append(m.group(1))
# also look for patterns like 'publication number US-11421276-B2' variations already covered
ids = list(dict.fromkeys(ids))
# fallback: also try to find application numbers like 'application (number US-202117472182-A)'
pattern2 = re.compile(r"application \(number\s+([A-Z]{2}-?\d+[A-Z0-9\-]*)\)", re.IGNORECASE)
for t in texts:
    for m in pattern2.finditer(t):
        if m.group(1) not in ids:
            ids.append(m.group(1))
# also look for 'app. number' or 'app. number TW-107142982-A'
pattern3 = re.compile(r"app\. number\s+([A-Z]{2}-?\d+[A-Z0-9\-]*)", re.IGNORECASE)
for t in texts:
    for m in pattern3.finditer(t):
        if m.group(1) not in ids:
            ids.append(m.group(1))
# Output list
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_ut7WdDsWTHeaPTY0l7N78YWW': ['publicationinfo'], 'var_call_42eJZpAO2w2mYOtquWKcommi': ['cpc_definition'], 'var_call_SpSHlWc9Wvw6XBIPzo9P5Jzs': 'file_storage/call_SpSHlWc9Wvw6XBIPzo9P5Jzs.json'}

exec(code, env_args)
