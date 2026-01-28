code = """import json, re
civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

park_projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'completed' in text.lower() and '2022' in text and ('park' in text.lower() or 'playground' in text.lower()):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 5 and len(line) < 100 and line[0].isupper():
                if 'park' in line.lower() or 'playground' in line.lower():
                    next_text = ' '.join(lines[i:i+5]).lower()
                    if 'completed' in next_text and '2022' in next_text:
                        park_projects_2022.append(line)

unique_projects = list(set(park_projects_2022))
print('Projects found:', len(unique_projects))
for p in unique_projects:
    print('-', p)

total_funding = 0
matched = []
for project in unique_projects:
    proj_name_lower = project.lower()
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '').lower()
        if 'park' in fund_name and (proj_name_lower in fund_name or fund_name in proj_name_lower):
            amount = int(fund.get('Amount', 0))
            total_funding += amount
            matched.append(fund.get('Project_Name'))

print('\nMatched funding records:', len(set(matched)))
print('Total funding:', total_funding)
print('__RESULT__:')
print('Total funding for park-related projects completed in 2022 is $' + str(total_funding))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
