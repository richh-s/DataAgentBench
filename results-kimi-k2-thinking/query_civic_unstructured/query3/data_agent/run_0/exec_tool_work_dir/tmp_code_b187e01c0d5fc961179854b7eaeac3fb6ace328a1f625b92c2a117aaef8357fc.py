code = """import json

# The previous attempts failed due to syntax errors. Let me try a different approach.
# I'll directly reference the variable names without string concatenation issues.

# Load funding data from the stored variable
funding_result = var_functions.query_db:0
with open(funding_result, 'r') as f:
    funding_records = json.load(f)

# Load civic documents from the stored variable
civic_result = var_functions.query_db:5
with open(civic_result, 'r') as f:
    civic_documents = json.load(f)

# Filter for projects containing 'FEMA' or 'emergency' (case-insensitive)
fema_emergency_projects = []
for record in funding_records:
    project_name_lower = record.get('Project_Name', '').lower()
    if 'fema' in project_name_lower or 'emergency' in project_name_lower:
        fema_emergency_projects.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

# Extract project status information from civic documents
project_status_map = {}

for doc in civic_documents:
    text = doc.get('text', '') or ''
    lines = [line for line in text.split('\n') if line.strip()]
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Skip header/footer lines
        if (not line or line.startswith('Page') or line.startswith('Agenda') or 
            line.startswith('To:') or line.startswith('From:') or line.startswith('Subject:') or 
            line.startswith('Date:') or line.startswith('Prepared by') or 
            'Public Works Commission' in line or len(line) < 5 or len(line) > 150):
            continue
            
        # Check if this looks like a project name (followed by project info)
        next_content = '\n'.join(lines[i:i+8]).lower()
        if 'updates:' in next_content or 'project schedule:' in next_content:
            # Determine status from document context
            status = 'Unknown'
            doc_lower = text.lower()
            if 'construction was completed' in doc_lower:
                status = 'completed'
            elif 'under construction' in doc_lower or 'out to bid' in doc_lower:
                status = 'construction'
            elif 'design' in doc_lower:
                status = 'design'
            elif 'not started' in doc_lower:
                status = 'not_started'
            
            # Store status if not already found or if current status is "Unknown"
            if line not in project_status_map or project_status_map[line] == 'Unknown':
                project_status_map[line] = status

# Match projects with their statuses
final_results = []
for project in fema_emergency_projects:
    project_name = project['Project_Name']
    status = 'Unknown'
    
    # Exact match
    if project_name in project_status_map:
        status = project_status_map[project_name]
    else:
        # Partial match - use base name before any parenthetical
        base_name = project_name.split('(')[0].strip()
        for civic_name, civic_status in project_status_map.items():
            if base_name.lower() in civic_name.lower() or civic_name.lower() in base_name.lower():
                status = civic_status
                break
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
