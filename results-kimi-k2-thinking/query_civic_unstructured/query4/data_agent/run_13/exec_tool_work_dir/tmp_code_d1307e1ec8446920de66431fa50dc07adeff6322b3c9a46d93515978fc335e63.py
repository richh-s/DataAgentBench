code = """import json

civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

spring_2022_starts = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (all caps or title case, not headers)
        if len(line) > 10 and line == line.upper() and not any(x in line for x in ['PAGE', 'ITEM', 'PUBLIC WORKS', 'COMMISSION', 'AGENDA', 'MINUTES', 'REPORT']):
            current_project = line
            continue
        
        # Look for start dates mentioning Spring 2022
        if current_project and '2022' in line:
            lower_line = line.lower()
            # Check if this line mentions beginning/advertising/starting in Spring 2022
            if ('spring' in lower_line or 'mar' in lower_line or 'apr' in lower_line or 'may' in lower_line) and \
               ('begin' in lower_line or 'advertise' in lower_line or 'start' in lower_line or 'complete' in lower_line):
                spring_2022_starts.append(current_project)
                current_project = None

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_2022_starts))

# Match with funding
matched_funding = 0
for fund in funding:
    fund_name = fund['Project_Name'].lower()
    for project in unique_projects:
        proj_lower = project.lower()
        if proj_lower in fund_name or fund_name in proj_lower:
            matched_funding += int(fund['Amount'])
            break

result = {
    'spring_2022_projects': len(unique_projects),
    'total_funding': matched_funding,
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}}

exec(code, env_args)
