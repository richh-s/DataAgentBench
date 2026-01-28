code = """import json
import re

# Load data from file paths
civic_path = var_functions.query_db_65
funding_path = var_functions.query_db_66

with open(civic_path, 'r') as cf:
    civic_docs_data = json.load(cf)

with open(funding_path, 'r') as ff:
    funding_data = json.load(ff)

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    low_text = text.lower()
    if 'park' in low_text and '2022' in text and 'completed' in low_text:
        for line in text.split('\n'):
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                if line_clean not in park_projects:
                    park_projects.append(line_clean)

# Clean project names
def clean_name(name):
    name = re.sub(r'(?i)\s+Project\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Design\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Construction\s*$', '', name)
    return name.strip().lower()

# Calculate total funding for matching park projects
total_funding = 0
for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    if not fund_name:
        continue
    fund_amount = int(fund.get('Amount', 0))
    fund_clean = clean_name(fund_name)
    if not fund_clean:
        continue
    for park in park_projects:
        park_clean = clean_name(park)
        if park_clean and (park_clean in fund_clean or fund_clean in park_clean):
            total_funding = total_funding + fund_amount
            break

result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
