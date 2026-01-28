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

# Extract project information from documents
projects_info = []
doc = civic_docs[0]
text = doc.get('text', '')

# Find projects mentioning FEMA or Emergency
# Looking for patterns like project names followed by details
lines = text.splitlines()

fema_projects = []
project_name = None
project_block = []

for i, line in enumerate(lines):
    line = line.strip()
    # Skip empty lines and special markers
    if not line or line.startswith('(cid:') or line.startswith('Page'):
        continue
    
    # Check if line is a project name (not starting with bullet, reasonably short, title case)
    if len(line) < 80 and not line.startswith('•') and not line.startswith('-') and line[0].isupper():
        # Save previous project if it mentions FEMA/emergency
        if project_name and project_block:
            block_text = ' '.join(project_block)
            if 'FEMA' in block_text or 'emergency' in block_text.lower() or 'Emergency' in block_text:
                # Extract status
                status = 'unknown'
                if 'currently under construction' in block_text.lower():
                    status = 'construction'
                elif 'construction was completed' in block_text.lower() or 'completed' in block_text.lower():
                    status = 'completed'
                elif 'design' in block_text.lower() or 'awaiting' in block_text.lower():
                    status = 'design'
                
                # Determine type
                project_type = 'disaster' if 'FEMA' in block_text else 'capital'
                
                fema_projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'type': project_type
                })
        
        # Start new project
        project_name = line
        project_block = [line]
    else:
        # Continue current project block
        if project_name:
            project_block.append(line)

# Add the last project
if project_name and project_block:
    block_text = ' '.join(project_block)
    if 'FEMA' in block_text or 'emergency' in block_text.lower() or 'Emergency' in block_text:
        status = 'unknown'
        if 'currently under construction' in block_text.lower():
            status = 'construction'
        elif 'construction was completed' in block_text.lower() or 'completed' in block_text.lower():
            status = 'completed'
        elif 'design' in block_text.lower() or 'awaiting' in block_text.lower():
            status = 'design'
        
        project_type = 'disaster' if 'FEMA' in block_text else 'capital'
        
        fema_projects.append({
            'Project_Name': project_name,
            'status': status,
            'type': project_type
        })

# Filter funding data
fema_funding = []
for fund in funding_data:
    name = fund.get('Project_Name', '')
    if 'FEMA' in name or 'emergency' in name.lower() or 'Emergency' in name:
        fema_funding.append({
            'Project_Name': name,
            'Funding_Source': fund.get('Funding_Source', ''),
            'Amount': fund.get('Amount', 0)
        })

result = {
    'projects_from_docs': fema_projects,
    'funding_records': fema_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
