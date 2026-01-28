code = """import json
import re

# Read the civic documents
civic_docs_file = '../var_functions.query_db:8'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
funding_file = '../var_functions.query_db:10'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Function to extract projects from text
def extract_projects(text):
    projects = []
    
    # Look for project patterns like "Project Name\n\n(•) Updates:" or similar structures
    # This is a simplified pattern - documents seem to have project names followed by bullet points
    
    # Pattern 1: Project name on its own line, followed by updates/status
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and obvious headers
        if not line or line.startswith('---') or 'Agenda Item' in line or 'Page ' in line:
            continue
            
        # Look for project names (typically not bullet points and have proper capitalization)
        # and followed by update markers
        if (i < len(lines) - 1 and 
            'Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1] or 'Project Description:' in line):
            
            # This is likely a project name
            project_name = line
            
            # Look ahead for status and dates
            status = None
            completion_date = None
            topics = []
            
            # Search next few lines for details
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                
                # Look for completion info
                if 'Complete Construction:' in next_line or 'Construction was completed' in next_line:
                    # Extract date info
                    date_match = re.search(r'(\b\w+\s+\d+\s*,?\s*\d{4}\b|\b\d{4}-\w+\b|\b\w+\s+\d{4}\b)', next_line)
                    if date_match:
                        completion_date = date_match.group(1)
                        status = 'completed'
                
                # Look for status indicators
                if 'Project is currently under construction' in next_line:
                    status = 'construction'
                elif 'Complete Design:' in next_line:
                    status = 'design'
                elif 'Not Started' in next_line:
                    status = 'not started'
            
            # Determine topics based on project name
            project_lower = project_name.lower()
            if 'park' in project_lower:
                topics.append('park')
            if 'road' in project_lower or 'street' in project_lower:
                topics.append('road')
            if 'drain' in project_lower:
                topics.append('drainage')
            if 'fema' in project_lower:
                topics.append('FEMA')
            
            if status == 'completed' and topics:
                projects.append({
                    'Project_Name': project_name,
                    'topics': ','.join(topics),
                    'status': status,
                    'completion_date': completion_date,
                    'et': completion_date
                })
    
    return projects

# Extract all projects from documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects(doc['text'])
    all_projects.extend(projects)

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for project in all_projects:
    if ('park' in project['topics'] and 
        project['status'] == 'completed' and 
        project['et'] and 
        '2022' in project['et']):
        park_projects_2022.append(project)

print("__RESULT__:")
print(json.dumps(park_projects_2022))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
