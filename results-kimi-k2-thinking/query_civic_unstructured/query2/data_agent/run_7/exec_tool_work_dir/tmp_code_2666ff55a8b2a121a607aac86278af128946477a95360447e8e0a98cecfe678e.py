code = """import json
import re

# Read the park-related civic documents
with open('var_functions.query_db:16', 'r') as f:
    civic_docs = json.load(f)

# Function to extract project information from text
def extract_park_projects(text):
    projects = []
    lines = text.split('\n')
    
    current_project = None
    project_status = None
    completion_date = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or line.startswith('Page') or line.startswith('Agenda Item'):
            continue
            
        # Look for project names containing "park" (case insensitive)
        if re.search(r'park', line, re.IGNORECASE) and len(line) < 150:
            # Check if it's likely a project name (not a sentence, not a heading)
            if not line.endswith('.') and not line.startswith('Capital') and not line.startswith('To:') \
               and not line.startswith('Subject:') and not line.startswith('Public Works'):
                # If we were building a previous project, save it
                if current_project and project_status and '2022' in str(completion_date):
                    projects.append({
                        'project_name': current_project,
                        'status': project_status,
                        'completion_date': completion_date
                    })
                
                # Start new project
                current_project = line.strip()
                project_status = None
                completion_date = None
                continue
        
        # Look for completion indicators
        if current_project:
            lower_line = line.lower()
            
            # Check for completion status
            if 'completed' in lower_line or 'completion' in lower_line or 'complete construction' in lower_line:
                # Extract date information
                if '2022' in line:
                    project_status = 'completed'
                    # Extract the date/period
                    date_match = re.search(r'([A-Za-z]+\s+)?2022|2022[A-Za-z\s]+', line)
                    if date_match:
                        completion_date = date_match.group()
                elif '2023' in line and ('completed' in lower_line or 'completion' in lower_line):
                    project_status = 'completed'
                    completion_date = '2023'
            
            # Check for specific completion patterns
            if 'complete construction:' in lower_line or 'construction was completed' in lower_line:
                if '2022' in line:
                    project_status = 'completed'
                    date_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', line, re.IGNORECASE)
                    if date_match:
                        completion_date = date_match.group()
    
    # Add the last project if valid
    if current_project and project_status and completion_date and '2022' in completion_date:
        projects.append({
            'project_name': current_project,
            'status': project_status,
            'completion_date': completion_date
        })
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_park_projects(doc['text'])
    all_projects.extend(projects)

# Remove duplicates and clean up
unique_projects = []
seen_names = set()
for proj in all_projects:
    # Clean up project name
    clean_name = proj['project_name'].strip()
    if clean_name not in seen_names:
        seen_names.add(clean_name)
        unique_projects.append({
            'project_name': clean_name,
            'status': proj['status'],
            'completion_date': proj['completion_date']
        })

result = {
    'park_projects_2022': unique_projects,
    'count': len(unique_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:14': {'civic_docs_count': 0, 'funding_records_count': 0, 'status': 'files_accessed'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
