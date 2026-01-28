code = """import json
import re

# Load all MongoDB documents from civic_docs_database
mongo_docs_path = locals()['var_functions.query_db:14']
with open(mongo_docs_path, 'r') as f:
    mongo_docs = json.load(f)

# Load all funding data from funding_database
# We need to run this query again first to get the actual data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create lookup dictionary for funding information
funding_dict = {}
for item in funding_data:
    project_name = item.get('Project_Name', '')
    funding_dict[project_name] = {
        'Funding_Source': item.get('Funding_Source', 'Not specified'),
        'Amount': item.get('Amount', 0)
    }

# Function to check if a project name or context is related to emergency/FEMA
def is_emergency_related(text, project_name):
    combined = (text + ' ' + project_name).lower()
    return (
        'fema' in combined or
        'emergency' in combined or
        'siren' in combined or
        'warning' in combined or
        'disaster' in combined
    )

# Extract projects from documents
emergency_projects = []

for doc in mongo_docs:
    text = doc['text']
    lines = text.split('
')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or len(line) < 5:
            continue
            
        # Skip known non-project lines
        skip_phrases = [
            'Public Works', 'Commission', 'Meeting', 'Agenda', 'Report',
            'To:', 'Prepared by:', 'Approved by:', 'Date', 'Subject:',
            'RECOMMENDED', 'DISCUSSION:', 'Page', 'Item', 'Capital Improvement',
            'Disaster Recovery', 'Projects (Design)', 'Projects (Construction)',
            'Projects (Not'
        ]
        
        if any(phrase in line for phrase in skip_phrases):
            continue
        
        # Look for potential project names followed by status info
        if i + 1 < len(lines):
            next_lines = '\n'.join(lines[i+1:i+4])
            
            # Check if this looks like a project (has status info following)
            if 'Updates:' in next_lines or 'Project Schedule:' in next_lines:
                
                # Get the status
                status = 'Unknown'
                for j in range(i+1, min(i+10, len(lines))):
                    curr_line = lines[j]
                    if 'Complete Construction:' in curr_line or 'c' in curr_line:
                        status = 'completed'
                        break
                    elif 'Begin Construction:' in curr_line:
                        status = 'in progress'
                        break
                    elif 'Advertise:' in curr_line or 'Project Schedule:' in curr_line:
                        status = 'design'
                        break
                    elif 'currently under construction' in curr_line.lower():
                        status = 'in progress'
                        break
                
                # Check if related to emergency/FEMA
                context = '\n'.join(lines[max(0,i-2):min(len(lines),i+8)])
                if is_emergency_related(context, line):
                    
                    # Get funding info
                    funding_info = funding_dict.get(line, {
                        'Funding_Source': 'Not specified',
                        'Amount': 0
                    })
                    
                    emergency_projects.append({
                        'Project_Name': line,
                        'Funding_Source': funding_info['Funding_Source'],
                        'Amount': funding_info['Amount'],
                        'Status': status
                    })

# Also check all funding records for FEMA/emergency keywords
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    
    if is_emergency_related('', proj_name):
        # Only add if not already captured
        exists = any(p['Project_Name'] == proj_name for p in emergency_projects)
        if not exists:
            # Try to find status from documents
            status = 'Unknown'
            for doc in mongo_docs:
                if proj_name in doc['text']:
                    doc_text = doc['text']
                    if 'currently under construction' in doc_text.lower():
                        status = 'in progress'
                    elif 'complete construction' in doc_text.lower():
                        status = 'completed'
                    break
            
            emergency_projects.append({
                'Project_Name': proj_name,
                'Funding_Source': fund.get('Funding_Source', 'Not specified'),
                'Amount': fund.get('Amount', 0),
                'Status': status
            })

# Remove duplicates
unique_projects = []
seen_names = set()
for p in emergency_projects:
    if p['Project_Name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['Project_Name'])

# Format output
print("__RESULT__:")
print(json.dumps(unique_projects, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
