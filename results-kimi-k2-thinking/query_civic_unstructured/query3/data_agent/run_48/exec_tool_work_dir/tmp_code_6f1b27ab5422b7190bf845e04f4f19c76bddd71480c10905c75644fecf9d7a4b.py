code = """import json
import os

# Get the stored results
funding_result = locals()['var_functions.query_db:2']
civic_result = locals()['var_functions.query_db:0']

# Load funding data
funding_data = []
if isinstance(funding_result, str) and ('tmp' in funding_result):
    if os.path.exists(funding_result):
        with open(funding_result, 'r') as f:
            funding_data = json.load(f)
else:
    funding_data = funding_result

# Load civic documents
civic_docs = []
if isinstance(civic_result, str) and ('tmp' in civic_result):
    if os.path.exists(civic_result):
        with open(civic_result, 'r') as f:
            civic_docs = json.load(f)
else:
    civic_docs = civic_result

# Convert to correct types if needed
if not isinstance(funding_data, list):
    funding_data = []
if not isinstance(civic_docs, list):
    civic_docs = []

print("Loaded data successfully")
print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Find FEMA/emergency projects in funding data
fema_projects = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if 'FEMA' in project_name or 'emergency' in project_name.lower():
        fema_projects.append({
            'Project_Name': project_name,
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        })

print("FEMA/emergency projects found in funding:", len(fema_projects))

# Extract status from civic documents
extracted_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 10 and not line.startswith('('):
            lowercase_line = line.lower()
            if any(kw in lowercase_line for kw in ['project', 'repairs', 'improvements', 'sirens', 'drainage']):
                # Look ahead for status
                for j in range(i+1, min(i+4, len(lines))):
                    next_line = lines[j].lower()
                    status = None
                    if 'design' in next_line:
                        status = 'design'
                        break
                    elif 'completed' in next_line:
                        status = 'completed'
                        break
                    elif 'not started' in next_line:
                        status = 'not started'
                        break
                if status:
                    extracted_projects.append({'name': line, 'status': status})

print("Projects extracted from documents:", len(extracted_projects))

# Match and create final results
results = []
for funding_proj in fema_projects:
    project_name = funding_proj['Project_Name']
    status = 'Unknown'
    
    for extracted in extracted_projects:
        extracted_name = extracted['name']
        if (project_name.lower() in extracted_name.lower() or 
            extracted_name.lower() in project_name.lower()):
            status = extracted['status']
            break
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_proj['Funding_Source'],
        'Amount': funding_proj['Amount'],
        'Status': status
    })

# Print results
result_json = json.dumps(results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
