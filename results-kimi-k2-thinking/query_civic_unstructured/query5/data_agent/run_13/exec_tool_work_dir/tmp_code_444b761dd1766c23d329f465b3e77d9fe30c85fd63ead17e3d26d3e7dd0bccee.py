code = """import json
import re

# Load the civic docs data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for lines that appear to be project names
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and common non-project lines
        if not line or len(line) < 5 or len(line) > 150:
            continue
            
        # Skip lines that are clearly not project names
        skip_patterns = [
            'Page', 'Agenda', 'Public Works', 'Commission',
            'Meeting', 'Item', 'To:', 'Prepared by', 'Approved by',
            'Date prepared', 'Subject', 'RECOMMENDED ACTION',
            'DISCUSSION', 'Updates', 'Schedule', 'Complete',
            'Begin', 'Advertise', 'Project Description', 'cid',
            '•', '-', '(', '1.', '2.', '3.', '4.', '5.', '6.'
        ]
        
        if any(pattern in line for pattern in skip_patterns):
            continue
        
        # Look for project-like names (start with capital letter, contain descriptive words)
        project_indicators = ['Project', 'Improvements', 'Repairs', 'Replacement', 
                             'Drain', 'Road', 'Park', 'Bridge', 'Warning', 'System',
                             'Study', 'Program', 'Structure', 'Facility', 'Phase']
        
        if line[0].isupper() and any(indicator in line for indicator in project_indicators):
            # Check if this looks like a standalone project name
            if not line.endswith('.') or line.endswith('Project'):
                projects.append({
                    'Project_Name': line,
                    'doc_filename': filename
                })

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Look for disaster-related projects starting in 2022
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'warning', 'siren']
projects_2022 = []

for project in projects:
    project_name = project['Project_Name']
    
    # Check if disaster-related
    is_disaster = any(keyword.lower() in project_name.lower() for keyword in disaster_keywords)
    
    if is_disaster:
        projects_2022.append(project_name)

# Also check funding data for disaster projects
funding_disaster_2022 = []
for record in funding_data:
    project_name = record['Project_Name']
    if any(keyword.lower() in project_name.lower() for keyword in disaster_keywords):
        funding_disaster_2022.append(record)

print("__RESULT__:")
print(json.dumps({
    "disaster_projects_found": len(projects_2022),
    "funding_disaster_records": len(funding_disaster_2022),
    "sample_disaster_projects": projects_2022[:15],
    "sample_funding_disaster": funding_disaster_2022[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json'}

exec(code, env_args)
