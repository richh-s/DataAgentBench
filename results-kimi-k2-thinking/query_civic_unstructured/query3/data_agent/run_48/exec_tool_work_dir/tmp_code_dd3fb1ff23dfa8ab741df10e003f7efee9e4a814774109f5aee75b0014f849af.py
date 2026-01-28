code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:0']

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_documents = json.load(f)

print('Loaded', len(funding_records), 'funding records and', len(civic_documents), 'civic documents')

# Find FEMA/emergency projects in funding data
fema_projects = []
for rec in funding_records:
    name = rec['Project_Name']
    check_name = name.lower()
    if 'fema' in check_name or 'emergency' in check_name:
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

print('Found', len(fema_projects), 'FEMA/emergency related projects')

# Extract project status from civic documents
project_status = []
for doc in civic_documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        lower_line = line.lower()
        # Check if this line might be a project name
        if any(kw in lower_line for kw in ['project', 'repairs', 'sirens', 'warning', 'drainage']):
            # Look ahead to find status
            status = None
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].lower()
                if 'design' in next_line:
                    status = 'design'
                    break
                elif 'completed' in next_line or 'completion' in next_line:
                    status = 'completed'
                    break
                elif 'not started' in next_line:
                    status = 'not started'
                    break
            
            if status:
                project_status.append({'name': line, 'status': status})

print('Extracted', len(project_status), 'project statuses from documents')

# Match funding projects with status
results = []
for proj in fema_projects:
    matched_status = 'Unknown'
    proj_name_lower = proj['Project_Name'].lower()
    
    for ps in project_status:
        status_name_lower = ps['name'].lower()
        # Check if project names match (partial match is OK)
        if proj_name_lower in status_name_lower or status_name_lower in proj_name_lower:
            matched_status = ps['status']
            break
    
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': matched_status
    })

# Format and print result
result_json = json.dumps(results, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
