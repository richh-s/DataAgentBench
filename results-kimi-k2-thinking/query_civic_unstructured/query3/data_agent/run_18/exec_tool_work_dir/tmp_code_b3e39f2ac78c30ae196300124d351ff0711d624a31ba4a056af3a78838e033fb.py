code = """import json
import os

# Read the data from file paths
funding_path = locals()['var_functions.query_db:2']
docs_path = locals()['var_functions.query_db:0']

# Load funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Find emergency/FEMA related projects in funding data
emergency_projects = []

for record in funding_data:
    project_name = record['Project_Name'].lower()
    if 'emergency' in project_name or 'fema' in project_name:
        emergency_projects.append(record)

print('Found', len(emergency_projects), 'emergency/FEMA projects in funding data')

# Step 2: Extract project details from civic documents
def extract_project_details():
    details_dict = {}
    
    for doc in civic_docs:
        text = doc['text'].lower()
        lines = doc['text'].split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Look for project names (typically longer lines with keywords)
            if len(line) > 8:
                proj_lower = line.lower()
                
                # Check if it's emergency/FEMA related
                if 'emergency' in proj_lower or 'fema' in proj_lower or 'warning' in proj_lower or 'siren' in proj_lower:
                    # Determine status
                    status = 'not started'
                    if 'under construction' in text and line.lower() in text:
                        status = 'completed'
                    elif 'design' in text and 'complete design' not in text:
                        if line.lower() in text:
                            status = 'design'
                    
                    # Determine type
                    proj_type = 'disaster' if 'fema' in proj_lower else 'capital'
                    
                    details_dict[line.strip()] = {
                        'Status': status,
                        'Type': proj_type
                    }
    
    return details_dict

project_details = extract_project_details()

# Step 3: Merge funding data with project details
merged_results = []

for funding_proj in emergency_projects:
    proj_name = funding_proj['Project_Name']
    proj_name_lower = proj_name.lower()
    
    # Default values
    status = 'not started'
    proj_type = 'disaster' if 'fema' in proj_name_lower else 'capital'
    
    # Try to find matching project details
    if proj_name in project_details:
        status = project_details[proj_name]['Status']
        proj_type = project_details[proj_name]['Type']
    else:
        # Try partial matching
        for doc_proj_name, details in project_details.items():
            # Check if project names are similar
            if (proj_name.replace('(FEMA)', '').replace('(CalOES)', '').replace('(CalJPIA)', '').strip() in doc_proj_name or
                doc_proj_name.replace('(FEMA)', '').replace('(CalOES)', '').replace('(CalJPIA)', '').strip() in proj_name):
                status = details['Status']
                proj_type = details['Type']
                break
    
    merged_results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding_proj['Funding_Source'],
        'Amount': funding_proj['Amount'],
        'Status': status,
        'Type': proj_type
    })

# Output results
output = []
for result in merged_results:
    output.append(f"- Project: {result['Project_Name']}")
    output.append(f"  Funding Source: {result['Funding_Source']}")
    output.append(f"  Amount: ${result['Amount']:")
    output.append(f"  Status: {result['Status']}")
    output.append(f"  Type: {result['Type']}")

# Print in required format
print('__RESULT__:')
print(json.dumps(merged_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'docs_type': "<class 'str'>"}}

exec(code, env_args)
