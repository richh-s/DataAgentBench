code = """import json
import re

civic_docs_input = locals().get('var_functions.query_db:5', [])
funding_data_input = locals().get('var_functions.query_db:8', [])

# Load data if they are file paths
if isinstance(civic_docs_input, str) and civic_docs_input.endswith('.json'):
    with open(civic_docs_input, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_input

if isinstance(funding_data_input, str) and funding_data_input.endswith('.json'):
    with open(funding_data_input, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_data_input

# Extract projects that started in Spring 2022
projects_spring_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for projects with 2022 date references
    if '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if line and len(line) > 5:
                # Check following lines for Spring indicators
                next_text = ' '.join(lines[i+1:min(i+20, len(lines))])
                spring_match = any(indicator in next_text for indicator in [
                    'Spring 2022', '2022-Spring', '2022-March', '2022-April', '2022-May',
                    'March 2022', 'April 2022', 'May 2022', '2022-03', '2022-04', '2022-05'
                ])
                if spring_match:
                    projects_spring_2022.append(line)

# Remove duplicates
unique_projects = list(set(projects_spring_2022))

# Create funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Match projects with funding
matched_projects = []
total_funding = 0

for proj_name in unique_projects:
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        matched_projects.append({'Project_Name': proj_name, 'Amount': amount})
        total_funding += amount
        continue
    
    # Look for partial matches
    for fund_name, amount in funding_lookup.items():
        if (proj_name.lower() in fund_name.lower() or 
            fund_name.lower() in proj_name.lower()):
            matched_projects.append({'Project_Name': fund_name, 'Amount': amount})
            total_funding += amount
            break

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}}

exec(code, env_args)
