code = """import json
import re

civic_docs_var = globals()['var_functions_query_db_0']
funding_var = globals()['var_functions_query_db_5']

civic_docs = civic_docs_var if isinstance(civic_docs_var, list) else eval(str(civic_docs_var))
funding_data = funding_var if isinstance(funding_var, list) else eval(str(funding_var))

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    filename = doc.get('filename', '')
    
    spring_patterns = ['2022-spring', 'spring 2022', '2022 spring', 'march 2022', 'april 2022', 'may 2022']
    project_indicators = ['project', 'improvements', 'repairs', 'replacement', 'facility', 'structure', 'road', 'park', 'drain', 'bridge']
    
    if any(pattern in text for pattern in spring_patterns):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if any(indicator in line for indicator in project_indicators):
                if 15 < len(line) < 200:
                    project_name = line.title().replace('Cid:190', '').replace('Cid:131', '').strip()
                    if project_name and len(project_name) > 10:
                        spring_2022_projects.append({
                            'project_name': project_name,
                            'filename': filename
                        })

unique_project_names = list(set([p['project_name'] for p in spring_2022_projects]))
print('Spring 2022 projects found:', len(unique_project_names))

results = []
for project_name in unique_project_names:
    project_funding = [f for f in funding_data if f['Project_Name'].lower() in project_name.lower() or project_name.lower() in f['Project_Name'].lower()]
    
    for fund in project_funding:
        results.append({
            'project_name': project_name,
            'funding_name': fund['Project_Name'],
            'amount': int(fund['Amount']),
            'source': fund['Funding_Source']
        })

total_funding = sum([r['amount'] for r in results])
print('Total funding for Spring 2022 projects:', total_funding)

print('__RESULT__:')
print(json.dumps({
    'project_count': len(unique_project_names),
    'total_funding': total_funding,
    'matching_funding_records': len(results),
    'projects': unique_project_names[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'civic_count': 5, 'funding_count': 500}}

exec(code, env_args)
