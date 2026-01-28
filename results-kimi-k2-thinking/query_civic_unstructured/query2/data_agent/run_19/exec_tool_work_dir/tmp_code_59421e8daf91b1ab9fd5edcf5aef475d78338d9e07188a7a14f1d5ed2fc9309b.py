code = """import json
import re

# Load the funding records
f_path = locals()['var_functions.query_db:0']
with open(f_path, 'r') as f:
    funding_records = json.load(f)

# Load the civic documents
c_path = locals()['var_functions.query_db:14']
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Define park keywords
park_keywords = ['park', 'playground', 'arbors', 'recreation']

# Get all funding records that are park-related
park_funding = [f for f in funding_records if any(kw in f['Project_Name'].lower() for kw in park_keywords)]

# Find projects completed in 2022 from civic docs
completed_2022 = []
for doc in civic_docs:
    text = doc['text']
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for line in lines:
            if '2022' in line and 'completed' in line.lower():
                for pf in park_funding:
                    if pf['Project_Name'].lower().split()[0] in line.lower():
                        completed_2022.append(pf)

# Calculate total
total = sum(int(p['Amount']) for p in completed_2022)

print('__RESULT__:')
print(json.dumps({'total': total, 'projects': len(completed_2022)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
