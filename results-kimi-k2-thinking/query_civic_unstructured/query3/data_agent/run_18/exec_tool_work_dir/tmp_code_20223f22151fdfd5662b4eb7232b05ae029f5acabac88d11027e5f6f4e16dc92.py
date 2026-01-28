code = """import json

# Load data
with open(locals()['var_functions.query_db:2']) as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:0']) as f:
    docs = json.load(f)

# Step 1: Get all emergency/FEMA projects from funding
emergency_funding = []
for rec in funding:
    pname_lower = rec['Project_Name'].lower()
    if 'emergency' in pname_lower or 'fema' in pname_lower:
        emergency_funding.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

# Step 2: Create a lookup for project status from civic docs
project_status_lookup = {}
for doc in docs:
    text = doc['text'].lower()
    # Look for project sections
    lines = doc['text'].split('\n')
    for line in lines:
        line_clean = line.strip()
        if line_clean:
            line_lower = line_clean.lower()
            if 'emergency' in line_lower or 'fema' in line_lower or 'warning' in line_lower or 'siren' in line_lower:
                # Determine status
                status = 'not started'
                if 'under construction' in text and line_lower in text:
                    status = 'completed'
                elif 'design' in text and 'complete design' not in text:
                    status = 'design'
                project_status_lookup[line_clean] = status

# Step 3: Merge funding with status info
final_results = []
for proj in emergency_funding:
    proj_name = proj['Project_Name']
    status = project_status_lookup.get(proj_name, 'not started')
    
    # Determine type
    proj_type = 'disaster' if 'fema' in proj_name.lower() else 'capital'
    
    final_results.append({
        'Project_Name': proj_name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status,
        'Type': proj_type
    })

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'docs_type': "<class 'str'>"}, 'var_functions.execute_python:34': {'funding_count': 500, 'docs_count': 5}}

exec(code, env_args)
