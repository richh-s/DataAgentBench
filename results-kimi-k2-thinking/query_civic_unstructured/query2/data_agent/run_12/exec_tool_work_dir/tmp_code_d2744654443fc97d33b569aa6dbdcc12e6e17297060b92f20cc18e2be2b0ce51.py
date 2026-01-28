code = """import json
import re

# Access data
funding_data = var_functions.query_db_5
civic_docs_data = var_functions.query_db_2

# Extract park projects with 2022 completion from civic documents
park_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    if 'park' in text.lower() and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                if line_clean not in park_projects:
                    park_projects.append(line_clean)

# Sum funding amounts for park projects
total_funding = 0
project_matches = []

for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    if not fund_name:
        continue
    
    fund_name_clean = fund_name.lower()
    for park in park_projects:
        park_clean = park.lower()
        if park_clean in fund_name_clean or fund_name_clean in park_clean:
            total_funding += fund_amount
            project_matches.append({'park': park, 'fund': fund_name, 'amount': fund_amount})
            break

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding, 'match_count': len(project_matches)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}}

exec(code, env_args)
