code = """import json
import re

# Get all civic documents
civic_docs = locals().get('var_functions.query_db:2')
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print('Processing documents...')

# Initialize list to store extracted projects
extracted_projects = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
            
        # Detect project names - look for title case lines that aren't headers
        if (line[0].isupper() and 
            len(line) > 8 and 
            not line.startswith(('Agenda', 'Public', 'Capital', 'Disaster', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Page', 'Item')) and
            not any(keyword in line for keyword in ['Commission', 'Department', 'City', 'Staff', 'Project Schedule', 'Project Updates', 'Updates:'])):
            
            # Save previous project
            if current_project:
                extracted_projects.append(current_project)
            
            # Start new project
            current_project = {
                'Project_Name': line,
                'topic': '',
                'status': 'unknown',
                'completion_date': '',
                'is_park_related': 'park' in line.lower(),
                'is_2022_completed': False
            }
            
            if current_project['is_park_related']:
                current_project['topic'] = 'park'
        
        # If we have a current project, look for status and dates
        if current_project:
            lower_line = line.lower()
            
            # Check for completion in 2022
            if 'completed' in lower_line and '2022' in line:
                current_project['status'] = 'completed'
                current_project['is_2022_completed'] = True
                
                # Try to extract the exact date
                date_match = re.search(r'([A-Za-z]+(?:\s+\d{1,2},?)?\s+2022)', line)
                if date_match:
                    current_project['completion_date'] = date_match.group(1)
            
            # Check for park references in description
            if 'park' in lower_line:
                current_project['is_park_related'] = True
                current_project['topic'] = 'park'
    
    # Add last project from document
    if current_project:
        extracted_projects.append(current_project)

# Filter park-related projects completed in 2022
park_projects_2022 = [p for p in extracted_projects if p['is_park_related'] and p['is_2022_completed']]

print('__RESULT__:')
print(json.dumps({
    'total_extracted': len(extracted_projects),
    'park_completed_2022': len(park_projects_2022),
    'projects': park_projects_2022
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}}

exec(code, env_args)
