code = """import json

# Load data from the stored variables
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:6']

# Load the data if they are file paths
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert funding amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

# Extract park-related projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for completion information and park-related keywords
    # Pattern: project name followed by completion date containing 2022
    
    # Split into lines for easier parsing
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if line mentions completion in 2022
        if '2022' in line and ('complete' in line.lower() or 'completed' in line.lower() or 'construction was completed' in line.lower()):
            # Look backwards to find the project name (usually a few lines above)
            project_name = None
            
            # Check previous lines for project name
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and len(prev_line) < 100:
                    # Check if it's park-related
                    park_keywords = ['park', 'playground', 'walkway', 'green streets', 'bluffs', 'shade structure', 'arbors', 'benches', 'workout station']
                    if any(keyword in prev_line.lower() for keyword in park_keywords):
                        project_name = prev_line
                        break
            
            if project_name:
                # Clean up project name
                project_name = project_name.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                
                # Add to our list
                park_projects_2022.append({
                    'name': project_name,
                    'completion_note': line,
                    'doc_id': doc['_id']
                })

# Now match with funding data
park_funding_2022 = []
for project in park_projects_2022:
    proj_name = project['name']
    
    # Look for exact or partial matches in funding data
    for funding_record in funding_data:
        fund_proj_name = funding_record['Project_Name']
        
        # Check for exact match or if the civic project name contains the funding project name
        # or vice versa
        if (proj_name.lower() in fund_proj_name.lower() or 
            fund_proj_name.lower() in proj_name.lower()):
            park_funding_2022.append({
                'project_name': proj_name,
                'funding_project_name': fund_proj_name,
                'amount': funding_record['Amount'],
                'funding_source': funding_record['Funding_Source']
            })
            break  # Assume first match is the correct one

# Calculate total funding
total_funding = sum([p['amount'] for p in park_funding_2022])

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022_count': len(park_projects_2022),
    'matched_funding_records': len(park_funding_2022),
    'total_funding': total_funding,
    'projects': park_funding_2022
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
