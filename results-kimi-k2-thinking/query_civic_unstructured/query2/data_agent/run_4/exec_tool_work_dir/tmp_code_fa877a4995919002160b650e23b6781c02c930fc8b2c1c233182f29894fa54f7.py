code = """import json
import re

# Load data from storage
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:6']

# Load from file paths if needed
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert amounts to integers
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Extract park projects completed in 2022
matched_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        if '2022' in line and 'completed' in line.lower():
            # Look back for project name
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if not prev_line or len(prev_line) > 100:
                    continue
                
                # Check if park-related
                park_words = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs']
                if any(word in prev_line.lower() for word in park_words):
                    clean_name = re.sub(r'\(cid:\d+\)', '', prev_line).strip()
                    
                    # Find matching funding
                    clean_lower = clean_name.lower()
                    for fund in funding_data:
                        fund_name = fund['Project_Name'].lower()
                        if clean_lower in fund_name or fund_name in clean_lower:
                            matched_projects.append({
                                'project': clean_name,
                                'funding': fund['Project_Name'],
                                'amount': fund['Amount']
                            })
                            break
                            
# Calculate total
total_funding = sum(p['amount'] for p in matched_projects)

result = {'total_funding': total_funding, 'projects': matched_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
