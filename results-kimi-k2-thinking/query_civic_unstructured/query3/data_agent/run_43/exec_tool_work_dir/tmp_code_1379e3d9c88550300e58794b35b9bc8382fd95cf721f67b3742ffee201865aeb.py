code = """import json
import re
import pandas as pd

# Load MongoDB documents
mongo_file = locals()['var_functions.query_db:0']
with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

# Load funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Convert funding to DataFrame
df_funding = pd.DataFrame(funding_records)
print("Funding data loaded:", df_funding.shape)
print("Columns:", df_funding.columns.tolist())
print("First 3 records:")
for i in range(min(3, len(df_funding))):
    print(str(df_funding.iloc[i].to_dict()))

# Analyze text to extract project information
all_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for project patterns - capital projects and disaster projects
    # Pattern 1: Capital Improvement Projects (Design/Construction/Not Started)
    # Pattern 2: Projects with FEMA in name
    
    # Split text into sections by project names
    lines = text.split('\n')
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        # Detect project names (typically uppercase or title case, sometimes with suffixes)
        if re.match(r'^[A-Z][a-zA-Z\s&\-]+(?:\([^)]*\))?$', line) and len(line) > 10:
            # This is likely a project name
            project = {
                'Project_Name': line,
                'topic': '',
                'type': '',
                'status': '',
                'st': '',
                'et': ''
            }
            
            # Determine type based on context or name
            if '(FEMA' in line or 'FEMA' in line:
                project['type'] = 'disaster'
                project['topic'] = 'FEMA'
            elif 'emergency' in text.lower():
                project['type'] = 'disaster'
                project['topic'] = 'emergency'
            else:
                project['type'] = 'capital'
                # Infer topic from name
                if 'storm' in line.lower() or 'drain' in line.lower():
                    project['topic'] = 'storm drain'
                elif 'road' in line.lower():
                    project['topic'] = 'road'
                elif 'warning' in line.lower():
                    project['topic'] = 'emergency warning'
                elif 'bridge' in line.lower():
                    project['topic'] = 'bridge'
                elif 'park' in line.lower():
                    project['topic'] = 'park'
            
            # Check for status in surrounding text
            if 'construction was completed' in text.lower() or 'completed' in line.lower():
                project['status'] = 'completed'
            elif 'design' in line.lower() or 'under design' in text.lower():
                project['status'] = 'design'
            elif 'not started' in text.lower():
                project['status'] = 'not started'
            
            # Check for dates in format like "2023-Spring", "2023-Fall", etc.
            date_patterns = [r'20\d{2}-Spring', r'20\d{2}-Summer', r'20\d{2}-Fall', r'20\d{2}-Winter', r'20\d{2}-\d{2}']
            for pattern in date_patterns:
                matches = re.findall(pattern, text)
                if matches:
                    project['st'] = matches[0] if len(matches) > 0 else ''
                    project['et'] = matches[1] if len(matches) > 1 else ''
                    break
            
            all_projects.append(project)

print("Extracted", len(all_projects), "projects")
print("Sample projects:")
for i in range(min(5, len(all_projects))):
    print(str(all_projects[i]))

# Now find projects specifically related to 'emergency' or 'FEMA'
emergency_fema_projects = []
for proj in all_projects:
    text_lower = proj['Project_Name'].lower()
    if 'emergency' in text_lower or 'fema' in text_lower:
        emergency_fema_projects.append(proj)

print("\nFound", len(emergency_fema_projects), "projects related to emergency/FEMA:")
for proj in emergency_fema_projects:
    print(str(proj))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
