code = """import json
import re

# Load stored data
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:6']

# Load from files if needed
if type(civic_docs) is str:
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)
if type(funding_data) is str:
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert amounts to integers
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Find park projects completed in 2022
completed_park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    lines = [l.strip() for l in lines if l.strip()]
    
    for i, line in enumerate(lines):
        lower_line = line.lower()
        if '2022' in line and 'completed' in lower_line:
            # Look back for project name
            for j in range(max(0, i-6), i):
                prev_line = lines[j]
                if len(prev_line) > 100 or '(cid:' in prev_line:
                    continue
                
                park_terms = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs', 'skate park']
                if any(term in prev_line.lower() for term in park_terms):
                    clean_name = re.sub(r'\(cid:\d+\)', '', prev_line).strip()
                    completed_park_projects.append(clean_name)

# Match with funding records
matches = []
for project_name in completed_park_projects:
    project_lower = project_name.lower()
    for fund in funding_data:
        fund_lower = fund['Project_Name'].lower()
        if project_lower in fund_lower or fund_lower in project_lower:
            matches.append({'name': project_name, 'amount': fund['Amount']})
            break

# Calculate total funding
total = sum(m['amount'] for m in matches)

result = {'total_funding_2022_park_projects': total, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
