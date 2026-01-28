code = """import json

# Read the full civic_docs result
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    documents = json.load(f)

park_projects = []

for doc in documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        if 'park' in line.lower() and len(line) < 150:
            skip_line = False
            skip_headers = [
                'capital improvement',
                'disaster recovery',
                'projects',
                'status report',
                'discussion',
                'recommended action'
            ]
            for header in skip_headers:
                if header in line.lower():
                    skip_line = True
                    break
            if line.startswith('('):
                skip_line = True
            if not line.strip():
                skip_line = True
                
            if skip_line:
                continue
                
            project_info = {
                'project_name': line,
                'completed_2022': False,
                'topic': 'park'
            }
            
            # Check next 10 lines for completion info
            for i in range(max(0, line_num), min(len(lines), line_num + 15)):
                next_line = lines[i].strip().lower()
                if 'completed' in next_line and '2022' in next_line:
                    project_info['completed_2022'] = True
                    break
                    
            park_projects.append(project_info)

# Remove duplicates
unique_projects = {}
for proj in park_projects:
    if proj['project_name'] not in unique_projects:
        unique_projects[proj['project_name']] = proj
        
park_projects_unique = list(unique_projects.values())
completed_2022 = [p for p in park_projects_unique if p['completed_2022']]

result = {
    'total_park_projects': len(park_projects_unique),
    'completed_2022_count': len(completed_2022),
    'completed_projects': completed_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
