code = """import json

# Read funding data from the stored result
funding_data = []
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Read civic documents from the stored result
civic_docs = []
with open('var_functions.query_db:5', 'r') as f:
    civic_docs = json.load(f)

# Find projects with 'FEMA' or 'emergency' in their names
fema_emergency_projects = []
for record in funding_data:
    project_name_lower = str(record.get('Project_Name', '')).lower()
    if 'fema' in project_name_lower or 'emergency' in project_name_lower:
        fema_emergency_projects.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

# Extract project status information from civic documents
status_lookup = {}
for document in civic_docs:
    text = document.get('text', '')
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    for i in range(len(lines)):
        line = lines[i]
        # Skip non-project lines
        if (not line or line.startswith('Page') or line.startswith('Agenda') 
            or 'To:' in line or 'From:' in line or 'Subject:' in line
            or len(line) < 5 or len(line) > 100):
            continue
        
        # Check if followed by project information
        if i + 3 < len(lines):
            next_lines = ' '.join(lines[i+1:i+4])
            if 'updates' in next_lines.lower() or 'project schedule' in next_lines.lower():
                # Determine status
                doc_lower = text.lower()
                if 'construction was completed' in doc_lower:
                    status = 'completed'
                elif 'under construction' in doc_lower or 'out to bid' in doc_lower:
                    status = 'construction'
                elif 'design' in doc_lower:
                    status = 'design'
                elif 'not started' in doc_lower:
                    status = 'not_started'
                else:
                    status = 'Unknown'
                
                status_lookup[line] = status

# Match projects with statuses
output = []
for project in fema_emergency_projects:
    project_name = project['Project_Name']
    project_status = 'Unknown'
    
    # Try exact match
    if project_name in status_lookup:
        project_status = status_lookup[project_name]
    else:
        # Try partial match (base name without parenthetical)
        base_name = project_name.split('(')[0].strip()
        for civic_name, civic_status in status_lookup.items():
            if base_name.lower() in civic_name.lower():
                project_status = civic_status
                break
    
    output.append({
        'Project_Name': project_name,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': project_status
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
