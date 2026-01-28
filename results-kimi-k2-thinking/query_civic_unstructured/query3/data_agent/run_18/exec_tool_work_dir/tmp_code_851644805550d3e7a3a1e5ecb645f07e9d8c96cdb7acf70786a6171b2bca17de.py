code = """import json
import re

# Get the civic documents from the stored variable
civic_docs = locals()['var_functions.query_db:0']

# Get funding data
funding_data = locals()['var_functions.query_db:2']

print(f"Civic docs type: {type(civic_docs)}, length: {len(civic_docs)}")
print(f"Funding data type: {type(funding_data)}, length: {len(funding_data)}")

# First, let's extract all project information from civic docs
all_projects = []

# Process each document
for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Look for project patterns in the text
    # Common patterns: Project names in bold or with specific formatting
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project name indicators
        # Pattern 1: Lines ending with project indicators
        if line and (line.endswith('Project') or 
                    line.endswith('Improvements') or 
                    line.endswith('Repairs') or
                    line.endswith('Facilit') or
                    '(FEMA' in line or
                    '(CalOES' in line or
                    '(CalJPIA' in line):
            
            # This might be a project name
            if len(line) > 10 and not line.startswith('(') and not 'Recommended' in line:
                # Check if next lines contain status info
                if i+1 < len(lines):
                    next_line = lines[i+1].strip()
                    
                    # Extract project info
                    proj_name = line.strip()
                    
                    # Determine status based on text patterns
                    status = 'not started'
                    if 'construction' in text.lower() and proj_name.lower() in text.lower():
                        if 'under construction' in text.lower() or 'construction was completed' in text.lower():
                            status = 'completed'
                        elif 'design' in text.lower():
                            status = 'design'
                    
                    # Determine if it's emergency/FEMA related
                    is_emergency = False
                    if 'fema' in proj_name.lower() or 'emergency' in proj_name.lower():
                        is_emergency = True
                    elif 'warning' in proj_name.lower() or 'siren' in proj_name.lower():
                        is_emergency = True
                    
                    if is_emergency:
                        project_info = {
                            'Project_Name': proj_name,
                            'Status': status,
                            'Document': filename
                        }
                        all_projects.append(project_info)

# Filter emergency/FEMA projects from funding data
emergency_funding = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    if 'emergency' in project_name or 'fema' in project_name:
        emergency_funding.append(record)

print(f"Found {len(all_projects)} emergency projects in civic docs")
print(f"Found {len(emergency_funding)} emergency projects in funding data")

# Combine the data
print("\nEmergency projects from civic docs:")
for proj in all_projects:
    print(json.dumps(proj, indent=2))

print("\nEmergency projects from funding data:")
for proj in emergency_funding:
    print(json.dumps(proj, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
