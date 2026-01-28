code = """import json
import re
from datetime import datetime

# Read the full result from the JSON file
with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

# Function to extract project information from text
def extract_projects(text):
    projects = []
    
    # Look for sections related to projects
    # Pattern for project names: usually they're on separate lines
    # Look for "completed" projects in 2022
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names (typically title case lines that are not part of headings)
        # Common patterns for project names
        project_patterns = [
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+(?:Park|Project|Road|Improvements|Repairs|Facility|Structure|Study))\b',
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+Park\b)',
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+Road\b)',
        ]
        
        is_project_name = False
        for pattern in project_patterns:
            if re.match(pattern, line):
                # Check if this line likely contains status information
                if not any(keyword in line.lower() for keyword in ['updates:', 'updates', 'schedule:', 'description:', 'project description:']):
                    current_project = line
                    is_project_name = True
                    break
        
        # If we have a current project, look for status and dates
        if current_project:
            # Look for completion information in this line or next few lines
            completion_patterns = [
                r'completed[\s,]*(\w+\s+2022)',
                r'completion[\s,]*(\w+\s+2022)',
                r'Complete[\s,]*(\w+\s+2022)',
                r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+2022'
            ]
            
            # Check current line
            for pattern in completion_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    # Determine project type and topic
                    topics = []
                    project_type = "unknown"
                    
                    # Check for park-related keywords
                    if any(keyword in current_project.lower() for keyword in ['park', 'playground', 'walkway']):
                        topics.append('park')
                    if 'storm' in current_project.lower() or 'drain' in current_project.lower():
                        topics.append('drainage')
                    if 'road' in current_project.lower():
                        topics.append('road')
                    if 'water' in current_project.lower():
                        topics.append('water treatment')
                    
                    # Check for type
                    if 'Capital' in text:
                        project_type = 'capital'
                    elif 'Disaster' in text or 'FEMA' in current_project:
                        project_type = 'disaster'
                    
                    projects.append({
                        'Project_Name': current_project,
                        'topic': ', '.join(topics) if topics else 'unknown',
                        'status': 'completed',
                        'type': project_type,
                        'st': '2022',
                        'et': '2022',
                        'completion_date': match.group(1) if match.groups() else '2022'
                    })
                    current_project = None
                    break
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects(doc['text'])
    all_projects.extend(projects)

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(all_projects),
    'park_projects_2022': [p for p in all_projects if 'park' in p['topic'] and '2022' in p['et']]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:8': {'path': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'Loaded 5 documents'}

exec(code, env_args)
