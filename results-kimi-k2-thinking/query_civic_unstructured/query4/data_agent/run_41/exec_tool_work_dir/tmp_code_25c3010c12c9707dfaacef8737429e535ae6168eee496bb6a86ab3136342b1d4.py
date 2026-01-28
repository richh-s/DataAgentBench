code = """import json
import re

# Load the filtered documents
with open('/tmp/tmp_zu5y9j5.json', 'r') as f:
    spring_docs = json.load(f)

print('Number of Spring 2022 documents:', len(spring_docs))

spring_2022_projects = []

for doc in spring_docs:
    text = doc['text']
    
    # Split by lines and look for patterns
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if line contains Spring 2022 and construction/advertise keywords
        if ('Spring 2022' in line or '2022-Spring' in line) and \
           any(keyword in line.lower() for keyword in ['begin', 'construction', 'advertise', 'complete design', 'start']):
            
            # Look backward for project name
            project_name = None
            for j in range(i-1, max(-1, i-10), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('•'):
                    if len(prev_line) < 150 and not any(word in prev_line.lower() for word in ['update', 'schedule', 'description']):
                        project_name = prev_line
                        break
            
            if project_name:
                spring_2022_projects.append(project_name)

# Get unique projects
unique_projects = list(set(spring_2022_projects))

print('Unique Spring 2022 projects:', len(unique_projects))
print('\nProjects:')
for name in sorted(unique_projects):
    print('-', name)

result = {
    'count': len(unique_projects),
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
