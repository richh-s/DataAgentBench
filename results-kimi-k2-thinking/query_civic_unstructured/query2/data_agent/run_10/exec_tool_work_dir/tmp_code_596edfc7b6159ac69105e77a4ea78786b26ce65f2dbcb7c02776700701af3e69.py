code = """import json
import re

# Get all civic documents
civic_docs = locals().get('var_functions.query_db:2')
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print(f'Total documents: {len(civic_docs)}')

# Initialize list for extracted projects
projects = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    in_project_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect if we're in project listings
        if 'Capital Improvement Projects' in line or 'Disaster Recovery Projects' in line:
            in_project_section = True
            continue
        
        # Detect project names - simpler pattern
        if in_project_section and line and line[0].isupper() and len(line) > 10:
            # Skip headers
            if any(skip in line for skip in ['Commission', 'Agenda', 'Public Works', 'City', 'Staff', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'Page']):
                continue
            
            # Save previous project
            if current_project:
                projects.append(current_project)
            
            # Create new project record
            current_project = {
                'Project_Name': line,
                'is_park': 'park' in line.lower(),
                'completed_2022': False,
                'completion_note': ''
            }
        
        # Look for completion info
        if current_project and '2022' in line and 'completed' in line.lower():
            current_project['completed_2022'] = True
            current_project['completion_note'] = line
            
            # Also check if park-related in description
            if 'park' in line.lower():
                current_project['is_park'] = True
    
    # Save last project
    if current_project:
        projects.append(current_project)

# Filter for park projects completed in 2022
park_projects = [p for p in projects if p['is_park'] and p['completed_2022']]

print('__RESULT__:')
print(json.dumps({
    'total_projects': len(projects),
    'park_projects_completed_2022': len(park_projects),
    'park_projects': park_projects
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}}

exec(code, env_args)
