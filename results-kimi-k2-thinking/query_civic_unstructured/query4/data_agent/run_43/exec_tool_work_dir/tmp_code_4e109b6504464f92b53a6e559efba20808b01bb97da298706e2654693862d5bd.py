code = """import json
import re

# Load civic documents from the query result file
civic_file = locals()['var_functions.query_db:22']
civic_docs = []
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data from the query result file
funding_file = locals()['var_functions.query_db:19']
funding_list = []
with open(funding_file, 'r') as f:
    funding_list = json.load(f)

# Create a dictionary for quick funding lookup
funding_lookup = {}
for item in funding_list:
    funding_lookup[item['Project_Name']] = int(item['Total_Amount'])

# Define patterns for Spring 2022
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

# Extract projects that started in Spring 2022
spring_projects = set()

for doc in civic_docs:
    text = doc['text']
    for pattern in spring_patterns:
        if pattern in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if len(line) > 10 and (line.istitle() or line.isupper()):
                    if 'Project' in line or 'Improvements' in line or 'Repair' in line:
                        clean_line = re.sub(r'[^\w\s&-]', '', line)
                        clean_line = re.sub(r'\s+', ' ', clean_line).strip()
                        spring_projects.add(clean_line)
                        break

# Find matching funding for these projects
total_funding = 0
matched_projects = []

for project in spring_projects:
    if project in funding_lookup:
        amount = funding_lookup[project]
        total_funding += amount
        matched_projects.append({'name': project, 'funding': amount})
    else:
        base_name = project.split('(')[0].strip()
        if base_name in funding_lookup:
            amount = funding_lookup[base_name]
            total_funding += amount
            matched_projects.append({'name': project, 'funding': amount})

# Prepare result
result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}]}

exec(code, env_args)
