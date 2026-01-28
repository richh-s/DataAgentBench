code = """import json
import re

# Load stored variables
civic_docs = locals()['var_functions.query_db:2']
funding_records = locals()['var_functions.query_db:6']

# Handle potential file paths
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)
if isinstance(funding_records, str):
    with open(funding_records, 'r') as f:
        funding_records = json.load(f)

# Convert funding amounts to integers
for rec in funding_records:
    rec['Amount'] = int(rec['Amount'])

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    lines = [l.strip() for l in lines if l.strip()]
    
    for i in range(len(lines)):
        line = lines[i]
        if '2022' in line and 'completed' in line.lower():
            for j in range(max(0, i-5), i):
                prev = lines[j]
                if len(prev) > 100:
                    continue
                
                # Check park keywords
                keywords = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs']
                if any(k in prev.lower() for k in keywords):
                    clean_name = re.sub(r'\(cid:\d+\)', '', prev).strip()
                    park_projects.append(clean_name)

# Match with funding data
fundings = []
for park in park_projects:
    park_lower = park.lower()
    for fund in funding_records:
        fund_lower = fund['Project_Name'].lower()
        if park_lower in fund_lower or fund_lower in park_lower:
            fundings.append({
                'project': park,
                'amount': fund['Amount']
            })
            break

# Calculate total
total = sum(f['amount'] for f in fundings)
result = {'total_funding': total, 'matched_projects': fundings}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
