code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
docs_file = locals()['var_functions.query_db:34']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for patterns: Project Name followed by "Construction was completed" and "2022"
    # The pattern captures project names that contain "Park" or "park"
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Check for lines containing park (likely project names)
        if 'park' in line_clean.lower():
            # Skip if it's a section/header
            if any(skip in line_clean for skip in ['Project Schedule', 'Updates:', 'Project Description', 'PAGE', 'Agenda']):
                continue
            if len(line_clean) < 8 or len(line_clean) > 150:
                continue
            
            # Look ahead for completion in 2022
            for j in range(i, min(i+8, len(lines))):
                next_line = lines[j]
                if 'Construction was completed' in next_line and '2022' in next_line:
                    # Clean up the project name
                    project_name = line_clean.strip()
                    if project_name and project_name not in park_projects_2022:
                        park_projects_2022.append(project_name)
                    break

# Also look for patterns where project name comes right before completion notice
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'Construction was completed' in line and '2022' in line:
            # Look back for the project name
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if 'park' in prev_line.lower():
                    if any(skip in prev_line for skip in ['Project Schedule', 'Updates:', 'Project Description']):
                        continue
                    if 8 < len(prev_line) < 150:
                        if prev_line not in park_projects_2022:
                            park_projects_2022.append(prev_line)
                        break

# Deduplicate while preserving order
unique_projects = []
for p in park_projects_2022:
    if p not in unique_projects:
        unique_projects.append(p)

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': unique_projects,
    'count': len(unique_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
