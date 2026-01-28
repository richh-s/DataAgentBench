code = """import json

# Load funding and civic documents
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:34']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract park projects completed in 2022 from civic documents
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Find patterns indicating park projects completed in 2022
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check if line is a park project name (contains park, reasonable length, not header)
        if 'park' in line.lower() and len(line) > 8:
            if len(line) < 100 and 'schedule' not in line.lower():
                
                # Check next few lines for completion in 2022
                for j in range(i+1, min(i+8, len(lines))):
                    next_line = lines[j]
                    if '2022' in next_line and 'completed' in next_line:
                        if line not in park_projects:
                            park_projects.append(line)
                        break

# Remove duplicates
unique_projects = []
for p in park_projects:
    if p not in unique_projects and p:
        unique_projects.append(p)

print('__RESULT__:')
print(json.dumps({
    'projects': unique_projects,
    'count': len(unique_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
