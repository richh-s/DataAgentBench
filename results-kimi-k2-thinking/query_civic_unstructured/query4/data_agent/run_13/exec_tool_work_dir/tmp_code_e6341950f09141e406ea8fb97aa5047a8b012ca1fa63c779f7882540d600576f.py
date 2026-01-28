code = """import json
import re

# Load both datasets
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Function to extract project information from document text
def extract_projects_from_text(text, filename):
    projects = []
    lines = text.split('\n')
    current_project = None
    capturing = False
    
    # Patterns to identify project sections
    project_patterns = [
        r'^[A-Z].+Project\s*$',
        r'^[A-Z].+Improvements\s*$',
        r'^[A-Z].+Repairs\s*$',
        r'^[A-Z].+Study\s*$',
        r'^[A-Z].+Infrastructure\s*$',
        r'^[A-Z].+System\s*$',
        r'^[A-Z].+Structure\s*$',
        r'^[A-Z].+Replacement\s*$',
        r'^[A-Z].+Renovation\s*$',
        r'^[A-Z].+Development\s*$'
    ]
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this is a project title (usually all caps or title case)
        if (line.isupper() and len(line) > 10 and 
            not line.startswith('Page') and 
            not line.startswith('Item') and
            not any(keyword in line for keyword in ['Agenda', 'Public Works', 'Commission', 'Minutes', 'Report'])):
            
            # Save previous project
            if current_project and current_project.get('Project_Name'):
                projects.append(current_project)
            
            # Start new project
            current_project = {
                'Project_Name': line,
                'filename': filename,
                'st': '',
                'et': '',
                'status': '',
                'type': '',
                'topic': ''
            }
            capturing = True
            continue
        
        if current_project and capturing:
            # Extract dates - look for "Complete Design", "Advertise", "Begin Construction", etc.
            if 'Complete Design' in line or 'Advertise' in line or 'Begin Construction' in line or 'Complete Construction' in line:
                # Parse date patterns
                date_patterns = [
                    r'(Spring|Summer|Fall|Winter)\s+(202\d)',
                    r'(202\d)-([A-Z][a-z]+)',
                    r'(202\d)-(Spring|Summer|Fall|Winter)'
                ]
                
                for pattern in date_patterns:
                    matches = re.findall(pattern, line)
                    if matches:
                        if current_project['st'] == '':
                            current_project['st'] = line
                        current_project['et'] = line
                        break
            
            # Extract status based on section headers
            if line.startswith('Capital Improvement Projects (Design)'):
                if current_project:
                    current_project['status'] = 'design'
            elif line.startswith('Capital Improvement Projects (Construction)'):
                if current_project:
                    current_project['status'] = 'construction'
            elif line.startswith('Capital Improvement Projects (Not Started)'):
                if current_project:
                    current_project['status'] = 'not started'
            elif line.startswith('Disaster Recovery Projects'):
                if current_project:
                    current_project['type'] = 'disaster'
            
            # Determine type based on keywords
            if 'FEMA' in line:
                current_project['type'] = 'disaster'
            elif 'CalOES' in line or 'CalJPIA' in line:
                current_project['type'] = 'disaster'
            elif 'Capital' in filename or 'capital' in text.lower():
                current_project['type'] = 'capital'
            
            # Extract topics
            topic_keywords = ['park', 'road', 'FEMA', 'fire', 'emergency', 'drainage', 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 'guardrail', 'stormwater', 'infrastructure']
            for keyword in topic_keywords:
                if keyword.lower() in text.lower() and keyword not in current_project['topic']:
                    current_project['topic'] += keyword + ','
    
    # Add last project
    if current_project and current_project.get('Project_Name'):
        projects.append(current_project)
    
    return projects

# Extract all projects
all_projects = []
for doc in civic_docs_data:
    projects = extract_projects_from_text(doc['text'], doc['filename'])
    all_projects.extend(projects)

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(all_projects),
    'sample_projects': all_projects[:10] if all_projects else []
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
