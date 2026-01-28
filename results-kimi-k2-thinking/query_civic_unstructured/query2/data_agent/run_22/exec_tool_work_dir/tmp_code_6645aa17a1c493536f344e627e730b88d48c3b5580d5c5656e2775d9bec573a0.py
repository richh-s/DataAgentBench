code = """import json
import re

civic_docs = json.load(open('var_functions.query_db_36'))
funding_data = json.load(open('var_functions.query_db_8'))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Park' in text and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 'Park' in line and len(line) < 120:
                bad = ['updates', 'schedule', 'description', 'page', 'agenda', 'item']
                if not any(w in line.lower() for w in bad):
                    if line not in park_projects:
                        park_projects.append(line)

# Calculate total funding
total = 0
for project in park_projects:
    proj_lower = project.lower()
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        if proj_lower == fund_name:
            total += int(fund['Amount'])

result = {'total_funding': total, 'projects': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
