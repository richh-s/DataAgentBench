code = """import json
import re

# Load data
civic_path = var_functions.query_db_118
funding_path = var_functions.query_db_107

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_records = json.load(f)

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    low = text.lower()
    if 'park' in low and '2022' in text and 'completed' in low:
        for line in text.split('\n'):
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                park_projects.append(line_clean)

print('Park projects found:', len(park_projects))

# Sum matching funding
total = 0
matched = set()

for fund in funding_records:
    fund_name = fund.get('Project_Name','')
    if not fund_name:
        continue
    amount = int(fund.get('Amount',0))
    fund_low = fund_name.lower()
    for park in park_projects:
        park_low = park.lower()
        if park_low in fund_low or fund_low in park_low:
            if fund_name not in matched:
                total += amount
                matched.add(fund_name)

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.list_db:104': ['civic_docs'], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:118': 'file_storage/functions.query_db:118.json'}

exec(code, env_args)
