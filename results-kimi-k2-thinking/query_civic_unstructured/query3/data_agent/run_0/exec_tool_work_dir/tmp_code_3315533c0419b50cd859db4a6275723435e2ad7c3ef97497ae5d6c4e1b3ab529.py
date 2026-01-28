code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter funding data for projects containing 'emergency' or 'FEMA' (case-insensitive)
filtered_funding = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    if 'emergency' in project_name or 'fema' in project_name:
        filtered_funding.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

# Load civic documents
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic documents
# We'll look for project names and their statuses in the text
project_status_map = {}

for doc in civic_docs:
    text = doc.get('text', '')
    # Extract project names and statuses
    # Look for patterns like "Project Name\n\n(⚬) Updates:" or similar structures
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for project names (typically on their own line, title case)
        if line and not line.startswith('(') and not line.startswith('•') and \
           not line.startswith('Page') and not line.startswith('Agenda') and \
           len(line) < 100 and not line.startswith('To:') and not line.startswith('From:') and \
           not line.startswith('Subject:') and not line.startswith('Date') and \
           not line.startswith('Prepared by') and not line.startswith('Approved by') and \
           not line.startswith('Meeting date') and not line.startswith('RECOMMENDED'):
            
            # Check if next few lines contain status indicators
            next_few_lines = ' '.join(lines[i+1:i+4]).lower()
            if 'updates:' in next_few_lines or 'status:' in next_few_lines or 'project schedule' in next_few_lines:
                current_project = line
                
                # Try to find status by looking ahead
                status = 'Unknown'
                look_ahead = ' '.join(lines[i+1:i+10]).lower()
                
                if 'construction was completed' in look_ahead or 'completed' in look_ahead:
                    status = 'completed'
                elif 'under construction' in look_ahead or 'construction' in look_ahead:
                    status = 'construction'
                elif 'design' in look_ahead:
                    status = 'design'
                elif 'not started' in look_ahead:
                    status = 'not started'
                    
                project_status_map[current_project] = status

# Now match funding projects with their statuses
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

# Print result in required format
print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
