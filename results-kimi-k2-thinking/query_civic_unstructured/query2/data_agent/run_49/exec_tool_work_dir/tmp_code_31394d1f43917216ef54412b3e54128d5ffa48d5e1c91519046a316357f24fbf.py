code = """import json
import re

result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    documents = json.load(f)

project_names = []

for doc in documents:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers
        if line[0] == '(' or line.startswith('Page') or line.startswith('Agenda'):
            continue
        
        # Look for what might be project names
        if line.istitle() and 'Project' not in line and len(line.split()) > 1:
            # Check if mentioned with completion in 2022
            snippet = ' '.join(lines[max(0,i-5):i+10])
            if 'completed' in snippet.lower() and '2022' in snippet:
                # Check if park-related
                if any(k in line.lower() or k in snippet.lower() for k in ['park','playground','bluffs','canyon']):
                    project_names.append(line)

# Get unique projects
unique_projects = list(set(project_names))
print('__RESULT__:')
print(json.dumps(unique_projects, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)
