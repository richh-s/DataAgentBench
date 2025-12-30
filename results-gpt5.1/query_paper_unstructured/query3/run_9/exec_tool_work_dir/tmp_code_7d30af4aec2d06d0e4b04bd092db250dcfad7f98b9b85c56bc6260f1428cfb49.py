code = """import json

mongo_path = var_call_JrvCkgZlVyQIh8mF21biU9gs
with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)

# Just count how many empirical & after 2016 and list titles
import re
emps = []
for doc in mongo_records:
    text = doc.get('text','') or ''
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        years = re.findall(r'(20[1-9][0-9])', text)
        year = None
        if years:
            cand = sorted({int(y) for y in years})
            for y in cand:
                if y >= 2017:
                    year = y
                    break
        if year is None or year <= 2016:
            continue
        title = (doc.get('filename') or '').replace('.txt','')
        emps.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(emps))"""

env_args = {'var_call_JrvCkgZlVyQIh8mF21biU9gs': 'file_storage/call_JrvCkgZlVyQIh8mF21biU9gs.json', 'var_call_ju9InGP20lZd1uAjGF4LYxx9': 'file_storage/call_ju9InGP20lZd1uAjGF4LYxx9.json', 'var_call_zbtNXIbDTaDGuIw5urip4aHx': ['title', 'total_citations']}

exec(code, env_args)
