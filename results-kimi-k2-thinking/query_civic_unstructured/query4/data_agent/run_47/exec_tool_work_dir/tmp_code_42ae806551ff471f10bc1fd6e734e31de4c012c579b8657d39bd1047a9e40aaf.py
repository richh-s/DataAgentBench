code = """import json
import os

# Load the data files
civic_file_path = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_68.json'
funding_file_path = '/tmp/results/20250219_143343_sqlite_funding_database_query_12.json'

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Find Spring 2022 projects
spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Skip headers
        if line.isupper() and len(line) > 15 and not any(x in line for x in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:']):
            # Look for Spring 2022 in following lines
            following = '\n'.join(lines[i:i+15])
            if '2022' in following and 'pring' in following.lower():
                spring_projects.add(line)

project_list = sorted(list(spring_projects))
total_funding = 0

for proj in project_list:
    for fund in funding_data:
        if fund.get('Project_Name') == proj:
            total_funding += int(fund.get('Amount', 0))

result = {
    'project_count': len(project_list),
    'total_funding': total_funding,
    'projects': project_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:62': {'status': 'files_loaded'}, 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
