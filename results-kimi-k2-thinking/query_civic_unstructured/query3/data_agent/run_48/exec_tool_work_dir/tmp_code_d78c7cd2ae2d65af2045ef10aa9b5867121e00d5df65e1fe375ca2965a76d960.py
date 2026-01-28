code = """import json
import os

# Access stored results
funding_result = locals()['var_functions.query_db:2']
civic_result = locals()['var_functions.query_db:0']

# Load data
funding_data = []
if type(funding_result) == str and 'tmp' in funding_result:
    if os.path.exists(funding_result):
        with open(funding_result, 'r') as f:
            funding_data = json.load(f)
else:
    funding_data = funding_result

civic_docs = []
if type(civic_result) == str and 'tmp' in civic_result:
    if os.path.exists(civic_result):
        with open(civic_result, 'r') as f:
            civic_docs = json.load(f)
else:
    civic_docs = civic_result

# Ensure we have lists
if not isinstance(funding_data, list):
    funding_data = []
if not isinstance(civic_docs, list):
    civic_docs = []

print("Data loaded:", len(funding_data), "funding records", len(civic_docs), "civic documents")

# Find FEMA/emergency projects
fema_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if 'FEMA' in project_name or 'fema' in project_name or 'emergency' in project_name.lower():
        fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        })

print("Found", len(fema_projects), "FEMA/emergency projects in funding data")

# Extract project status from civic documents
status_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, curr_line in enumerate(lines):
        curr_line = curr_line.strip()
        if len(curr_line) < 10 or curr_line.startswith('('):
            continue
            
        lower_line = curr_line.lower()
        # Check if project name pattern
        if any(kw in lower_line for kw in ['project', 'repairs', 'improvements', 'sirens', 'warning', 'drainage']):
            # Look ahead for status
            found_status = None
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'design' in next_line:
                    found_status = 'design'
                    break
                elif 'completed' in next_line:
                    found_status = 'completed'
                    break
                elif 'not started' in next_line:
                    found_status = 'not started'
                    break
            
            if found_status:
                status_projects.append({'name': curr_line, 'status': found_status})

print("Extracted", len(status_projects), "projects with status from documents")

# Match projects and create results
results = []
for fema_proj in fema_projects:
    matched_status = 'Unknown'
    for sp in status_projects:
        sp_name = sp['name']
        fp_name = fema_proj['Project_Name']
        if fp_name.lower() in sp_name.lower() or sp_name.lower() in fp_name.lower():
            matched_status = sp['status']
            break
    
    results.append({
        'Project_Name': fema_proj['Project_Name'],
        'Funding_Source': fema_proj['Funding_Source'],
        'Amount': fema_proj['Amount'],
        'Status': matched_status
    })

# Output in required format
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
