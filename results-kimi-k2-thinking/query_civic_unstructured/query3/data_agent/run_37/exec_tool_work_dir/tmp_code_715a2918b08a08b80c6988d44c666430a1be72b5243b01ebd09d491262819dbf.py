code = """import json
import re

# Load data files
funding_path = locals()['var_functions.query_db:0']
civic_docs_path = locals()['var_functions.query_db:4']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    if name:
        funding_lookup[name] = {
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        }

# Extract project info from civic documents
extracted_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for project sections in the text
    # Pattern to find project names and their details
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names (typically capitalized, often with parentheses for FEMA)
        # This is a heuristic approach
        if (line.isupper() and len(line) > 10) or '(FEMA' in line or 'Project' in line:
            # Potential project name
            if len(line) < 100:  # Not too long to be a paragraph
                current_project = line
                
                # Check if this project has funding
                if current_project in funding_lookup:
                    funding_info = funding_lookup[current_project]
                    
                    # Try to determine status from context
                    status = 'Unknown'
                    if 'completed' in text.lower() and current_project in text:
                        status = 'completed'
                    elif 'design' in text.lower() or 'planning' in text.lower():
                        status = 'design'
                    elif 'construction' in text.lower():
                        status = 'construction'
                    elif 'not started' in text.lower():
                        status = 'not started'
                    
                    extracted_projects.append({
                        'Project_Name': current_project,
                        'Funding_Source': funding_info['Funding_Source'],
                        'Amount': funding_info['Amount'],
                        'Status': status
                    })

# Also add projects that have FEMA/emergency in their name but might not be in the documents
for proj_name, funding_info in funding_lookup.items():
    if ('FEMA' in proj_name.upper() or 'EMERGENCY' in proj_name.upper()) and proj_name not in [p['Project_Name'] for p in extracted_projects]:
        extracted_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': funding_info['Funding_Source'],
            'Amount': funding_info['Amount'],
            'Status': 'Unknown'
        })

__RESULT__ = json.dumps(extracted_projects)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
