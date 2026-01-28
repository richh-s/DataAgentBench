code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:5']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_functions.query_db:16']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_map = {rec['Project_Name']: int(rec['Total_Amount']) for rec in funding_records}

spring_2022_projects = []
seen_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    project_patterns = [
        r'([A-Z][^.\n]{5,100}?)(?=\n\(cid:190\))',
        r'([A-Z][^.\n]{5,100}?)(?=\n\(cid:130\))',
    ]
    
    for pattern in project_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            project_name = match.group(1).strip()
            if len(project_name) < 5:
                continue
            
            has_2022 = '2022' in project_name
            schedule_section = text[match.end():match.end()+500]
            
            spring_2022_in_schedule = any(x in schedule_section for x in [
                '2022-Spring', 'Spring 2022', '2022-March', '2022-April', '2022-May',
                'March 2022', 'April 2022', 'May 2022', '2022 - Spring'
            ])
            
            if has_2022 or spring_2022_in_schedule:
                if project_name not in seen_projects:
                    seen_projects.add(project_name)
                    amount = funding_map.get(project_name, 0)
                    spring_2022_projects.append({
                        'name': project_name,
                        'funding': amount
                    })

project_names_to_check = [
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    '2022 Annual Street Maintenance',
]

for name in project_names_to_check:
    if name in str(civic_docs) and name not in seen_projects:
        seen_projects.add(name)
        amount = funding_map.get(name, 0)
        spring_2022_projects.append({
            'name': name,
            'funding': amount
        })

total_funding = sum(p['funding'] for p in spring_2022_projects)
result = f"Projects starting in Spring 2022: {len(spring_2022_projects)}\nTotal funding: ${total_funding:,}\n\nDetails:\n"
for p in spring_2022_projects:
    result += f"- {p['name']}: ${p['funding']:,}\n"

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': []}

exec(code, env_args)
