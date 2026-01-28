code = """import json
import re

civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

with open(civic_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding = json.load(f)

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'park' in text and '2022' in text and 'completed' in text:
        lines = doc.get('text', '').split('\n')
        for line in lines:
            if 'park' in line.lower() and len(line) > 10:
                park_projects.append(line.strip())

# Remove duplicates
park_projects = list(set(park_projects))

# Calculate total funding
total_funding = 0
for project in park_projects:
    proj_words = project.lower().split()
    for fund in funding:
        fund_name = fund['Project_Name'].lower()
        if 'park' in fund_name and any(w in fund_name for w in proj_words[:2]):
            total_funding += int(fund['Amount'])

result = {'total_funding': total_funding, 'project_count': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
