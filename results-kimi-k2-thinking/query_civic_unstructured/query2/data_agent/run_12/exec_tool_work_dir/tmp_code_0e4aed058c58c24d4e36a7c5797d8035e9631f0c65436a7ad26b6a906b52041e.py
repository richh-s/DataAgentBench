code = """import json, re
funding_data = var_functions.query_db_66
civic_docs_data = var_functions.query_db_65
park_projects = []
for doc in civic_docs_data:
    text = doc.get('text','')
    low_text = text.lower()
    if 'park' in low_text and '2022' in text and 'completed' in low_text:
        lines = text.splitlines()
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                park_projects.append(line_clean)

def clean_name(n):
    if not n:
        return ''
    n = re.sub(r'(?i)\s+Project\s*$','',n)
    n = re.sub(r'(?i)\s*-\s*Design\s*$','',n)
    n = re.sub(r'(?i)\s*-\s*Construction\s*$','',n)
    return n.strip().lower()

total = 0
used = []
for fund in funding_data:
    fund_name = fund.get('Project_Name','')
    if not fund_name:
        continue
    amount = int(fund.get('Amount',0))
    clean_fund = clean_name(fund_name)
    if not clean_fund:
        continue
    for park in park_projects:
        clean_park = clean_name(park)
        if clean_park and (clean_park in clean_fund or clean_fund in clean_park):
            if fund_name not in used:
                total = total + amount
                used.append(fund_name)

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
