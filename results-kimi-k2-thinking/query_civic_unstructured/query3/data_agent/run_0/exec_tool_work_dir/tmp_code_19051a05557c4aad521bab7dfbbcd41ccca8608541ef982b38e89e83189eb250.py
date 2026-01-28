code = """import json

# Read the funding data result
temp_funding = var_functions.query_db:0
with open(temp_funding, 'r') as f:
    funding_data = json.load(f)

# Read the civic documents result
temp_civic = var_functions.query_db:5
with open(temp_civic, 'r') as f:
    civic_docs = json.load(f)

# Find projects with 'emergency' or 'fema' in the name
emergency_projects = []
for record in funding_data:
    name = record.get('Project_Name', '').lower()
    if 'fema' in name or 'emergency' in name:
        emergency_projects.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

# Build a map of project statuses from civic documents
status_map = {}
for doc in civic_docs:
    text = doc.get('text', '')
    sections = text.split('\n\n')
    
    for i, section in enumerate(sections):
        lines = [l.strip() for l in section.split('\n') if l.strip()]
        for line in lines:
            if line and not line.startswith('Page') and not line.startswith('Agenda') and len(line) < 100:
                # Check if this looks like a project name
                if i + 1 < len(sections):
                    next_section = sections[i+1].lower()
                    if 'updates' in next_section or 'project schedule' in next_section or 'status' in next_section:
                        # Determine status
                        status = 'Unknown'
                        if 'construction was completed' in next_section:
                            status = 'completed'
                        elif 'under construction' in next_section or 'out to bid' in next_section:
                            status = 'construction'
                        elif 'design' in next_section:
                            status = 'design'
                        elif 'not started' in next_section:
                            status = 'not started'
                        status_map[line] = status

# Combine information
final_results = []
for proj in emergency_projects:
    project_name = proj['Project_Name']
    status = 'Unknown'
    
    # Try exact match
    if project_name in status_map:
        status = status_map[project_name]
    else:
        # Try partial match
        base_name = project_name.split(' (')[0]
        for key in status_map:
            if base_name.lower() in key.lower():
                status = status_map[key]
                break
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
