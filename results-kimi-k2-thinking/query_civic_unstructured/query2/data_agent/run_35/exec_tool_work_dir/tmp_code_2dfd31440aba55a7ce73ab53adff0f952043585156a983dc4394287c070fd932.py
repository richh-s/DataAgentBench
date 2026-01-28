code = """import json
import re

civic_docs_file = locals()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Check if line looks like a project name and contains 'park'
        if ('park' in line_clean.lower() and 5 < len(line_clean) < 100 and 
            not line_clean.startswith('(') and 'Project Schedule' not in line_clean and
            'Updates' not in line_clean and 'Project Description' not in line_clean):
            
            # Look ahead for completion in 2022
            for j in range(i, min(i + 10, len(lines))):
                next_line = lines[j]
                if 'Construction was completed' in next_line and '2022' in next_line:
                    park_projects.append(line_clean)
                    break

# Remove duplicates while preserving order
unique_park_projects = []
for p in park_projects:
    if p not in unique_park_projects:
        unique_park_projects.append(p)

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': unique_park_projects,
    'count': len(unique_park_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}}

exec(code, env_args)
