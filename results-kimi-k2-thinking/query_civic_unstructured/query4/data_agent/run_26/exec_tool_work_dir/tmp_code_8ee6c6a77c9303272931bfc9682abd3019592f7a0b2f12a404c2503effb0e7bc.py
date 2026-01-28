code = """import json, re

civic_docs = var_functions_query_db_36
funding_data = var_functions_query_db_34

print('Documents with Spring 2022:', len(civic_docs))
print('Total funding records:', len(funding_data))

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10 or line.startswith('Page'):
            continue
            
        proj_keywords = ['project', 'improvements', 'repairs', 'replacement', 'facility', 'road', 'park', 'drain', 'bridge']
        if any(keyword in line.lower() for keyword in proj_keywords):
            context = '\n'.join(lines[i:i+8])
            
            patterns = ['Begin.*Spring.*2022', 'Start.*Spring.*2022', '2022.*Spring.*Begin', '2022.*Spring.*Start']
            patterns.extend(['Begin.*(March|April|May).*2022', 'Start.*(March|April|May).*2022'])
            
            for pattern in patterns:
                if re.search(pattern, context, re.IGNORECASE):
                    name = re.sub(r'^(cid:\d+\s*)+', '', line)
                    name = re.sub(r'^[\-\*\•\d\.\s]+', '', name)
                    name = name.strip()
                    
                    if name and len(name) > 10:
                        spring_projects.append({'name': name, 'file': doc.get('filename')})
                        break

unique = {}
for p in spring_projects:
    if p['name'] not in unique:
        unique[p['name']] = p

spring_projects = list(unique.values())
print('Unique Spring 2022 projects:', len(spring_projects))

for i, p in enumerate(spring_projects[:10]):
    print(i+1, p['name'])

# Calculate funding
total = 0
matches = []
for project in spring_projects:
    proj_lower = project['name'].lower()
    for fund in funding_data:
        fund_lower = fund['Project_Name'].lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            total += int(fund['Amount'])
            matches.append({'proj': project['name'], 'fund': fund['Project_Name'], 'amount': int(fund['Amount'])})

print('Total funding:', total)
print('__RESULT__:')
print(json.dumps({'count': len(spring_projects), 'funding': total, 'matches': len(matches)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'civic_count': 5, 'funding_count': 500}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
