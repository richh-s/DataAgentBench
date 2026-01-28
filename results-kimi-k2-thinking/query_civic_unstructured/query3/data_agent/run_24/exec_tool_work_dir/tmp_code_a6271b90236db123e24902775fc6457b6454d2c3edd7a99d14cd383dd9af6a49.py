code = """import json
import os

# Load the MongoDB results
file_path = var_functions.query_db:5
print('Loading from file path:', file_path)

with open(file_path, 'r') as f:
    mongo_docs = json.load(f)

print(f'Found {len(mongo_docs)} documents')
print(f'First doc keys: {list(mongo_docs[0].keys()) if mongo_docs else "No docs"}')

# Simple pattern matching to find project names in the text
projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for patterns that indicate projects
    import re
    
    # Common project patterns in these documents
    # Split by section headers
    sections = re.split(r'\n\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\([^)]+\)\s*\n', text)
    
    section_type = None
    
    for i, section in enumerate(sections):
        if 'Design' in section:
            section_type = 'design'
            continue
        elif 'Construction' in section:
            section_type = 'construction'
            continue
        elif 'Not Started' in section:
            section_type = 'not_started'
            continue
        
        # Look for project listings
        if section_type and len(section.strip()) > 50:
            # Find bold/special formatted lines that are likely project names
            section_lines = section.split('\n')
            
            for line in section_lines:
                line = line.strip()
                # Skip empty lines, bullets, common markers
                if (len(line) > 10 and not line.startswith('•') and not line.startswith('■') and 
                    not line.startswith('(') and 'Page' not in line and 'Updates:' not in line and 
                    'Schedule:' not in line and 'Project Description:' not in line):
                    
                    # Check context - next lines should have project info
                    line_idx = section_lines.index(line)
                    next_context = ' '.join(section_lines[line_idx:line_idx+4])
                    
                    if 'Updates:' in next_context or 'Schedule:' in next_context or 'Project Description:' in next_context:
                        # This is likely a project name
                        project_name = line
                        
                        # Determine topics
                        topics = []
                        name_lower = project_name.lower()
                        text_lower = text.lower()
                        
                        if 'fema' in name_lower or 'fema' in text_lower:
                            topics.append('FEMA')
                        if 'emergency' in name_lower or 'emergency' in text_lower:
                            topics.append('emergency')
                        if 'fire' in name_lower:
                            topics.append('fire')
                        if 'storm' in name_lower or 'drainage' in name_lower:
                            topics.append('drainage')
                        if 'warning' in name_lower or 'siren' in name_lower:
                            topics.append('emergency warning')
                        
                        project_type = 'disaster' if '(FEMA' in project_name or '(CalOES' in project_name or '(CalJPIA' in project_name else 'capital'
                        status = section_type if section_type else 'unknown'
                        
                        projects.append({
                            'Project_Name': project_name,
                            'status': status,
                            'type': project_type,
                            'topics': topics,
                            'filename': filename
                        })

print(f'\nExtracted {len(projects)} projects')
print('\nFirst 15 projects:')
for i, p in enumerate(projects[:15]):
    print(f'{i+1}. {p[\"Project_Name\"][:70]} | status: {p[\"status\"]} | type: {p[\"type\"]} | topics: {p[\"topics\"]}')

# Filter for emergency/FEMA related projects
emergency_fema_projects = []
for proj in projects:
    proj_name = proj['Project_Name'].lower()
    if 'fema' in proj_name or 'emergency' in proj_name or len(proj['topics']) > 0:
        emergency_fema_projects.append(proj)

print(f'\nFiltered to {len(emergency_fema_projects)} emergency/FEMA related projects')

# Save for downstream use
result = {
    'all_projects': projects,
    'emergency_fema_projects': emergency_fema_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
