code = """import json
import re

# Read the civic documents file
civic_docs_path = var_functions.query_db:6
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data file
funding_path = var_functions.query_db:7
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

projects_info = []

# Extract project information from civic documents
doc = civic_docs[0]
text = doc.get('text', '')

# Look for FEMA and emergency related projects
fema_emergency_projects = []

# Find project sections that mention FEMA or emergency
lines = text.split('\n')
current_project = None
project_text = ''

for line in lines:
    line = line.strip()
    # Detect project name lines (often start with capital letters, don't start with bullet points)
    if line and not line.startswith('(cid:') and not line.startswith('•') and not line.startswith('-') and not line.startswith('(') and len(line) < 100:
        # Check if next line contains updates or schedule
        if 'Updates:' in text or 'Project Schedule:' in text or 'Updates\n' in text:
            if project_text and ('FEMA' in project_text or 'emergency' in project_text.lower()):
                fema_emergency_projects.append({
                    'project_name': current_project,
                    'text': project_text
                })
            current_project = line
            project_text = line + '\n'
        else:
            if current_project:
                project_text += line + '\n'
    else:
        if current_project:
            project_text += line + '\n'

# Add the last project
if project_text and ('FEMA' in project_text or 'emergency' in project_text.lower()):
    fema_emergency_projects.append({
        'project_name': current_project,
        'text': project_text
    })

# Parse projects to extract structured info
for proj in fema_emergency_projects:
    project_name = proj['project_name']
    project_text = proj['text']
    
    # Extract status
    status = 'unknown'
    if 'construction' in project_text.lower() and 'completed' not in project_text.lower():
        if 'currently under construction' in project_text.lower():
            status = 'construction'
    elif 'completed' in project_text.lower():
        status = 'completed'
    elif 'design' in project_text.lower() or 'awaiting' in project_text.lower() or 'pending' in project_text.lower():
        status = 'design'
    
    # Determine type
    project_type = 'disaster' if 'FEMA' in project_text or 'disaster' in project_text.lower() else 'capital'
    
    projects_info.append({
        'Project_Name': project_name,
        'status': status,
        'type': project_type
    })

# Filter funding data for FEMA/emergency related projects
filtered_funding = []
for fund in funding_data:
    project_name = fund.get('Project_Name', '')
    if 'FEMA' in project_name or 'emergency' in project_name.lower():
        filtered_funding.append({
            'Project_Name': project_name,
            'Funding_Source': fund.get('Funding_Source', ''),
            'Amount': fund.get('Amount', 0)
        })

# Combine results
result = {
    'projects_with_status': projects_info,
    'funding_records': filtered_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
