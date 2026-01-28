code = """import json, re
civic_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

# Extract all project names from documents
all_projects = []
search_terms = ['spring 2022', '2022-spring']
for doc in civic_docs:
    text = doc['text'].lower()
    if any(term in text for term in search_terms):
        lines = doc['text'].split('\n')
        for line in lines:
            line_clean = line.strip()
            if len(line_clean) > 10 and line_clean[0].isupper() and not line_clean.startswith('Page') and not line_clean.startswith('Item'):
                all_projects.append(line_clean)

# Count unique projects
unique = list(dict.fromkeys(all_projects))

# Match with funding data
total = 0
for fund in funding:
    fund_lower = fund['Project_Name'].lower()
    for proj in unique:
        proj_lower = proj.lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            total += int(fund['Amount'])
            break

print('__RESULT__:')
print(json.dumps({'count': len(unique), 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}}

exec(code, env_args)
