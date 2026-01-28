code = """import json
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
    # Simple string search for spring 2022 patterns
    if ('Spring 2022' in text) or ('2022-Spring' in text) or ('2022 - Spring' in text):
        # Extract project names that appear near these dates
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project names (length > 10, starts with uppercase, not header)
            if len(line) > 10 and line[0].isupper() and not line.startswith('Page') and not line.startswith('Item'):
                if 'COMMISSION' not in line and 'AGENDA' not in line:
                    spring_2022_projects.add(line)

# Convert set to list for JSON serialization
project_list = list(spring_2022_projects)

# Match with funding data
total_funding = 0
matched_funding = []

for fund in funding:
    fund_name = fund['Project_Name'].lower()
    for proj_name in spring_2022_projects:
        proj_lower = proj_name.lower()
        # Check if project name matches funding record
        if proj_lower == fund_name or proj_lower in fund_name or fund_name in proj_lower:
            total_funding += int(fund['Amount'])
            matched_funding.append(fund['Project_Name'])
            break

result = {
    'count': len(spring_2022_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}}

exec(code, env_args)
