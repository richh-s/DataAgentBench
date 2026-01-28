code = """import json, re

civic_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

# Extract project names that have Spring 2022 dates
spring_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Look for project name pattern
        if len(line) > 10 and line[0].isupper() and not (line.startswith('Page') or line.startswith('Item')):
            # Check if following lines mention dates
            following_text = ' '.join(lines[i:min(i+10, len(lines))]).lower()
            if ('2022' in following_text and 'spring' in following_text) or '2022-spring' in following_text:
                current_project = line
                # Now look for actual Spring 2022 mention
                for j in range(i, min(i+8, len(lines))):
                    next_line = lines[j].lower()
                    if ('2022' in next_line and 'spring' in next_line) or \
                       ('2022' in next_line and ('mar' in next_line or 'apr' in next_line or 'may' in next_line)):
                        spring_projects.add(current_project)
                        break

# Count and fund
project_list = list(spring_projects)

# Match funding - sum amounts for projects with 2022 in their names
spring_funding = 0
for fund in funding:
    name = fund['Project_Name']
    if '2022' in name and any(x in name.lower() for x in ['spring', 'mar', 'apr', 'may']):
        spring_funding += int(fund['Amount'])

result = {'count': len(project_list), 'total_funding': spring_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.execute_python:54': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.query_db:58': [{'total_funding': 'None', 'project_count': '0'}]}

exec(code, env_args)
