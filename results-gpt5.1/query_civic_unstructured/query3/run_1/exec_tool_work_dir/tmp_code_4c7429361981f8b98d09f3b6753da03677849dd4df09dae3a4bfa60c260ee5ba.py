code = """import re, json
from pathlib import Path

path_docs = Path(var_call_rzxNukdDZfQ2KkjVUEVPATIs)
with open(path_docs, 'r') as f:
    docs = json.load(f)

project_keywords = re.compile(r'(emergency|FEMA)', re.I)
projects = set()
for doc in docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        if project_keywords.search(line):
            name = line.strip().strip('-').strip()
            if len(name) > 3:
                projects.add(name)

funding = var_call_LpcCzxjb4ZsKydfzWAcdcL4c

results = []
for row in funding:
    pname = row['Project_Name']
    if project_keywords.search(pname):
        amt = row['Amount']
        try:
            amt = int(amt)
        except Exception:
            pass
        results.append({'Project_Name': pname, 'Funding_Source': row['Funding_Source'], 'Amount': amt, 'Status': None})

seen = set()
unique = []
for r in results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'])
    if key not in seen:
        seen.add(key)
        unique.append(r)

out = json.dumps(unique)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_rzxNukdDZfQ2KkjVUEVPATIs': 'file_storage/call_rzxNukdDZfQ2KkjVUEVPATIs.json', 'var_call_LpcCzxjb4ZsKydfzWAcdcL4c': 'file_storage/call_LpcCzxjb4ZsKydfzWAcdcL4c.json', 'var_call_lIFvh1lBVDy6RnCtOYNPanDD': ['civic_docs'], 'var_call_g9FfNpykuJJYJWazsGvPMLOK': ['Funding']}

exec(code, env_args)
