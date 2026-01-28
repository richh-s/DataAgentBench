code = """import json, re

funding_data = var_functions.query_db_5
civic_docs_data = var_functions.query_db_2

park_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    if 'park' in text.lower() and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150 and line_clean not in park_projects:
                park_projects.append(line_clean)

def clean(n):
    if not n:
        return ''
    n = re.sub(r'(?i)\s+Project\s*$', '', n)
    n = re.sub(r'(?i)\s*-\s*Design\s*$', '', n)
    n = re.sub(r'(?i)\s*-\s*Construction\s*$', '', n)
    return n.strip().lower()

total = 0
for fund in funding_data:
    f_name = fund.get('Project_Name', '')
    f_amt = int(fund.get('Amount', 0))
    if not f_name:
        continue
    f_clean = clean(f_name)
    for park in park_projects:
        p_clean = clean(park)
        if p_clean and (p_clean in f_clean or f_clean in p_clean):
            total += f_amt
            break

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'park_projects_found': len(park_projects)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}}

exec(code, env_args)
