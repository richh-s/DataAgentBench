code = """import json
import re

# Load civic documents
with open('/tmp/tmp_d5q7p7j.json', 'r') as f:
    documents = json.load(f)

print('Loaded', len(documents), 'documents')

# Extract projects with Spring 2022 start dates
spring_2022_projects = []

for doc in documents:
    text = doc['text']
    filename = doc['filename']
    
    # Look for project sections and date information
    # Split into lines for better parsing
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check if this might be a project name (capitalize first letter, not too long, not a common header)
        if (len(line) < 150 and 
            not any(keyword in line.lower() for keyword in ['update', 'schedule', 'status', 'discussion:', 'recommended action:', 'subject:']) and
            not line.startswith('(') and 
            not line.startswith('•') and
            not line.startswith('-') and
            line[0].isupper()):
            
            # This could be a project name
            current_project = line
            
        # Look for Spring 2022 dates
        if current_project and any(pattern in line for pattern in ['Spring 2022', '2022-Spring', 'Spring 2022']):
            # Check if this is a start date
            if any(keyword in line.lower() for keyword in ['begin', 'start', 'advertise', 'complete design']):
                spring_2022_projects.append({
                    'project_name': current_project,
                    'context': line,
                    'filename': filename
                })
                print(f'Found: {current_project} - {line}')

print('\nTotal Spring 2022 projects found:', len(spring_2022_projects))

# Get unique project names
unique_projects = {}
for p in spring_2022_projects:
    name = p['project_name']
    if name not in unique_projects:
        unique_projects[name] = p

print('Unique projects:', len(unique_projects))

result = {
    'count': len(unique_projects),
    'projects': list(unique_projects.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
