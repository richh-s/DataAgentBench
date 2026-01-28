code = """import json
import re

# Load data from previous queries
civic_docs = var_functions.query_db_2
funding_data = var_functions.query_db_6

# If these are file paths, read them
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert funding amounts to integers
for rec in funding_data:
    rec['Amount'] = int(rec['Amount'])

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text_lines = doc['text'].split('\n')
    
    for i, line in enumerate(text_lines):
        line_clean = line.strip()
        lower_line = line_clean.lower()
        
        if '2022' in line_clean and 'completed' in lower_line:
            for j in range(max(0, i-5), i):
                prev = text_lines[j].strip()
                if len(prev) < 80 and '(cid:' not in prev:
                    park_terms = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs']
                    if any(term in prev.lower() for term in park_terms):
                        clean_name = re.sub(r'\(cid:\d+\)', '', prev).strip()
                        park_projects.append(clean_name)

# Match with funding
funding_matches = []
for park_name in park_projects:
    park_lower = park_name.lower()
    for fund in funding_data:
        fund_lower = fund['Project_Name'].lower()
        if park_lower in fund_lower or fund_lower in park_lower:
            funding_matches.append({
                'project': park_name,
                'funding_name': fund['Project_Name'],
                'amount': fund['Amount']
            })
            break

# Calculate total
total_funding = sum(f['amount'] for f in funding_matches)

result = {
    'total_funding': total_funding,
    'project_count': len(funding_matches),
    'projects': funding_matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
