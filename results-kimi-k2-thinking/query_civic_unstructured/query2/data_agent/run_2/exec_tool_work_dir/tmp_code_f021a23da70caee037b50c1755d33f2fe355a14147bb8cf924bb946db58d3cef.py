code = """import json
import re

# Access data files
civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:2']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

print('Loaded', len(civic_docs), 'documents and', len(funding_data), 'funding records')

# Simple extraction of park projects completed in 2022
projects_2022 = []

for doc in civic_docs:
    txt = doc.get('text', '').lower()
    if 'park' in txt and 'completed' in txt and '2022' in txt:
        # Extract potential project names
        for line in doc.get('text', '').split('\n'):
            line = line.strip()
            if line and 'park' in line.lower() and len(line) < 80 and line[0].isupper():
                if 'completed' in txt or '2022' in txt:
                    projects_2022.append(line)

# Get unique projects
unique = list(set(projects_2022))
print('Park projects 2022:', unique[:5])

# Calculate funding
total = 0
seen = set()

for proj in unique:
    proj_name_lower = proj.lower()
    
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        fund_lower = fund_name.lower()
        
        if 'park' in fund_lower:
            # Check name match
            if proj_name_lower in fund_lower or fund_lower in proj_name_lower:
                if fund_name not in seen:
                    total += int(fund.get('Amount', 0))
                    seen.add(fund_name)

result_str = 'Total funding for park-related projects completed in 2022 is $' + str(total)
print(result_str)
print('__RESULT__:', total)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.list_db:17': ['Funding']}

exec(code, env_args)
