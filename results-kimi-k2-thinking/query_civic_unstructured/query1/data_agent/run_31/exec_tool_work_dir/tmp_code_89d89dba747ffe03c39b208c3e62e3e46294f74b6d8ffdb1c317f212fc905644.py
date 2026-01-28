code = """import json
funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:5
with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic = json.load(f)
funding_names = []
for rec in funding:
    if int(rec['Amount']) > 50000:
        funding_names.append(rec['Project_Name'])
projects = []
for doc in civic:
    if 'text' in doc:
        text = doc['text']
        if 'Capital Improvement Projects' in text and 'Design' in text:
            for line in text.split('\n'):
                line = line.strip()
                if 8 < len(line) < 60 and not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line:
                    lower = line.lower()
                    if 'road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower:
                        projects.append(line)
unique_projects = list(set(projects))
matched = 0
for proj in unique_projects:
    proj_clean = ''.join(c for c in proj.lower() if c.isalnum())
    for fund in funding_names:
        fund_clean = ''.join(c for c in fund.lower() if c.isalnum())
        if proj_clean in fund_clean or fund_clean in proj_clean:
            matched += 1
            break
result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
