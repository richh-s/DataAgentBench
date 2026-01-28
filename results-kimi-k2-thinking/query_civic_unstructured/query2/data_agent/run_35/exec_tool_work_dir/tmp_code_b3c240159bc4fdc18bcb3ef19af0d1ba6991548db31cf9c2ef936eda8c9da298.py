code = """import json
import re

funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:34']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # First approach: find "Construction was completed ... 2022" and look back for park name
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Check if line mentions construction completed in 2022
        if 'Construction was completed' in line_clean and '2022' in line_clean:
            # Look back up to 5 lines for the project name
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                
                # Check if this line contains park (likely the project name)
                if 'park' in prev_line.lower() and len(prev_line) < 100:
                    # Skip if it's clearly a section header
                    if any(term in prev_line for term in ['Project Schedule', 'Updates:', 'Project Description', 'Agenda', 'Page']):
                        continue
                    
                    # This looks like a valid project name
                    if prev_line not in park_projects_2022:
                        park_projects_2022.append(prev_line)
                        break

# Also try forward search
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Find lines with park that look like project names
        if 'park' in line_clean.lower() and 8 < len(line_clean) < 100:
            if any(term in line_clean for term in ['Project Schedule', 'Updates:', 'Project Description', 'Agenda', 'Page']):
                continue
                
            # Look ahead for completion in 2022
            for j in range(i, min(i+8, len(lines))):
                next_line = lines[j]
                if 'Construction was completed' in next_line and '2022' in next_line:
                    if line_clean not in park_projects_2022:
                        park_projects_2022.append(line_clean)
                    break

# Deduplicate
park_projects_2022_final = []
for p in park_projects_2022:
    if p not in park_projects_2022_final:
        park_projects_2022_final.append(p)

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': park_projects_2022_final,
    'count': len(park_projects_2022_final)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
