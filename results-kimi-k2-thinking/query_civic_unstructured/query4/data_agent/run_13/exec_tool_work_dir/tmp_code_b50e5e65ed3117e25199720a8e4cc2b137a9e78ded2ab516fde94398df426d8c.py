code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

spring_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        lower_line = line.lower()
        has_spring_2022 = False
        
        if 'spring' in lower_line and '2022' in lower_line:
            has_spring_2022 = True
        if '2022-spring' in lower_line:
            has_spring_2022 = True
        if '2022' in lower_line:
            if 'mar' in lower_line or 'apr' in lower_line or 'may' in lower_line:
                has_spring_2022 = True
        
        if has_spring_2022:
            project_name = None
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if (len(prev_line) > 15 and prev_line[0].isupper() and 
                    not prev_line.startswith('Page') and not prev_line.startswith('Item')):
                    if 'PUBLIC WORKS' not in prev_line and 'COMMISSION' not in prev_line:
                        project_name = prev_line
                        break
            
            if project_name:
                spring_projects.add(project_name)

project_list = sorted(list(spring_projects))

total_funding = 0
for fund in funding:
    fund_name_lower = fund['Project_Name'].lower()
    amount = int(fund['Amount'])
    
    for project in spring_projects:
        project_lower = project.lower()
        if project_lower in fund_name_lower or fund_name_lower in project_lower:
            total_funding += amount
            break

result = {
    'count': len(project_list),
    'total_funding': total_funding,
    'projects': project_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.execute_python:54': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.query_db:58': [{'total_funding': 'None', 'project_count': '0'}], 'var_functions.execute_python:64': {'spring_2022_projects': 4, 'total_funding': 83000}}

exec(code, env_args)
