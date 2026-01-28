code = """import json, re
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

project_names = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10 and line[0].isupper() and not line.startswith('Page') and not line.startswith('Item'):
            next_text = '  '.join(lines[i:i+5])
            if next_text.find('2022') >= 0 and next_text.lower().find('spring') >= 0:
                project_names.append(line)

# Deduplicate
unique_names = []
for p in project_names:
    if p not in unique_names:
        unique_names.append(p)

# Match funding
total_funding = 0
for fund in funding:
    fund_lower = fund['Project_Name'].lower()
    for proj in unique_names:
        proj_lower = proj.lower()
        if proj_lower.find(fund_lower) >= 0 or fund_lower.find(proj_lower) >= 0:
            total_funding += int(fund['Amount'])
            break

result = {'spring_2022_projects': len(unique_names), 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}}

exec(code, env_args)
