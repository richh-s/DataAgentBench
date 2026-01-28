code = """import json

# Load funding and civic documents data
with open('/tmp/results/20250219_143343_sqlite_funding_database_query_12.json', 'r') as f:
    funding_data = json.load(f)

with open('/tmp/results/20250219_143343_mongodb_civic_docs_database_query_42.json', 'r') as f:
    civic_docs = json.load(f)

print(f'Funding records: {len(funding_data)}')
print(f'Civic documents: {len(civic_docs)}')

# Find projects that started in Spring 2022
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty or short lines
        if not line or len(line) < 10:
            continue
        
        # Skip header lines
        if any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT', 'RECOMMENDED ACTION']):
            continue
        
        # Check for projects with 2022 in their name
        if '2022' in line and 'Page' not in line and 'AGENDA' not in line:
            spring_2022_projects.add(line)
        
        # Check for uppercase project names
        elif line.isupper() and len(line) > 15:
            look_ahead = '\n'.join(lines[i:i+20])
            if '2022' in look_ahead and 'pring' in look_ahead.lower() and 'Advertise' in look_ahead:
                spring_2022_projects.add(line)

# Clean results
final_projects = []
for proj in spring_2022_projects:
    if len(proj) > 15 and not proj.startswith('PAGE'):
        final_projects.append(proj)

final_projects.sort()
project_count = len(final_projects)

# Calculate total funding
total_funding = 0
for project_name in final_projects:
    for funding in funding_data:
        if funding.get('Project_Name') == project_name:
            total_funding += int(funding.get('Amount', 0))

print(f'Spring 2022 projects: {project_count}')
print(f'Total funding: ${total_funding:,}')
print(f'Projects: {final_projects}')

result = {
    'project_count': project_count,
    'total_funding': total_funding,
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
