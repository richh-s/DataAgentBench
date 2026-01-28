code = """import json, re

funding_data = var_functions.query_db_5
civic_docs_data = var_functions.query_db_2

# Find park-related projects completed in 2022
park_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for park and 2022 and completed in the same text
    lower_text = text.lower()
    if 'park' in lower_text and '2022' in lower_text and ('completed' in lower_text or 'construction was completed' in lower_text):
        # Extract specific project lines
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if not line_clean or len(line_clean) > 100:
                continue
            if 'park' in line_clean.lower():
                park_projects.append(line_clean)
                print('Park project found:', line_clean)

def clean_name(name):
    if not name:
        return ''
    name = re.sub(r'(?i)\s+Project\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Design\s*$', '', name)
    name = re.sub(r'(?i)\s*-\s*Construction\s*$', '', name)
    return name.strip().lower()

# Calculate total funding for matched park projects
total_funding = 0
matches = []

for park in park_projects:
    park_clean = clean_name(park)
    if not park_clean:
        continue
    for fund in funding_data:
        fund_project = fund.get('Project_Name', '')
        fund_clean = clean_name(fund_project)
        if fund_clean and (park_clean in fund_clean or fund_clean in park_clean):
            amount = int(fund.get('Amount', 0))
            total_funding += amount
            matches.append({'park': park, 'fund': fund_project, 'amount': amount})
            print('Matched park to funding:', park, '->', fund_project, '=', amount)

result = {'total_funding': total_funding, 'matches': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}}

exec(code, env_args)
