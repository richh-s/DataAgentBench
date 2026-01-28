code = """import json
import re

# Load the data
funding_data = var_functions.query_db_66
civic_docs_data = var_functions.query_db_65

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs_data), 'civic documents')

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    lower_text = text.lower()
    # Look for park projects with 2022 completion
    if 'park' in lower_text and '2022' in text and 'completed' in lower_text:
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                if line_clean not in park_projects:
                    park_projects.append(line_clean)

print('Found', len(park_projects), 'park projects with 2022 completion')

# Clean project names for matching
def clean_name(name):
    name = re.sub(r'(?i)\s+Project\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Design\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Construction\s*$', '', name)
    return name.strip().lower()

total = 0
for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    if not fund_name or fund_amount == 0:
        continue
    fund_clean = clean_name(fund_name)
    if not fund_clean:
        continue
    for park in park_projects:
        park_clean = clean_name(park)
        if park_clean and (park_clean in fund_clean or fund_clean in park_clean):
            total = total + fund_amount
            print('Matched:', park[:50], '->', fund_name[:50], '=', fund_amount)
            break

result = {'total_funding': total}
print('Result:', result)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
