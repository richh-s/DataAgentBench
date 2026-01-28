code = """import json
import re

# Access the data file paths from storage
civic_file = var_functions.query_db_106
funding_file = var_functions.query_db_107

# Load the data
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'park' in line.lower() and len(line) < 150 and not line.startswith('('):
            context = ' '.join(lines[max(0,i-5):i+5]).lower()
            if 'completed' in context and '2022' in context:
                if line not in park_projects:
                    park_projects.append(line)

# Clean names

def clean(n):
    if not n:
        return ''
    n = re.sub(r'\s+Project\s*$', '', n, flags=re.IGNORECASE)
    n = re.sub(r'\s*-\s*Design\s*$', '', n, flags=re.IGNORECASE)
    n = re.sub(r'\s*-\s*Construction\s*$', '', n, flags=re.IGNORECASE)
    return n.strip().lower()

# Match funding
total = 0
used = set()

for fund in funding_records:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    if not fund_name or fund_amount == 0:
        continue
    fund_clean = clean(fund_name)
    if not fund_clean:
        continue
    for park in park_projects:
        park_clean = clean(park)
        if park_clean and (park_clean in fund_clean or fund_clean in park_clean):
            if fund_name not in used:
                total = total + fund_amount
                used.add(fund_name)
                break

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.list_db:104': ['civic_docs'], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json'}

exec(code, env_args)
