code = """import json
import re

# Get all civic documents
civic_docs = locals().get('var_functions.query_db:2')
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print(f'Total documents to process: {len(civic_docs)}')

# Initialize list to store extracted projects
extracted_projects = []

# Pattern to match project names (title case lines that look like project names)
project_name_pattern = r'^[A-Z][a-zA-Z&\s\-]+(?:Project|Repair|Improvements|Structure|Facility|Park|Study|Plan|System|Upgrades|Screens|Walkway|Road|Lane|Power|Biofilter|Phase\s*\d*|\(FEMA\s+Project\)|\(CalJPIA\s+Project\)|\(CalOES\s+Project\))*
[A-Z][a-zA-Z&\s\-]*$'

# Pattern to find completion dates
completion_patterns = [
    r'Construction was completed[,:]?\s*([A-Za-z]+(?:\s+\d{1,2},)?\s+2022)',
    r'Completed[,:]?\s*([A-Za-z]+(?:\s+\d{1,2},)?\s+2022)',
    r'Notice of completion filed[,:]?\s*([A-Za-z]+(?:\s+\d{1,2},)?\s+2022)',
    r'Complete Construction[,:]?\s*([A-Za-z]+(?:\s+\d{1,2},)?\s+2022)',
    r'completed,?\s*([A-Za-z]+\s+2022)',
    r'2022\s*-\s*([A-Za-z]+)\s*-?\s*completed'
]

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 5:
            continue
            
        # Check if this looks like a project name
        if re.match(project_name_pattern, line) and not line.startswith(('Agenda', 'Public', 'Capital', 'Disaster', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION')):
            # Save previous project if it exists
            if current_project:
                extracted_projects.append(current_project)
            
            # Start new project
            current_project = {
                'Project_Name': line,
                'topic': '',
                'status': 'unknown',
                'st': '',
                'et': '',
                'completion_date': '',
                'is_park_related': False,
                'is_2022_completed': False
            }
            
            # Check if park-related
            if 'park' in line.lower():
                current_project['is_park_related'] = True
                current_project['topic'] = 'park'
        
        # If we have a current project, look for status and dates
        if current_project:
            lower_line = line.lower()
            
            # Check for completion status in 2022
            if 'completed' in lower_line and '2022' in line:
                for pattern in completion_patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        current_project['status'] = 'completed'
                        current_project['completion_date'] = match.group(1)
                        current_project['is_2022_completed'] = True
                        break
                
                # If no specific date pattern matched but still contains completed + 2022
                if current_project['status'] != 'completed':
                    current_project['status'] = 'completed'
                    current_project['is_2022_completed'] = True
            
            # Check for park references in description
            if 'park' in lower_line and not current_project['is_park_related']:
                current_project['is_park_related'] = True
                current_project['topic'] = 'park'
    
    # Add last project if exists
    if current_project:
        extracted_projects.append(current_project)

# Filter park-related projects completed in 2022
park_projects_2022 = [p for p in extracted_projects if p['is_park_related'] and p['is_2022_completed']]

print('__RESULT__:')
print(json.dumps({
    'total_projects_extracted': len(extracted_projects),
    'park_projects_2022': len(park_projects_2022),
    'park_projects_2022_list': park_projects_2022
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'num_documents': 5, 'type': "<class 'list'>", 'data_preview': "[{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\n\\nChair Dittrich and Members of the Public Works Commission\\n\\nPrepared by:\\n\\nJorge Rubalcava, Senior Civil Engineer\\n\\nApproved by:\\n\\nRob DuBoux, Public Works Director/City Engineer\\n\\nDate prepared: March 15, 2023\\n\\nMeeting date: March 22, 2023\\n\\nSubject:\\n\\nCapital Improvement Projects and "}}

exec(code, env_args)
