code = """import json
import re

# Load data
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Extract projects
projects = []

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if not line or line.startswith('Page') or line.startswith('Item'):
            continue
        
        if len(line) > 15 and line[0].isupper():
            next_text = ' '.join(lines[i+1:i+4]).lower()
            if 'updates' in next_text or 'schedule' in next_text:
                project = {
                    'name': line,
                    'has_spring_2022': False,
                    'status': '',
                    'type': 'capital'
                }
                
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j]
                    
                    if re.search(r'spring\s+2022', next_line, re.IGNORECASE):
                        project['has_spring_2022'] = True
                    if re.search(r'2022-\s*spring', next_line, re.IGNORECASE):
                        project['has_spring_2022'] = True
                    if re.search(r'2022.*mar|2022.*apr|2022.*may', next_line, re.IGNORECASE):
                        project['has_spring_2022'] = True
                    if re.search(r'2022.*03|2022.*04|2022.*05', next_line):
                        project['has_spring_2022'] = True
                    
                    low_line = next_line.lower()
                    if 'design' in low_line and ('complete' in low_line or 'final' in low_line):
                        project['status'] = 'design'
                    elif 'construction' in low_line:
                        project['status'] = 'construction'
                    elif 'not started' in low_line:
                        project['status'] = 'not started'
                    
                    if 'FEMA' in next_line or 'CalOES' in next_line or 'CalJPIA' in next_line:
                        project['type'] = 'disaster'
                
                projects.append(project)

spring_2022 = [p for p in projects if p['has_spring_2022']]
spring_2022_names = [p['name'] for p in spring_2022]

matches = []
total_funding = 0

for fund in funding_data:
    fund_name = fund['Project_Name'].lower()
    for project_name in spring_2022_names:
        proj_lower = project_name.lower()
        if proj_lower in fund_name or fund_name in proj_lower:
            matches.append({
                'project': project_name,
                'funding': fund['Project_Name'],
                'amount': int(fund['Amount'])
            })
            total_funding += int(fund['Amount'])
            break

result = {
    'spring_2022_projects_count': len(spring_2022),
    'spring_2022_projects': spring_2022_names,
    'funding_matches': matches,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
