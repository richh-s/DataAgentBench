code = """import json
import re

# Read civic documents
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all park-related projects with completion dates
    # Look for patterns like "Bluffs Park Shade Structure" followed by "Construction was completed, November 2022"
    
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if line contains "park" (case-insensitive) and looks like a project name
        if 'park' in line.lower() and len(line) > 5 and not line.startswith('(') and 'Project' not in line:
            # Check if this is a project name (not too long, not a status line)
            if len(line) < 100 and 'Schedule' not in line and 'Updates' not in line and 'Description' not in line:
                
                # Look ahead for completion status
                project_info = {
                    'name': line,
                    'completed_in_2022': False
                }
                
                # Look at next few lines for completion status
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    if 'Construction was completed' in next_line and '2022' in next_line:
                        project_info['completed_in_2022'] = True
                        break
                
                projects.append(project_info)

# Filter for projects completed in 2022
park_projects_2022 = [p for p in projects if p['completed_in_2022']]

print('__RESULT__:')
print(json.dumps({
    'park_projects_completed_2022': park_projects_2022,
    'count': len(park_projects_2022)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}}

exec(code, env_args)
