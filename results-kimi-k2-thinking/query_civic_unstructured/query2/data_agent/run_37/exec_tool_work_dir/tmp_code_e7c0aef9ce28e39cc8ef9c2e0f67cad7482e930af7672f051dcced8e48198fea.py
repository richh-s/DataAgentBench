code = """import json
import re
import pandas as pd

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
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and common headers
            if not line:
                if current_project and project_text:
                    # Process the completed project
                    project_info = parse_project_text(current_project, '\n'.join(project_text), doc)
                    if project_info:
                        projects.append(project_info)
                    current_project = None
                    project_text = []
                continue
            
            # Check if this is a project name (usually all caps or title case, not a header)
            if (len(line) > 5 and 
                not line.startswith('Public Works') and 
                not line.startswith('Capital Improvement') and
                not line.startswith('Disaster Recovery') and
                not line.startswith('RECOMMENDED') and
                not line.startswith('DISCUSSION') and
                not line.startswith('Page') and
                not line.startswith('Agenda Item')):
                
                # Check if line looks like a project name (no common action words at start)
                if not any(line.startswith(word) for word in ['To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'Staff', 'City', 'Project']):
                    # This might be a project name
                    if current_project and project_text:
                        project_info = parse_project_text(current_project, '\n'.join(project_text), doc)
                        if project_info:
                            projects.append(project_info)
                    
                    current_project = line
                    project_text = []
                    continue
            
            if current_project:
                project_text.append(line)
        
        # Don't forget the last project
        if current_project and project_text:
            project_info = parse_project_text(current_project, '\n'.join(project_text), doc)
            if project_info:
                projects.append(project_info)
    
    return projects

def parse_project_text(project_name, text, doc):
    if not project_name or len(project_name) < 5:
        return None
    
    # Skip common headers
    skip_patterns = [
        'Capital Improvement Projects',
        'Disaster Recovery Projects',
        'Public Works Commission',
        'RECOMMENDED ACTION',
        'DISCUSSION',
        'To:',
        'Prepared by',
        'Approved by',
        'Date prepared',
        'Meeting date',
        'Subject:'
    ]
    
    if any(pattern in project_name for pattern in skip_patterns):
        return None
    
    lower_text = text.lower()
    
    # Extract status
    status = None
    if 'completed' in lower_text or 'construction was completed' in lower_text:
        status = 'completed'
    elif 'design' in lower_text or 'planning' in lower_text or 'working with consultant' in lower_text:
        status = 'design'
    elif 'not started' in lower_text or 'identified' in lower_text or 'preliminary design' in lower_text:
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
    
    # Extract dates (et = end time/completion date)
    et = None
    
    # Look for completion patterns
    completion_patterns = [
        r'Complete[d]?[\s:]+([A-Za-z\d\-\s,]+?)(?=\n|$)',
        r'Complete Construction[\s:]+([A-Za-z\d\-\s,]+?)(?=\n|$)',
        r'Construction was completed[\s,]*([A-Za-z\d\-\s,]+?)(?=\n|$)'
    ]
    
    for pattern in completion_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            date_str = match.group(1).strip()
            if date_str and len(date_str) < 50:  # Avoid capturing too much text
                et = date_str
                break
    
    return {
        'Project_Name': project_name,
        'topic': ', '.join(topics) if topics else None,
        'status': status,
        'st': None,  # We mainly need et for completion year
        'et': et,
        'source_doc': doc.get('filename')
    }

# Extract projects from civic documents
extracted_projects = extract_projects_from_docs(civic_docs_data)

print('__RESULT__:')
print(json.dumps({
    'extracted_projects_count': len(extracted_projects),
    'sample_projects': extracted_projects[:15]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json'}

exec(code, env_args)
