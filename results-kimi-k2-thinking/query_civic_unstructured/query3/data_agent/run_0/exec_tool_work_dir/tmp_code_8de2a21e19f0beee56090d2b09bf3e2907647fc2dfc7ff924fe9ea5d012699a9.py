code = """import json

# Get the file paths from the variables
funding_file_path = "var_functions.query_db:0"
civic_file_path = "var_functions.query_db:5"

# Read funding data
with open(funding_file_path, 'r') as f:
    funding_records = json.load(f)

# Read civic documents
with open(civic_file_path, 'r') as f:
    civic_documents = json.load(f)

# Filter projects containing 'FEMA' or 'emergency'
fema_emergency_projects = []
for record in funding_records:
    project_name = record.get('Project_Name', '').lower()
    if 'fema' in project_name or 'emergency' in project_name:
        fema_emergency_projects.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

# Extract project status information from civic documents
project_statuses = {}
for document in civic_documents:
    text = document.get('text', '')
    text_lower = text.lower()
    
    # Look for project sections and extract status
    if 'Updates:' in text or 'Project Schedule:' in text:
        # Find project names in the text
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        for i, line in enumerate(lines):
            if (line and len(line) < 100 and not line.startswith('Page') and not line.startswith('Agenda') 
                and not any(x in line for x in ['To:', 'From:', 'Subject:', 'Date:', 'Prepared by', 'Approved by'])):
                
                # Check if this is followed by project details
                if i + 1 < len(lines):
                    next_content = ' '.join(lines[i+1:min(i+10, len(lines))])
                    next_content_lower = next_content.lower()
                    
                    if 'updates' in next_content_lower or 'project schedule' in next_content_lower:
                        # Determine status
                        status = 'Unknown'
                        
                        if 'construction was completed' in text_lower:
                            status = 'completed'
                        elif 'under construction' in text_lower or 'out to bid' in text_lower:
                            status = 'construction'
                        elif 'design' in text_lower:
                            status = 'design'
                        elif 'not started' in text_lower:
                            status = 'not starter'
                        
                        if line not in project_statuses or project_statuses[line] == 'Unknown':
                            project_statuses[line] = status

# Create final combined results
final_list = []
for project in fema_emergency_projects:
    project_name = project['Project_Name']
    status = 'Unknown'
    
    # Check exact match
    if project_name in project_statuses:
        status = project_statuses[project_name]
    else:
        # Check partial match using base project name
        base_name = project_name.split('(')[0].strip()
        for civic_name, civic_status in project_statuses.items():
            if base_name.lower() in civic_name.lower() or civic_name.lower() in base_name.lower():
                status = civic_status
                break
    
    final_list.append({
        'Project_Name': project_name,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(final_list, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
