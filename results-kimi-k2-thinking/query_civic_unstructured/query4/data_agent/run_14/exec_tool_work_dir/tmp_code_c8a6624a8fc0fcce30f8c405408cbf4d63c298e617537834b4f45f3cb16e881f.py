code = """import json
import re

civic_docs = locals().get('var_functions.query_db:2')
funding = locals().get('var_functions.query_db:5')

if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs

if isinstance(funding, str) and funding.endswith('.json'):
    with open(funding, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding

print('Loaded docs:', len(civic_docs_data), 'funding records:', len(funding_data))

funding_map = {record['Project_Name'].strip().lower(): int(record['Amount']) for record in funding_data}

spring_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    spring_indicators = ['2022-spring', '2022-march', '2022-april', '2022-may']
    has_spring_2022 = any(indicator in text_lower for indicator in spring_indicators)
    
    if has_spring_2022:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if any(indicator in line_lower for indicator in spring_indicators):
                project_name = None
                for j in range(i-1, max(i-4, -1), -1):
                    prev_line = lines[j].strip()
                    clean_line = prev_line.replace('●', '').replace('■', '').strip()
                    skip_terms = ['project schedule', 'updates:', 'complete design', 'advertise:', 'begin construction:']
                    if clean_line and len(clean_line) > 10 and not any(term in clean_line.lower() for term in skip_terms) and not clean_line.startswith('('):
                        project_name = clean_line
                        break
                
                if project_name:
                    project_key = project_name.lower()
                    funding_amount = 0
                    if project_key in funding_map:
                        funding_amount = funding_map[project_key]
                    else:
                        for funded_key, amount in funding_map.items():
                            if funded_key in project_key or project_key in funded_key:
                                funding_amount = amount
                                break
                    
                    spring_2022_projects.append({'name': project_name, 'funding': funding_amount})

unique_projects = {}
for proj in spring_2022_projects:
    name = proj['name']
    if name not in unique_projects or proj['funding'] > 0:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())
total_count = len(final_projects)
total_funding = sum(p['funding'] for p in final_projects)
funded_projects = [p for p in final_projects if p['funding'] > 0]

print('\nFinal Results:')
print('Projects:', total_count)
print('Total funding:', total_funding)
print('Funded projects:', len(funded_projects))

result = {'project_count': total_count, 'total_funding': total_funding, 'sample_projects': funded_projects[:5]}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
