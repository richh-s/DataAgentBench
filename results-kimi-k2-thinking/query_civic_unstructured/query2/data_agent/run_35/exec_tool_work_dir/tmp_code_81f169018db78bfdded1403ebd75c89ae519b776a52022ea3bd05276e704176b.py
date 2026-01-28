code = """import json

# Load the civic documents from filtered results
civic_file = locals()['var_functions.query_db:34']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Split into lines and look for patterns
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Find park project names by looking for lines containing 'park'
        if 'park' in line.lower():
            # Skip if it's too short or too long
            if len(line) < 10 or len(line) > 150:
                continue
            
            # Skip known headers/sections
            if any(header in line for header in ['Project Schedule', 'Updates:', 'Project Description', 'Agenda', 'Page']):
                continue
            
            # Look ahead for completion notice with 2022
            for j in range(i, min(i+10, len(lines))):
                next_line = lines[j]
                if 'Construction was completed' in next_line and '2022' in next_line:
                    if line not in park_projects_2022:
                        park_projects_2022.append(line)
                    break

# Deduplicate
final_projects = []
for p in park_projects_2022:
    if p not in final_projects:
        final_projects.append(p)

result = {'projects': final_projects, 'count': len(final_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
