code = """import json, re

civic_file = var_functions.query_db_118
funding_file = var_functions.query_db_107

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Extract park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line_clean = line.strip()
        if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
            park_projects.append(line_clean)

# Calculate total funding for matching projects
total_funding = 0
seen = set()

for fund in funding_records:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    if not fund_name or fund_amount == 0 or fund_name in seen:
        continue
    
    for park in park_projects:
        if park.lower() in fund_name.lower() or fund_name.lower() in park.lower():
            total_funding = total_funding + fund_amount
            seen.add(fund_name)
            break

result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.list_db:104': ['civic_docs'], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:118': 'file_storage/functions.query_db:118.json'}

exec(code, env_args)
