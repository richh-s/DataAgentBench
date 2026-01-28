code = """import json; import re

civic_path = var_functions.query_db_118
funding_path = var_functions.query_db_107

with open(civic_path) as cf:
    civic_docs = json.load(cf)

with open(funding_path) as ff:
    funding = json.load(ff)

park_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    low = text.lower()
    if 'park' in low and '2022' in text and 'completed' in low:
        for line in text.split('\n'):
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                park_projects.append(line_clean)

def clean_name(name):
    name = re.sub(r'(?i)\s+Project\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Design\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Construction\s*$', '', name)
    return name.strip().lower()

total = 0
used = set()

for fund in funding:
    fund_name = fund.get('Project_Name','')
    fund_amount = int(fund.get('Amount',0))
    if not fund_name or fund_amount == 0:
        continue
    fund_clean = clean_name(fund_name)
    for park in park_projects:
        park_clean = clean_name(park)
        if park_clean and (park_clean in fund_clean or fund_clean in park_clean):
            if fund_name not in used:
                total = total + fund_amount
                used.add(fund_name)
                break

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.list_db:104': ['civic_docs'], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:118': 'file_storage/functions.query_db:118.json'}

exec(code, env_args)
