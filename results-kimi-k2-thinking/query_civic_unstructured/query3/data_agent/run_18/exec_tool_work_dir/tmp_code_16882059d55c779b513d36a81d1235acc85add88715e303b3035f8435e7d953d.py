code = """import json

# Access stored data
funding_records = locals()['var_functions.query_db:2']
civic_documents = locals()['var_functions.query_db:0']

# Initialize results storage
emergency_projects = []

# Step 1: Filter funding records for emergency/FEMA projects
print('Scanning funding records...')
for record in funding_records:
    proj_name = record.get('Project_Name', '').lower()
    if 'emergency' in proj_name or 'fema' in proj_name:
        emergency_projects.append({
            'Project_Name': record['Project_Name'],
            'Funding_Source': record['Funding_Source'],
            'Amount': record['Amount'],
            'Status': 'Unknown',  # Will extract from civic docs
            'Type': 'Unknown'
        })

print('Found', len(emergency_projects), 'emergency/FEMA projects in funding data')

# Step 2: Extract project details from civic documents
project_details = {}

for doc in civic_documents:
    text = doc.get('text', '').lower()
    lines = doc.get('text', '').split('\n')
    
    # Look for project names and status information
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if line looks like a project name
        project_indicators = ['Project', 'Improvements', 'Repairs', 'System', 'Facility', 'Study', 'Replacement']
        if any(indicator in line for indicator in project_indicators) and len(line) > 10:
            
            # Normalize project name for matching
            proj_name_normalized = line.strip()
            proj_name_lower = proj_name_normalized.lower()
            
            # Check if emergency/FEMA related
            if 'emergency' in proj_name_lower or 'fema' in proj_name_lower or 'warning' in proj_name_lower or 'siren' in proj_name_lower:
                
                # Determine status
                status = 'not started'
                if 'under construction' in text or 'construction was completed' in text:
                    if proj_name_lower in text:
                        status = 'completed'
                elif 'design' in text and 'complete design' not in text:
                    if proj_name_lower in text:
                        status = 'design'
                        
                # Determine type
                proj_type = 'disaster' if 'fema' in proj_name_lower else 'capital'
                
                project_details[proj_name_normalized] = {
                    'Status': status,
                    'Type': proj_type
                }

# Step 3: Merge funding data with project details
merged_results = []
for project in emergency_projects:
    proj_name = project['Project_Name']
    details = project_details.get(proj_name, {})
    
    merged_results.append({
        'Project_Name': proj_name,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': details.get('Status', 'Unknown'),
        'Type': details.get('Type', 'disaster' if 'fema' in proj_name.lower() else 'capital')
    })

print('\nFinal results:')
for result in merged_results:
    print(json.dumps(result))
    
print('\nTotal results:', len(merged_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
