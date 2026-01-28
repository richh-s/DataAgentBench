code = """import json
import re

f_fund = var_functions.query_db:2
f_civic = var_functions.query_db:5

with open(f_fund) as f:
    funding = json.load(f)

with open(f_civic) as f:
    civic = json.load(f)

funding_names = [rec['Project_Name'] for rec in funding if int(rec['Amount']) > 50000]

projects = []
for doc in civic:
    if 'text' in doc and 'Capital Improvement Projects' in doc['text'] and 'Design' in doc['text']:
        for line in doc['text'].splitlines():
            line = line.strip()
            if 8 < len(line) < 60 and not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line:
                if any(k in line.lower() for k in ['road', 'park', 'canyon', 'storm', 'bridge']):
                    projects.append(line)

unique_projects = list(set(projects))

matched = 0
for proj in unique_projects:
    proj_clean = re.sub(r'[^a-zA-Z0-9]', '', proj).lower()
    for fund in funding_names:
        fund_clean = re.sub(r'[^a-zA-Z0-9]', '', fund).lower()
        if proj_clean in fund_clean or fund_clean in proj_clean:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
