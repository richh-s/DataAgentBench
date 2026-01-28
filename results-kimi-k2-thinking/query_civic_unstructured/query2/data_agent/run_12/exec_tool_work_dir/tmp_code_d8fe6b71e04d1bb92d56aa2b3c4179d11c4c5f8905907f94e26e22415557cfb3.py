code = """import json
import re

# Load data from file paths
civic_path = var_functions.query_db_118
funding_path = var_functions.query_db_107

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Civic docs count: ' + str(len(civic_docs)))
print('Funding records count: ' + str(len(funding_records)))

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    low_text = text.lower()
    
    # Only process documents mentioning parks and 2022 completion
    if 'park' in low_text and '2022' in text and 'completed' in low_text:
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                park_projects.append(line_clean)

print('Park projects with 2022 completion: ' + str(len(park_projects)))
for proj in park_projects:
    print(' - ' + proj)

# Simple matching - check if project names match
matched_funding = []
unmatched_funding = []

for fund in funding_records:
    fund_name = fund.get('Project_Name','')
    if not fund_name:
        continue
    
    name_lower = fund_name.lower()
    matched = False
    
    for park in park_projects:
        park_lower = park.lower()
        # Check if names are similar
        if park_lower in name_lower or name_lower in park_lower:
            matched_funding.append(fund)
            matched = True
            break
    
    if not matched:
        unmatched_funding.append(fund_name)

# Calculate total funding
total = 0
matched_names = []
for f in matched_funding:
    amt = int(f.get('Amount', 0))
    total = total + amt
    matched_names.append(f.get('Project_Name',''))

print('Matched funding records: ' + str(len(matched_funding)))
print('Total funding amount: ' + str(total))
print('Matched projects:')
for name in matched_names:
    print(' - ' + name)

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.list_db:104': ['civic_docs'], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:118': 'file_storage/functions.query_db:118.json'}

exec(code, env_args)
