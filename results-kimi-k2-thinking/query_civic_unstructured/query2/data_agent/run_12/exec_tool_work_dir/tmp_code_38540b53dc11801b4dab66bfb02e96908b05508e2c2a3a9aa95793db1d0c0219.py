code = """import json, re

funding_data = var_functions.query_db_5
civic_docs_data = var_functions.query_db_2

print('Starting analysis')
print('Funding records: ' + str(len(funding_data)))
print('Civic documents: ' + str(len(civic_docs_data)))

park_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    if 'park' in text.lower() and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                if line_clean not in park_projects:
                    park_projects.append(line_clean)

print('Park projects found: ' + str(len(park_projects)))

def clean_name(name):
    if not name:
        return ''
    name = re.sub(r'(?i)\s+Project\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Design\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Construction\s*$', '', name)
    return name.strip().lower()

total_funding = 0
for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    if not fund_name:
        continue
    fund_clean = clean_name(fund_name)
    for park in park_projects:
        park_clean = clean_name(park)
        if park_clean and (park_clean in fund_clean or fund_clean in park_clean):
            total_funding += fund_amount
            print('Match: ' + park + ' -> ' + fund_name + ' (' + str(fund_amount) + ')')
            break

print('Total funding: ' + str(total_funding))
result = {'total_funding': total_funding, 'park_projects_count': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}}

exec(code, env_args)
