code = """import json
import re

# Read civic documents
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract park projects completed in 2022 from documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Find patterns: project name lines containing 'park' and completion notices with '2022'
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for park project names (contain 'park', reasonable length, not a status/section header)
        if ('park' in line.lower() and len(line) > 5 and len(line) < 100 and 
            not line.startswith('(') and not line.startswith('•') and 
            'Project Schedule' not in line and 'Updates' not in line and 
            'Project Description' not in line):
            
            # Look ahead for completion status in next 10 lines
            completed_2022 = False
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                if 'Construction was completed' in next_line and '2022' in next_line:
                    completed_2022 = True
                    break
            
            if completed_2022:
                park_projects_2022.append({'name': line, 'completed_in_2022': True})

print('__RESULT__:')
print(json.dumps({
    'park_projects_completed_2022': park_projects_2022,
    'count': len(park_projects_2022)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}}

exec(code, env_args)
