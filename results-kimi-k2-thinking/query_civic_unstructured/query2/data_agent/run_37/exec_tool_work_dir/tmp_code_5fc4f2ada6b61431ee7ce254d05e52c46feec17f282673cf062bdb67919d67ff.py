code = """import json
import re

# Read the civic documents data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Read the funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Function to extract project information from civic documents
def extract_projects_from_docs(docs):
    projects = []
    
    for doc in docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        current_project = None
        project_text = []
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            # Skip obvious headers and metadata
            skip_terms = [
                'Public Works', 'Commission', 'Agenda', 'Prepared by', 'Approved by',
                'Date prepared', 'Meeting date', 'Subject', 'RECOMMENDED ACTION',
                'DISCUSSION', 'To:', 'Page', 'Agenda Item', 'Capital Improvement',
                'Disaster Recovery', 'Staff', 'City', 'Project Schedule', 'Updates'
            ]
            
            if any(term in line for term in skip_terms):
                continue
            
            # Look for project-like names (not bullet points, not dates, etc.)
            if (len(line) > 10 and 
                not line.startswith('•') and 
                not line.startswith('-') and
                not line.startswith('(') and
                not re.match(r'^[A-Z\s]+$', line) and  # Not all caps headers
                not re.match(r'^\d{1,2}/\d{1,2}/\d{4}', line) and  # Not dates
                not ':' in line):  # Not labels
                
                # This looks like a project name
                if current_project and project_text:
                    project_info = parse_project_text(current_project, project_text, doc)
                    if project_info:
                        projects.append(project_info)
                
                current_project = line
                project_text = []
            elif current_project:
                project_text.append(line)
        
        # Process last project
        if current_project and project_text:
            project_info = parse_project_text(current_project, project_text, doc)
            if project_info:
                projects.append(project_info)
    
    return projects

def parse_project_text(project_name, text_lines, doc):
    if len(project_name) < 5:
        return None
    
    full_text = ' '.join(text_lines)
    lower_text = full_text.lower()
    
    # Extract status
    status = None
    if 'completed' in lower_text or 'construction was completed' in lower_text:
        status = 'completed'
    elif 'design' in lower_text or 'working with consultant' in lower_text or 'planning' in lower_text:
        status = 'design'
    elif 'not started' in lower_text or 'identified' in lower_text:
        status = 'not started'
    
    # Extract topic keywords
    topics = []
    if 'park' in lower_text:
        topics.append('park')
    if 'road' in lower_text:
        topics.append('road')
    if 'fema' in lower_text:
        topics.append('FEMA')
    if 'drainage' in lower_text or 'storm drain' in lower_text:
        topics.append('drainage')
    if 'bridge' in lower_text:
        topics.append('bridge')
    if 'playground' in lower_text:
        topics.append('playground')
    if 'fire' in lower_text:
        topics.append('fire')
    if 'warning' in lower_text or 'siren' in lower_text:
        topics.append('emergency warning')
    
    # Extract completion date (et)
    et = None
    
    # Look for completion patterns
    completion_patterns = [
        r'Complete[d]?[\s:]+([A-Za-z\d\-\s,]+?)(?=\.|\n|$)',
        r'Complete Construction[\s:]+([A-Za-z\d\-\s,]+?)(?=\.|\n|$)',
        r'Construction was completed[\s,]*([A-Za-z\d\-\s,]+?)(?=\.|\n|$)'
    ]
    
    for pattern in completion_patterns:
        match = re.search(pattern, ' '.join(text_lines), re.IGNORECASE)
        if match:
            date_str = match.group(1).strip()
            if date_str and len(date_str) < 30:
                et = date_str
                break
    
    return {
        'Project_Name': project_name,
        'topic': ', '.join(topics) if topics else None,
        'status': status,
        'st': None,
        'et': et,
        'source_doc': doc.get('filename')
    }

# Extract projects from civic documents
extracted_projects = extract_projects_from_docs(civic_docs_data)

# Filter for park-related projects completed in 2022
park_projects_2022 = []

for project in extracted_projects:
    # Check if it's park-related
    if project.get('topic') and 'park' in project.get('topic', ''):
        # Check if completed in 2022
        et = project.get('et', '')
        if et and '2022' in str(et):
            park_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps({
    'total_extracted_projects': len(extracted_projects),
    'park_projects_2022': park_projects_2022,
    'count_park_projects_2022': len(park_projects_2022)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json'}

exec(code, env_args)
