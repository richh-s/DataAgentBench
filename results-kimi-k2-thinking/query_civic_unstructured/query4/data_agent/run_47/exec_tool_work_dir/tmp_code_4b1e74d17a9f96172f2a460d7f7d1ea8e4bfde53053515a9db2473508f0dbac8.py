code = """import json
import os

# Load the full MongoDB results
result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_32.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total documents: {len(civic_docs)}")

# Find projects that started in Spring 2022
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if line could be a project name
        is_project = False
        
        # Projects with year in name (like "2022 Morning View...")
        if '2022' in line and len(line) > 10:
            if not any(skip in line for skip in ['Page', 'AGENDA ITEM', 'SUBJECT:', 'DATE']):
                is_project = True
        
        # Uppercase project names
        if line.isupper() and len(line) > 15:
            if not any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:']):
                # Check following text for Spring 2022 scheduling
                following = '\n'.join(lines[i:i+10])
                if '2022' in following and 'pring' in following.lower():
                    is_project = True
        
        if is_project:
            spring_2022_projects.add(line)

# Clean and organize results
project_names = sorted(list(spring_2022_projects))
print(f"Spring 2022 projects found: {len(project_names)}")
for name in project_names:
    print(f"  - {name}")

result = {'count': len(project_names), 'projects': project_names}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
