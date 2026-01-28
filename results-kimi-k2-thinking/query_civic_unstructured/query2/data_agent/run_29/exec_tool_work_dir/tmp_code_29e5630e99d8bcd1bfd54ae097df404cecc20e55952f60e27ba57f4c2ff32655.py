code = """import json
import re

# Read the civic documents from the file
civic_docs_file = '/tmp/tmpz5hptp8z.json'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Function to extract project information from text
def extract_projects_from_text(text):
    projects = []
    
    # Split text into sections that look like project descriptions
    # Look for patterns like project names followed by updates
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Look for project names (typically bold or title-like)
        # Pattern: project name followed by updates or status
        if line and not line.startswith('(') and not line.startswith('-') and \
           len(line) > 10 and not any(marker in line.lower() for marker in ['page', 'agenda', 'item', 'subject:', 'recommended action:', 'discussion:']):
            # This might be a project name
            candidate = line.strip()
            # Check if next few lines contain project info
            if any(keyword in candidate.lower() for keyword in ['project', 'repairs', 'improvements', 'structure', 'drainage', 'road']):
                if current_project:
                    projects.append(project_info)
                current_project = candidate
                project_info = {'Project_Name': candidate, 'status': '', 'et': '', 'topic': ''}
        
        # Look for status and completion information
        if current_project:
            lower_line = line.lower()
            if 'completed' in lower_line or 'complete construction' in lower_line:
                project_info['status'] = 'completed'
                # Extract date
                date_match = re.search(r'(\b\w+\s+202[0-9]\b|\b202[0-9]-\w+\b|\b202[0-9]\b)', line)
                if date_match:
                    project_info['et'] = date_match.group(1)
            elif 'construction was completed' in lower_line:
                project_info['status'] = 'completed'
                date_match = re.search(r'(\b\w+\s+202[0-9]\b|\b202[0-9]-\w+\b|\b202[0-9]\b)', line)
                if date_match:
                    project_info['et'] = date_match.group(1)
            elif 'complete construction:' in lower_line:
                project_info['status'] = 'completed'
                date_match = re.search(r'(\b\w+\s+202[0-9]\b|\b202[0-9]-\w+\b|\b202[0-9]\b)', line)
                if date_match:
                    project_info['et'] = date_match.group(1)
        
        # Determine topic based on keywords
        if current_project:
            project_lower = current_project.lower()
            topics = []
            if 'park' in project_lower:
                topics.append('park')
            if 'road' in project_lower:
                topics.append('road')
            if 'drain' in project_lower or 'storm' in project_lower:
                topics.append('drainage')
            if 'fema' in project_lower:
                topics.append('FEMA')
            if 'bridge' in project_lower:
                topics.append('bridge')
            if 'playground' in project_lower:
                topics.append('playground')
            
            project_info['topic'] = ', '.join(topics)
    
    if current_project:
        projects.append(project_info)
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc.get('text', ''))
    all_projects.extend(projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for project in all_projects:
    if 'park' in project.get('topic', '').lower() and project.get('status') == 'completed':
        et = project.get('et', '')
        if '2022' in et:
            park_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': park_projects_2022,
    'count': len(park_projects_2022)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
