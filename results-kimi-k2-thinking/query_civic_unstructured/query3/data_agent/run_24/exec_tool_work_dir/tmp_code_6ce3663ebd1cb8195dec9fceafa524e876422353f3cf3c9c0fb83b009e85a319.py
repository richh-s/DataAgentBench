code = """import json

# Get the file path from storage
file_path = locals()['var_functions.query_db:5']
print('Loading from:', file_path)

# Read the MongoDB documents
with open(file_path, 'r') as f:
    mongo_docs = json.load(f)

print('Documents loaded:', len(mongo_docs))

# Extract project information
projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    section_type = None
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        if 'Design' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'design'
        elif 'Construction' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'construction'
        elif 'Not Started' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'not_started'
        
        # Look for project names (simple heuristic)
        if len(line) > 10 and not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line:
            # Check if next lines contain project info
            next_lines = ' '.join(lines[i+1:i+4])
            if 'Updates:' in next_lines or 'Schedule:' in next_lines:
                project_name = line
                
                # Check for topics
                topics = []
                lower_name = project_name.lower()
                lower_text = text.lower()
                
                if 'fema' in lower_name or 'fema' in lower_text:
                    topics.append('FEMA')
                if 'emergency' in lower_name or 'emergency' in lower_text:
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

print('Extracted', len(projects), 'projects')

# Filter for emergency/FEMA
emergency_fema = []
for proj in projects:
    lower_name = proj['Project_Name'].lower()
    if 'fema' in lower_name or 'emergency' in lower_name or 'FEMA' in proj['topics'] or 'emergency' in proj['topics']:
        emergency_fema.append(proj)

print('Emergency/FEMA projects:', len(emergency_fema))

result = {
    'emergency_fema_projects': emergency_fema,
    'total_extracted': len(projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
