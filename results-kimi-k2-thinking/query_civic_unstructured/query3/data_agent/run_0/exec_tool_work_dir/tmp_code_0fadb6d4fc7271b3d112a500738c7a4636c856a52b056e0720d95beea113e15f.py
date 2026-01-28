code = """import json

# Access the stored results using locals()
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:5']

# Read funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic documents
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Filter for projects containing 'FEMA' or 'emergency'
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
project_status_map = {}

for document in civic_docs:
    text = document.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 5 or len(line) > 100:
            continue
            
        # Skip header/footer lines
        if (line.startswith('Page') or line.startswith('Agenda') or 
            'To:' in line or 'From:' in line or 'Subject:' in line or
            'Date' in line or 'Prepared by' in line or 'Approved by' in line):
            continue
        
        # Check if followed by project details
        if i + 3 < len(lines):
            next_text = ' '.join(lines[i+1:i+5]).lower()
            if 'updates' in next_text or 'project schedule' in next_text:
                # Determine status
                doc_lower = text.lower()
                status = 'Unknown'
                if 'construction was completed' in doc_lower:
                    status = 'completed'
                elif 'under construction' in doc_lower or 'out to bid' in doc_lower:
                    status = 'construction'
                elif 'design' in doc_lower:
                    status = 'design'
                elif 'not started' in doc_lower:
                    status = 'not_started'
                
                project_status_map[line] = status

# Match projects with their statuses
results = []
for project in fema_emergency_projects:
    project_name = project['Project_Name']
    status = 'Unknown'
    
    # Try exact match
    if project_name in project_status_map:
        status = project_status_map[project_name]
    else:
        # Partial match using base name
        base_name = project_name.split('(')[0].strip()
        for civic_name, civic_status in project_status_map.items():
            if base_name.lower() in civic_name.lower() or civic_name.lower() in base_name.lower():
                status = civic_status
                break
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
