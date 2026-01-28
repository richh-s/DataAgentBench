code = """import json, pandas as pd, re
from datetime import datetime

path = var_call_QVVMdIHmtyFsuI5sqTG3yzN5
with open(path, 'r') as f:
    mongo_records = json.load(f)

papers = []
for rec in mongo_records:
    text = rec.get('text','')
    head = text[:2000]
    years = re.findall(r"(19[9][0-9]|20[0-2][0-9]|2030)", head)
    year = None
    for y in years:
        y_int = int(y)
        if 1990 <= y_int <= datetime.now().year:
            year = y_int
            break
    if not year or year <= 2016:
        continue
    if re.search(r"empirical", text, re.IGNORECASE):
        title = rec.get('filename','').replace('.txt','').strip()
        papers.append({'title': title, 'year': year})


path2 = var_call_5UTLYr6CjRTZ3IeIVAZpQMJA
with open(path2, 'r') as f:
    cites = json.load(f)


# build citation dict
cites_dict = {}
for c in cites:
    t = c.get('title','')
    if t.startswith('"') and t.endswith('"'):
        t = t[1:-1]
    cites_dict[t] = int(c.get('total_citations') or 0)

results = []
for p in papers:
    t = p['title']
    total = cites_dict.get(t)
    results.append({'title': t, 'total_citation_count': total})

out = json.dumps(results)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_QVVMdIHmtyFsuI5sqTG3yzN5': 'file_storage/call_QVVMdIHmtyFsuI5sqTG3yzN5.json', 'var_call_5UTLYr6CjRTZ3IeIVAZpQMJA': 'file_storage/call_5UTLYr6CjRTZ3IeIVAZpQMJA.json', 'var_call_SpvFYTStV8PPB31Dwjgufzxa': {'columns': ['title', 'total_citations']}}

exec(code, env_args)
