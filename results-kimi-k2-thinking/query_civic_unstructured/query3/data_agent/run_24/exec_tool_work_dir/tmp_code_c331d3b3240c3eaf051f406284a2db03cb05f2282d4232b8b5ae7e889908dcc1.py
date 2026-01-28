code = """import json
import re

# Read the MongoDB results
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    mongo_docs = json.load(f)

print(f"Found {len(mongo_docs)} documents")
print(f"First doc keys: {list(mongo_docs[0].keys()) if mongo_docs else 'No docs'}")

# Parse each document to extract project information
projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections
    # Pattern to find project names and their details
    lines = text.split('\n')
    
    current_project = None
    in_project_section = False
    
    # Track what section we're in
    section_type = None  # "design", "construction", "not_started"
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check for section headers
        if "Capital Improvement Projects (Design)" in line or "Disaster Recovery Projects (Design)" in line:
            section_type = "design"
            continue
        elif "Capital Improvement Projects (Construction)" in line or "Disaster Recovery Projects (Construction)" in line:
            section_type = "construction"
            continue
        elif "Capital Improvement Projects (Not Started)" in line or "Disaster Recovery Projects (Not Started)" in line:
            section_type = "not_started"
            continue
        
        # Look for project names (they're usually bold or standalone lines)
        # Projects often appear as standalone lines before update/schedule sections
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('■') and \
           not line.startswith('●') and 'Updates:' not in line and 'Schedule:' not in line and \
           'Project Description:' not in line and len(line) > 5 and not line.startswith('Page'):
            
            # Check if next lines contain project indicators
            next_lines = '\n'.join(lines[i+1:i+3]) if i+1 < len(lines) else ''
            
            if 'Updates:' in next_lines or 'Schedule:' in next_lines or 'Project Description:' in next_lines:
                # This is likely a project name
                current_project = {
                    'Project_Name': line,
                    'status': section_type,
                    'filename': filename,
                    'topics': []
                }
                
                # Determine topics based on project name and content
                project_lower = line.lower()
                if 'fema' in project_lower or 'fema' in text.lower():
                    current_project['topics'].append('FEMA')
                if 'emergency' in project_lower or 'emergency' in text.lower():
                    current_project['topics'].append('emergency')
                if 'fire' in project_lower:
                    current_project['topics'].append('fire')
                if 'storm' in project_lower or 'drainage' in project_lower:
                    current_project['topics'].append('drainage')
                if 'warning' in project_lower or 'siren' in project_lower:
                    current_project['topics'].append('emergency warning')
                if 'road' in project_lower:
                    current_project['topics'].append('road')
                if 'park' in project_lower:
                    current_project['topics'].append('park')
                
                # Check for disaster project indicators
                if '(FEMA Project)' in line or '(CalOES Project)' in line or '(CalJPIA Project)' in line:
                    current_project['type'] = 'disaster'
                elif section_type:
                    current_project['type'] = 'capital'
                else:
                    current_project['type'] = 'capital'
                
                projects.append(current_project)

# Filter projects that are related to emergency or FEMA
filtered_projects = []
for proj in projects:
    project_name = proj['Project_Name'].lower()
    text_content = ' '.join([doc.get('text', '').lower() for doc in mongo_docs])
    
    # Check if project is related to emergency or FEMA
    if ('emergency' in project_name or 'fema' in project_name or 
        'fema' in text_content or 'emergency' in text_content):
        filtered_projects.append(proj)

# Remove duplicates based on project name
unique_projects = {}
for proj in filtered_projects:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())

print(f"Extracted {len(projects)} total projects")
print(f"Filtered to {len(filtered_projects)} emergency/FEMA related projects")
print(f"Final unique projects: {len(final_projects)}")

# Print sample projects
for proj in final_projects[:5]:
    print(f"- {proj['Project_Name']}: status={proj['status']}, topics={proj['topics']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
