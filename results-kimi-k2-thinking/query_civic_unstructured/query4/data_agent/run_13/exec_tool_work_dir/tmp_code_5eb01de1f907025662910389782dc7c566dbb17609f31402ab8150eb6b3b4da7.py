code = """import json, re
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

# Extract projects that started in Spring 2022
spring_2022_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project name (potential)
        if len(line) > 10 and line[0].isupper() and not line.startswith('Page') and not line.startswith('Item'):
            # Check if next lines contain project details
            if i+1 < len(lines):
                next_lines = ' '.join(lines[i+1:min(i+8, len(lines))])
                if 'Complete Design:' in next_lines or 'Advertise:' in next_lines or 'Begin Construction:' in next_lines:
                    current_project = line
        
        # Look for Spring 2022 start dates
        if current_project:
            lower_line = line.lower()
            # Check for various patterns indicating Spring 2022 start
            if ('begin' in lower_line or 'advertise' in lower_line or 'start' in lower_line or 'complete' in lower_line) and \
               '2022' in line and ('spring' in lower_line or 'mar' in lower_line or 'apr' in lower_line or 'may' in lower_line):
                spring_2022_projects.add(current_project)
                current_project = None

# Convert set to list
project_list = list(spring_2022_projects)

# Match with funding data and sum amounts
total_funding = 0
matched_projects = []

for fund in funding:
    fund_name = fund['Project_Name'].lower()
    amount = int(fund['Amount'])
    
    for project in spring_2022_projects:
        proj_lower = project.lower()
        # Check for substring matches
        if proj_lower in fund_name or fund_name in proj_lower or \
           any(part in fund_name for part in proj_lower.split() if len(part) > 5):
            total_funding += amount
            matched_projects.append({'project': project, 'funding': fund['Project_Name'], 'amount': amount})
            break

result = {
    'spring_2022_projects_count': len(project_list),
    'total_funding': total_funding,
    'project_names': project_list,
    'matched_funding_count': len(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}}

exec(code, env_args)
