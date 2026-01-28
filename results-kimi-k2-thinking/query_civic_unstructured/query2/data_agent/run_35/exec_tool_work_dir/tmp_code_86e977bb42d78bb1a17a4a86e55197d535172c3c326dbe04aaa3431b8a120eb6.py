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
    filename = doc.get('filename', '')
    
    # Find project sections - they typically have project names followed by updates
    # Look for patterns like "Project Name\n\n(•) Updates:" or "Project Name\n\n(•) Project Description:"
    
    # Split by common project section markers
    # Look for sections that start with a project name and have updates
    
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and known headers
        if not line or line in ['Agenda Item # 4.B.', 'Public Works Commission', 'Agenda Report', 'Item', 'To:', 'Prepared by:', 'Approved by:', 
                               'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 
                               'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 
                               'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
            i += 1
            continue
        
        # Check if this line looks like a project name (not a bullet/update marker, not a date)
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('(') and \
           'COMPLETE' not in line.upper() and 'Construction was completed' not in line and \
           'Project Schedule' not in line and 'Updates' not in line and 'Project Description' not in line:
            
            possible_project_name = line
            
            # Look ahead to find updates/status for this project
            j = i + 1
            project_info = {
                'name': possible_project_name,
                'topics': '',
                'status': '',
                'et': '',  # end time
                'found_in_file': filename
            }
            
            # Check if this is a park-related project
            if 'park' in possible_project_name.lower():
                project_info['topics'] = 'park'
            
            # Look for completion status and dates
            while j < len(lines):
                next_line = lines[j].strip()
                
                # Check if we've reached the next project (next line might be a new project name)
                if next_line and not next_line.startswith('(') and not next_line.startswith('•') and \
                   'COMPLETE' not in next_line.upper() and 'Construction was completed' not in next_line and \
                   'Project Schedule' not in next_line and 'Updates' not in next_line and \
                   'Project Description' not in next_line and j > i + 5:
                    # This might be a new project, break
                    if 'Project' in next_line or len(next_line) < 50:
                        break
                
                if 'Construction was completed' in next_line:
                    project_info['status'] = 'completed'
                    # Extract year from completion date
                    year_match = re.search(r'(\d{4})', next_line)
                    if year_match:
                        project_info['et'] = year_match.group(1)
                    break
                
                j += 1
            
            # Only add if it's a park project and completed in 2022
            if project_info['topics'] == 'park' and project_info['status'] == 'completed' and project_info['et'] == '2022':
                projects.append(project_info)
            
            i = j
        else:
            i += 1

print('__RESULT__:')
print(json.dumps({
    'park_projects_completed_2022': projects,
    'count': len(projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}}

exec(code, env_args)
