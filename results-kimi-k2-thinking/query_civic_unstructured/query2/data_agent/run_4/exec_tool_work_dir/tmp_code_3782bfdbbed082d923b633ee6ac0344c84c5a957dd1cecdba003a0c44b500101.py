code = """import json

# Get file paths from storage
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:6']

# Load data
with open(civic_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

# Convert amounts
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Find park projects completed in 2022
projects_found = []

for doc in civic_docs:
    text = doc['text']
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if 'completed' in line_lower and '2022' in line:
                for j in range(max(0, i-3), i):
                    prev = lines[j].strip()
                    park_terms = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs']
                    if any(term in prev.lower() for term in park_terms):
                        clean_name = prev.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                        if 10 < len(clean_name) < 80:
                            projects_found.append(clean_name)

# Match with funding
matches = []
for project in projects_found:
    proj_lower = project.lower()
    for fund in funding_data:
        fund_lower = fund['Project_Name'].lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matches.append({'name': project, 'amount': fund['Amount']})
            break

total = sum(m['amount'] for m in matches)

result = {'total_funding': total, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}}

exec(code, env_args)
