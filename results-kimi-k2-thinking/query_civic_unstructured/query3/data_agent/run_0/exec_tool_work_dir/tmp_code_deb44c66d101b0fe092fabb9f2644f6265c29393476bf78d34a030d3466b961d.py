code = """import json

# Read the funding data and civic documents from the stored variables
funding_result = var_functions.query_db:0
civic_result = var_functions.query_db:5

# Since these are file paths, we need to read them
with open(funding_result, 'r') as f:
    funding_data = json.load(f)

with open(civic_result, 'r') as f:
    civic_docs = json.load(f)

# Filter funding data for projects containing 'emergency' or 'FEMA'
filtered_funding = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    if 'emergency' in project_name or 'fema' in project_name:
        filtered_funding.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

# Extract project information from civic documents
project_status_map = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for project names (based on typical patterns)
        if line and not line.startswith('(') and not line.startswith('Page') and not line.startswith('Agenda') and len(line) < 100:
            # Check for indicators that this is a project name
            next_section = '\n'.join(lines[i+1:i+5]).lower()
            if 'updates' in next_section or 'project schedule' in next_section or 'status' in next_section:
                project_name = line
                
                # Determine status from following text
                status = 'Unknown'
                look_ahead = '\n'.join(lines[i+1:i+10]).lower()
                
                if 'construction was completed' in look_ahead:
                    status = 'completed'
                elif 'under construction' in look_ahead or 'out to bid' in look_ahead:
                    status = 'construction'
                elif 'design' in look_ahead or 'finalize' in look_ahead:
                    status = 'design'
                elif 'not started' in look_ahead:
                    status = 'not started'
                    
                project_status_map[project_name] = status

# Combine funding data with status information
result = []
for funding_project in filtered_funding:
    project_name = funding_project['Project_Name']
    status = 'Unknown'
    
    # Try exact match first
    if project_name in project_status_map:
        status = project_status_map[project_name]
    else:
        # Try partial matching (base name without suffix)
        base_name = project_name.split(' (')[0].strip()
        for civic_project, civic_status in project_status_map.items():
            if base_name.lower() in civic_project.lower() or civic_project.lower() in base_name.lower():
                status = civic_status
                break
    
    result.append({
        'Project_Name': project_name,
        'Funding_Source': funding_project['Funding_Source'],
        'Amount': funding_project['Amount'],
        'Status': status
    })

# Return results
print("__RESULT__:")
print(json.dumps(result, indent=2, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
