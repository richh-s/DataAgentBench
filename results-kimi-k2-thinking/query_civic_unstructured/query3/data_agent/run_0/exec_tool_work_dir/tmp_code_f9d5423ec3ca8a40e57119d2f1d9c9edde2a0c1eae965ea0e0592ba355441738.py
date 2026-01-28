code = """import json

# Get file paths from variables
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:5']

# Read data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Find FEMA/emergency projects
fema_projects = []
for r in funding_data:
    name = r.get('Project_Name', '').lower()
    if 'fema' in name or 'emergency' in name:
        fema_projects.append({
            'Project_Name': r.get('Project_Name', ''),
            'Funding_Source': r.get('Funding_Source', ''),
            'Amount': int(r.get('Amount', 0))
        })

# Extract status info
status_map = {}
for doc in civic_data:
    text = doc.get('text', '')
    doc_lower = text.lower()
    
    # Set status based on document content
    status = 'Unknown'
    if 'construction was completed' in doc_lower:
        status = 'completed'
    elif 'under construction' in doc_lower:
        status = 'construction'
    elif 'design' in doc_lower:
        status = 'design'
    elif 'not started' in doc_lower:
        status = 'not started'
    
    # Extract project names
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    for i in range(len(lines)):
        line = lines[i]
        if line and len(line) < 100 and not line.startswith('Page') and not line.startswith('Agenda'):
            if i+1 < len(lines) and 'updates' in ' '.join(lines[i+1:i+4]).lower():
                status_map[line] = status

# Match
results = []
for p in fema_projects:
    pname = p['Project_Name']
    pstatus = 'Unknown'
    
    if pname in status_map:
        pstatus = status_map[pname]
    else:
        base = pname.split('(')[0].strip()
        for key, val in status_map.items():
            if base.lower() in key.lower():
                pstatus = val
                break
    
    results.append({
        'Project_Name': pname,
        'Funding_Source': p['Funding_Source'],
        'Amount': p['Amount'],
        'Status': pstatus
    })

# Output
output_str = json.dumps(results, indent=2)
print('__RESULT__:')
print(output_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
