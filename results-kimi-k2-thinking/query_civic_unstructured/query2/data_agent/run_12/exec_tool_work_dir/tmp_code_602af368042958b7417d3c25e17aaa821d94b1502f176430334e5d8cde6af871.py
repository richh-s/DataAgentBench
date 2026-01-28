code = """import json
import re

# Load data
civic_path = var_functions.query_db_118
funding_path = var_functions.query_db_107

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_records = json.load(f)

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    low_text = text.lower()
    
    # Check for park and 2022 completion
    if 'park' in low_text and '2022' in text and 'completed' in low_text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            # Look for park project lines
            if 'park' in line.lower() and len(line) < 150 and not line.startswith('('):
                # Check context for 2022 completion
                context = ' '.join(lines[max(0,i-5):i+5])
                if '2022' in context and 'completed' in context.lower():
                    if line not in park_projects:
                        park_projects.append(line)

print('Park projects found:', len(park_projects))
for p in park_projects:
    print(' -', p)

# Simple matching by checking if park name appears in funding name or vice versa
matched_funding = []
for fund in funding_records:
    fund_name = fund.get('Project_Name','')
    if not fund_name:
        continue
    
    fund_lower = fund_name.lower()
    for park in park_projects:
        park_lower = park.lower()
        # Check for matches
        if (park_lower in fund_lower) or (fund_lower in park_lower):
            # Check if we already counted this funding
            fund_id = fund.get('Funding_ID')
            if not any(m.get('Funding_ID') == fund_id for m in matched_funding):
                matched_funding.append(fund)

# Calculate total
total = sum(int(f.get('Amount', 0)) for f in matched_funding)
print('Total funding:', total)

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.list_db:104': ['civic_docs'], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:118': 'file_storage/functions.query_db:118.json'}

exec(code, env_args)
