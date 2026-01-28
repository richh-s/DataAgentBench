code = """import json

# Load funding data from stored variable
with open(str(var_functions.query_db:0), 'r') as f:
    funding_records = json.load(f)

# Load civic documents from stored variable  
with open(str(var_functions.query_db:5), 'r') as f:
    civic_documents = json.load(f)

# Filter for FEMA and emergency projects
fema_projects = []
for record in funding_records:
    name = record.get('Project_Name', '').lower()
    if 'fema' in name or 'emergency' in name:
        fema_projects.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

# Extract project statuses from civic documents
status_map = {}
for doc in civic_documents:
    text = doc.get('text', '')
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    for i in range(len(lines)):
        line = lines[i]
        # Skip headers/footers
        if line.startswith('Page') or line.startswith('Agenda') or 'To:' in line or 'From:' in line:
            continue
        # Check if project name
        if i < len(lines)-5 and len(line) > 5 and len(line) < 100:
            if 'updates' in ' '.join(lines[i:i+5]).lower():
                # Determine status
                doc_lower = text.lower()
                if 'construction was completed' in doc_lower:
                    status = 'completed'
                elif 'under construction' in doc_lower or 'out to bid' in doc_lower:
                    status = 'construction'
                elif 'design' in doc_lower:
                    status = 'design'
                elif 'not started' in doc_lower:
                    status = 'not_started'
                else:
                    status = 'Unknown'
                status_map[line] = status

# Match projects with status
results = []
for project in fema_projects:
    pname = project['Project_Name']
    pstatus = 'Unknown'
    
    # Exact match
    if pname in status_map:
        pstatus = status_map[pname]
    else:
        # Partial match
        base = pname.split('(')[0].strip()
        for key, val in status_map.items():
            if base.lower() in key.lower():
                pstatus = val
                break
    
    results.append({
        'Project_Name': pname,
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': pstatus
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
