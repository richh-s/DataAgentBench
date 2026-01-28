code = """import json

# Read the data from file paths
with open(locals()['var_functions.query_db:2'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:0'], 'r') as f:
    civic_docs = json.load(f)

# Step 1: Find emergency/FEMA projects in funding data
emergency_projects = []
for record in funding_data:
    if 'emergency' in record['Project_Name'].lower() or 'fema' in record['Project_Name'].lower():
        emergency_projects.append(record)

# Step 2: Extract project details from civic documents
project_details = {}
for doc in civic_docs:
    text = doc['text'].lower()
    original_lines = doc['text'].split('\n')
    
    for line in original_lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        line_lower = line_clean.lower()
        if 'emergency' in line_lower or 'fema' in line_lower or 'warning' in line_lower or 'siren' in line_lower:
            # Determine status
            status = 'not started'
            if 'under construction' in text and line_lower in text:
                status = 'completed'
            elif 'design' in text and 'complete design' not in text:
                status = 'design'
            
            # Determine type
            proj_type = 'disaster' if 'fema' in line_lower else 'capital'
            
            project_details[line_clean] = {'Status': status, 'Type': proj_type}

# Step 3: Merge and create final results
merged_results = []
for funding_proj in emergency_projects:
    proj_name = funding_proj['Project_Name']
    
    # Default values
    status = 'not started'
    proj_type = 'disaster' if 'fema' in proj_name.lower() else 'capital'
    
    # Try to find matching details
    if proj_name in project_details:
        status = project_details[proj_name]['Status']
        proj_type = project_details[proj_name]['Type']
    
    merged_results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding_proj['Funding_Source'],
        'Amount': funding_proj['Amount'],
        'Status': status,
        'Type': proj_type
    })

print('__RESULT__:')
print(json.dumps(merged_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'docs_type': "<class 'str'>"}}

exec(code, env_args)
