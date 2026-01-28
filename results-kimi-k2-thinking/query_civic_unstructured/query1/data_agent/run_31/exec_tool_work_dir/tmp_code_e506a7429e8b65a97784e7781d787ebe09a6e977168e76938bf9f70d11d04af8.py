code = """import json
funding_path = var_functions.query_db:68
civic_path = var_functions.query_db:5
with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic = json.load(f)
high_funding = [rec for rec in funding if int(rec['Amount']) > 50000]
design_projects = []
for doc in civic:
    if 'text' in doc and 'Capital' in doc['text'] and 'Design' in doc['text']:
        for line in doc['text'].split('\n'):
            line = line.strip()
            if line and len(line) > 8 and len(line) < 60:
                if 'road' in line.lower() or 'park' in line.lower() or 'canyon' in line.lower() or 'storm' in line.lower():
                    design_projects.append(line)
unique_design = list(set(design_projects))
matched = 0
for proj in unique_design:
    proj_clean = ''.join(c for c in proj.lower() if c.isalnum())
    for fund in high_funding:
        fund_clean = ''.join(c for c in fund['Project_Name'].lower() if c.isalnum())
        if proj_clean in fund_clean or fund_clean in proj_clean:
            matched += 1
            break
result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
