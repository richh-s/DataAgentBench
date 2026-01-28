code = """import json

# Read funding data file
funding_path = "var_functions.query_db:0"  # Use path directly
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Read civic docs file  
civic_path = "var_functions.query_db:5"  # Use path directly
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Filter for emergency/FEMA projects
emergency_fema_projects = []
for record in funding_data:
    proj_name = record.get('Project_Name', '').lower()
    if 'emergency' in proj_name or 'fema' in proj_name:
        emergency_fema_projects.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

# Extract status from civic documents
status_dict = {}
for doc in civic_docs:
    text_content = doc.get('text', '')
    lines = [line.strip() for line in text_content.split('\n') if line.strip()]
    
    for idx, line in enumerate(lines):
        # Check if this appears to be a project name
        if (line and 
            not line.startswith('Page') and 
            not line.startswith('Agenda') and 
            not line.startswith('To:') and 
            not line.startswith('From:') and 
            not line.startswith('Subject:') and 
            not line.startswith('Date') and 
            len(line) < 150):
            
            # Look ahead for status indicators
            if idx + 1 < len(lines):
                next_content = ' '.join(lines[idx+1:idx+5]).lower()
                if 'updates' in next_content or 'project schedule' in next_content:
                    status_value = 'Unknown'
                    
                    if 'construction was completed' in text_content.lower():
                        status_value = 'completed'
                    elif 'under construction' in text_content.lower():
                        status_value = 'construction'
                    elif 'design' in text_content.lower():
                        status_value = 'design'
                    elif 'not started' in text_content.lower():
                        status_value = 'not_started'
                    
                    # Store the status
                    if line not in status_dict or status_dict[line] == 'Unknown':
                        status_dict[line] = status_value

# Combine project data with status
output = []
for project in emergency_fema_projects:
    name = project['Project_Name']
    matched_status = 'Unknown'
    
    # Exact match check
    if name in status_dict:
        matched_status = status_dict[name]
    else:
        # Partial match using base name
        base_name = name.split('(')[0].strip()
        for key in status_dict:
            if base_name.lower() in key.lower():
                matched_status = status_dict[key]
                break
    
    output.append({
        'Project_Name': name,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': matched_status
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
