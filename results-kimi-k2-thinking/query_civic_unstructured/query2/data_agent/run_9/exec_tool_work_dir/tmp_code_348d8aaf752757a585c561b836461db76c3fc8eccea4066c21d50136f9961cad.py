code = """import json
import re

file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    all_documents = json.load(f)

park_projects = []

for doc in all_documents:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Find park projects completed in 2022
    # Look for patterns containing Park and 2022 completion
    patterns = [
        'Park.*2022.*completed',
        'completed.*2022.*Park',
        'Park.*construction was completed.*2022'
    ]
    
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE | re.DOTALL):
            # Extract project name
            lines = text.split('\n')
            for line in lines:
                if 'Park' in line and len(line.strip()) > 10:
                    clean_name = line.strip()
                    # Filter out obvious non-project lines
                    if 'Page' not in clean_name and not clean_name.startswith('---'):
                        park_projects.append(clean_name)
                        break

print('Found', len(park_projects), 'projects')
print('Unique projects:', len(set(park_projects)))

result = list(set(park_projects))
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
