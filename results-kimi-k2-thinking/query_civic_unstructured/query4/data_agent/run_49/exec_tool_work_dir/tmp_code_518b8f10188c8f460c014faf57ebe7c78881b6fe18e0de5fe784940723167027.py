code = """import json
import re

# Access the data from storage
civic_docs = var_functions.query_db:10
funding_records = var_functions.query_db:7

# If they are file paths, read them
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_records, str) and funding_records.endswith('.json'):
    with open(funding_records, 'r') as f:
        funding_records = json.load(f)

# Create funding map
funding_map = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[project_name] = amount

# Look for Spring 2022 projects
spring_projects = []

# Simple approach - look for project names that contain 2022 or Spring
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        # Look for project names that start the line (common pattern)
        if any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Drainage', 'Resurfacing']):
            if '2022' in line or any(month in line for month in ['Spring', 'March', 'April', 'May']):
                # Extract potential project name (first part of line)
                project_name = line.split('  ')[0].strip()
                if project_name and len(project_name) > 15:
                    spring_projects.append(project_name)

# Remove duplicates
spring_projects = list(set(spring_projects))

# Match with funding
matched_projects = []
total_funding = 0

for project in spring_projects:
    if project in funding_map:
        funding = funding_map[project]
        matched_projects.append({'name': project, 'funding': funding})
        total_funding += funding
    else:
        # Try partial matching
        for funded_project, amount in funding_map.items():
            if project in funded_project or funded_project in project:
                matched_projects.append({'name': project, 'funding': amount})
                total_funding += amount
                break

result = {
    'count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
