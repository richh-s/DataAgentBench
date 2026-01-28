code = """import json
import os

# Load MongoDB results
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    mongo_docs = json.load(f)

print('Documents loaded:', len(mongo_docs))

# Extract projects
projects = []
for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    section_type = None
    lines = text.split('||n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check section headers
        if 'Design' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'design'
        elif 'Construction' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'construction'
        elif 'Not Started' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'not_started'
        
        # Find project names
        if line and len(line) > 10 and not line.startswith('(') and 'Updates' not in line and 'Schedule' not in line:
            # Check next lines for project indicators
            next_lines = ' '.join(lines[i:i+4])
            if 'Updates' in next_lines or 'Schedule' in next_lines:
                project_name = line
                
                # Check topics
                topics = []
                if 'fema' in project_name.lower() or 'fema' in text.lower():
                    topics.append('FEMA')
                if 'emergency' in project_name.lower() or 'emergency' in text.lower():
                    topics.append('emergency')
                
                project_type = 'disaster' if '(FEMA' in project_name or '(CalOES' in project_name or '(CalJPIA' in project_name else 'capital'
                status = section_type if section_type else 'unknown'
                
                projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'type': project_type,
                    'topics': topics,
                    'filename': filename
                })

print('Total projects extracted:', len(projects))
print('Sample projects:')
for p in projects[:10]:
    print(' -', p['Project_Name'][:60], 'status:', p['status'], 'topics:', p['topics'])

# Filter emergency/FEMA projects
emergency_projects = []
for proj in projects:
    if 'fema' in proj['Project_Name'].lower() or 'emergency' in proj['Project_Name'].lower() or len(proj['topics']) > 0:
        emergency_projects.append(proj)

print('Emergency/FEMA projects found:', len(emergency_projects))

result = {
    'emergency_fema_projects': emergency_projects,
    'total_projects': len(projects)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
