code = """import json; import re

funding = var_functions.query_db_66
civic = var_functions.query_db_65

park_projects = []
for doc in civic:
    text = doc.get('text','')
    if 'park' in text.lower() and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                if line_clean not in park_projects:
                    park_projects.append(line_clean)

def clean(name):
    if not name:
        return ''
    name = re.sub(r'(?i)\s+Project\s*$','',name)
    name = re.sub(r'(?i)\s*-\s*Design\s*$','',name)
    name = re.sub(r'(?i)\s*-\s*Construction\s*$','',name)
    return name.strip().lower()

total = 0
funding_used = set()

for fund in funding:
    fund_name = fund.get('Project_Name','')
    fund_amount = int(fund.get('Amount',0))
    if not fund_name:
        continue
    fund_clean = clean(fund_name)
    if not fund_clean:
        continue
    for park in park_projects:
        park_clean = clean(park)
        if park_clean and (park_clean in fund_clean or fund_clean in park_clean):
            if fund_name not in funding_used:
                total = total + fund_amount
                funding_used.add(fund_name)
                break

result = {'total_funding':total,'unique_projects':len(funding_used)}
print('__RESULT__:'); print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
