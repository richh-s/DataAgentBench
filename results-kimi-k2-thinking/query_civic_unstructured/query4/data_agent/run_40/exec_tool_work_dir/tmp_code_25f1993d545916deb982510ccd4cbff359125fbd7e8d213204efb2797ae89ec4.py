code = """import json
import re
import os

# Load the data files
with open('/root/shared_data/var_functions.query_db:50.json', 'r') as f:
    funding_data = json.load(f)

with open('/root/shared_data/var_functions.query_db:72.json', 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_data), 'funding records and', len(civic_docs), 'civic documents')

# Extract projects that started in Spring 2022
spring_2022_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Check for Spring 2022 indicators
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Look backwards up to 5 lines for the project name
                start_idx = max(0, i-5)
                for j in range(i-1, start_idx-1, -1):
                    candidate = lines[j].strip()
                    if candidate and len(candidate) > 15 and not candidate.startswith('(') and 'Page' not in candidate:
                        spring_2022_project_names.append(candidate)
                        break
                break

print('Found', len(spring_2022_project_names), 'Spring 2022 project candidates')

# Match with funding records
total_funding = 0
matched_project_set = set()

for fund in funding_data:
    fund_name = fund['Project_Name']
    amount = int(fund['Amount'])
    
    for proj_name in spring_2022_project_names:
        # Check if the names match or contain each other
        if fund_name in proj_name or proj_name in fund_name:
            if fund_name not in matched_project_set:
                matched_project_set.add(fund_name)
                total_funding += amount
                break

# Format final answer
project_count = len(matched_project_set)
result = {"project_count": project_count, "total_funding": total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
