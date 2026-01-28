code = """import json
import re

# Load data carefully
civic = var_functions.query_db_2
funding = var_functions.query_db_6

# Convert if file paths
if isinstance(civic, str):
    with open(civic, 'r') as f:
        civic = json.load(f)
if isinstance(funding, str):
    with open(funding, 'r') as f:
        funding = json.load(f)

# Convert amounts
for f in funding:
    f['Amount'] = int(f['Amount'])

# Find projects
projects = []
for doc in civic:
    t = doc['text']
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    
    for i in range(len(lines)):
        line = lines[i]
        if '2022' in line and 'completed' in line.lower():
            for j in range(max(0, i-5), i):
                prev = lines[j]
                if len(prev) < 80:
                    terms = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs']
                    if any(term in prev.lower() for term in terms):
                        clean = re.sub(r'\(cid:\d+\)', '', prev).strip()
                        projects.append(clean)

# Match funding
matches = []
for p in projects:
    p_lower = p.lower()
    for f in funding:
        f_lower = f['Project_Name'].lower()
        if p_lower in f_lower or f_lower in p_lower:
            matches.append({'name': p, 'amount': f['Amount']})
            break

total = sum(m['amount'] for m in matches)

print('__RESULT__:')
print(json.dumps({'total': total, 'matches': matches}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
