code = """import json
import re

# Load the data
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:6']

# Handle file paths
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert amounts
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for idx, line in enumerate(lines):
        line_lower = line.lower()
        if '2022' in line and 'completed' in line_lower:
            for j in range(max(0, idx-6), idx):
                prev = lines[j].strip()
                if not prev or len(prev) > 100:
                    continue
                
                park_keywords = ['park', 'playground', 'walkway', 'green street', 'bluffs', 'shade']
                if any(k in prev.lower() for k in park_keywords):
                    clean_name = re.sub(r'\(cid:\d+\)', '', prev).strip()
                    park_projects.append(clean_name)
                    break

# Match with funding
matches = []
for park_name in park_projects:
    park_lower = park_name.lower()
    for fund in funding_data:
        fund_lower = fund['Project_Name'].lower()
        if park_lower in fund_lower or fund_lower in park_lower:
            matches.append({
                'name': park_name,
                'funding_name': fund['Project_Name'],
                'amount': fund['Amount']
            })
            break

total = sum(m['amount'] for m in matches)
result = {'total_funding': total, 'matches': matches}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
