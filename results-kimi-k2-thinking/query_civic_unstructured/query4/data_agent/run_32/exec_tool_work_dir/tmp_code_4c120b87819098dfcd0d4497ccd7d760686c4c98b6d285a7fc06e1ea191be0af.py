code = """import json
import re

# Load data from files
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)
    
with open(locals()['var_functions.query_db:6'], 'r') as f:
    civic_data = json.load(f)

# Create funding lookup map
funding_map = {}
for item in funding_data:
    name = item.get('Project_Name')
    if name:
        amount = int(item.get('Amount', 0))
        funding_map[name] = funding_map.get(name, 0) + amount

# Extract Spring 2022 projects
spring_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Simple pattern: find sections mentioning both 2022 and Spring/March/April/May
    if '2022' in text and ('Spring' in text or 'March' in text or 'April' in text or 'May' in text):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) < 60 and line and line[0].isupper():
                # Check context for spring 2022
                context = '\n'.join(lines[i:i+10])
                has_2022_spring = (
                    '2022' in context and 
                    ('Spring' in context or 'March' in context or 'April' in context or 'May' in context)
                )
                if has_2022_spring:
                    spring_projects.append(line)

# Deduplicate
spring_projects = list(set(spring_projects))

# Match with funding
count = 0
total_fund = 0
matched_names = []

for proj in spring_projects:
    # Direct match
    if proj in funding_map:
        count += 1
        total_fund += funding_map[proj]
        matched_names.append(proj)
        continue
    
    # Fuzzy match for disaster projects with suffixes
    for funded_name in funding_map:
        if proj.lower() in funded_name.lower() or funded_name.lower() in proj.lower():
            count += 1
            total_fund += funding_map[funded_name]
            matched_names.append(proj)
            break

result = {
    'project_count': count,
    'total_funding': total_fund,
    'sample_projects': matched_names[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
