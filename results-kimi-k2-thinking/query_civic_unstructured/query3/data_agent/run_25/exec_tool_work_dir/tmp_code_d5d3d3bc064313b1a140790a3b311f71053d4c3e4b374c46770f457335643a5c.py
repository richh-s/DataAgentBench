code = """import json
import re
from collections import defaultdict

# Read the civic documents
with open('var_functions.query_db:0', 'r') as f:
    civic_docs = json.load(f)

# Function to extract project information from text
def extract_projects_from_text(text):
    projects = []
    
    # Look for project patterns in the text
    # Common patterns for project names in these documents
    patterns = [
        r'([A-Z][a-zA-Z\s&\-]+?(?:Project|Improvements|Repairs|Facility|Park|Road|Structure|System|Phase\s+\d+))\s*\n',  # General project pattern
        r'([A-Z][a-zA-Z\s&\-\(\)]+?(?:\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\)))',  # Disaster projects with suffix
    ]
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line looks like a project name
        if (line.isupper() and len(line) > 10 and 'PROJECT' in line) or \
           ('Project' in line and len(line) < 100) or \
           ('Improvements' in line and len(line) < 100) or \
           ('Repairs' in line and len(line) < 100) or \
           ('(FEMA' in line) or \
           ('(CalJPIA' in line) or \
           ('(CalOES' in line):
            
            # Check if the line has emergency/fema relevance
            if re.search(r'emergency|fema|FEMA|Emergency', text, re.IGNORECASE):
                # Look for project details in nearby lines
                project_info = {
                    'Project_Name': line,
                    'topic': '',
                    'type': '',
                    'status': '',
                    'st': '',
                    'et': ''
                }
                
                # Determine type based on content
                if '(FEMA' in line or '(CalJPIA' in line or '(CalOES' in line or 'Disaster' in line:
                    project_info['type'] = 'disaster'
                elif 'Capital' in line or 'Improvement' in line or 'Infrastructure' in line:
                    project_info['type'] = 'capital'
                
                # Look for status in the next few lines
                next_lines = '\n'.join(lines[i:i+20])
                if 'design' in next_lines.lower() or 'Design' in next_lines:
                    project_info['status'] = 'design'
                elif 'complete' in next_lines.lower() or 'Complete' in next_lines:
                    project_info['status'] = 'completed'
                elif 'not started' in next_lines.lower() or 'Not Started' in next_lines:
                    project_info['status'] = 'not started'
                elif 'construction' in next_lines.lower() or 'Construction' in next_lines:
                    project_info['status'] = 'construction'
                
                # Look for dates
                date_patterns = [
                    r'(\d{4}-(?:Spring|Summer|Fall|Winter))',
                    r'(\d{4}-(?:January|February|March|April|May|June|July|August|September|October|November|December))',
                    r'(\d{4}-\d{1,2})',
                ]
                
                for date_pattern in date_patterns:
                    matches = re.findall(date_pattern, next_lines)
                    if matches:
                        if not project_info['st']:
                            project_info['st'] = matches[0]
                        if len(matches) > 1 and not project_info['et']:
                            project_info['et'] = matches[1]
                
                # Determine topic based on keywords
                topics = []
                if 'emergency' in line.lower() or 'emergency' in next_lines.lower():
                    topics.append('emergency')
                if 'fema' in line.lower() or 'FEMA' in next_lines:
                    topics.append('FEMA')
                if 'fire' in line.lower() or 'Fire' in next_lines:
                    topics.append('fire')
                if 'warning' in line.lower() or 'Warning' in next_lines:
                    topics.append('emergency warning')
                    
                project_info['topic'] = ', '.join(topics) if topics else 'emergency'
                
                projects.append(project_info)
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc.get('text', ''))
    if projects:
        all_projects.extend(projects)

# Filter for projects that have emergency or FEMA in topic
emergency_fema_projects = []
for project in all_projects:
    if project['topic'] and ('emergency' in project['topic'].lower() or 'fema' in project['topic'].lower()):
        emergency_fema_projects.append(project)

# Print the extracted projects
result = json.dumps(emergency_fema_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
