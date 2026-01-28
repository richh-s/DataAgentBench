code = """import json
import re

# Load data from storage
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:6']

with open(civic_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

# Convert amounts to integers
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Extract park projects completed in 2022
park_projects = []
for doc in civic_docs:
    lines = doc['text'].split('\n')
    for i, line in enumerate(lines):
        if '2022' in line and 'completed' in line.lower():
            for j in range(max(0, i-4), i):
                prev = lines[j].strip()
                if len(prev) > 100 or not prev:
                    continue
                park_terms = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs']
                if any(t in prev.lower() for t in park_terms):
                    clean_name = re.sub(r'\(cid:\d+\)', '', prev).strip()
                    if 10 < len(clean_name) < 80:
                        park_projects.append(clean_name)

# Match with funding data
matched = []
for park in park_projects:
    park_lower = park.lower()
    for fund in funding_data:
        fund_lower = fund['Project_Name'].lower()
        if park_lower in fund_lower or fund_lower in park_lower:
            matched.append({
                'project_name': park,
                'funding_name': fund['Project_Name'],
                'amount': fund['Amount']
            })
            break

total = sum(m['amount'] for m in matched)

result = {
    'total_funding_2022_park_projects': total,
    'number_of_projects': len(matched),
    'projects': matched
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}}

exec(code, env_args)
