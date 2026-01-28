code = """import json
import re

civic_docs_file = vars()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for park in line (case-insensitive)
        if 'park' in line.lower() and len(line) > 5 and len(line) < 100:
            # Skip common headers
            skip_terms = ['schedule', 'updates', 'description', 'project', 'projects']
            if any(term in line.lower() for term in skip_terms):
                continue
                
            # Look ahead for 2022 completion
            for j in range(i, min(i+10, len(lines))):
                next_line = lines[j]
                if 'Construction was completed' in next_line and '2022' in next_line:
                    if line not in park_projects_2022:
                        park_projects_2022.append(line)
                    break

# Remove any empty or too-short entries
park_projects_2022 = [p for p in park_projects_2022 if len(p) > 8]

print('__RESULT__:')
print(json.dumps(park_projects_2022))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}}

exec(code, env_args)
