code = """import json, re
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

spring_proj_names = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10 and line[0].isupper() and not line.startswith('Page') and not line.startswith('Item'):
            # Check following lines for spring 2022 
            next_part = ' '.join(lines[i:i+6]).lower()
            if ('spring' in next_part and '2022' in next_part) or '2022-spring' in next_part:
                spring_proj_names.append(line)

unique_proj = []
for p in spring_proj_names:
    if p not in unique_proj:
        unique_proj.append(p)

total_funding = 0
matched = []
for fund in funding:
    fund_lower = fund['Project_Name'].lower()
    for proj in unique_proj:
        proj_lower = proj.lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            total_funding += int(fund['Amount'])
            matched.append({'proj': proj, 'fund': fund['Project_Name'], 'amt': int(fund['Amount'])})
            break

result = {'spring_2022_project_count': len(unique_proj), 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}}

exec(code, env_args)
