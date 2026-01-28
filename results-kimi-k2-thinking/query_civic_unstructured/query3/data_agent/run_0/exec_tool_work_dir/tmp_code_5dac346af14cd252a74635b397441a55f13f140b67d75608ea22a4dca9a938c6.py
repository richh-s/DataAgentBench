code = """import json

# Get file paths
f1 = var_functions.query_db:0
f2 = var_functions.query_db:5

# Load data
with open(f1, 'r') as f:
    funding = json.load(f)
with open(f2, 'r') as f:
    civic = json.load(f)

# Find FEMA/emergency projects
projects = []
for r in funding:
    name = r.get('Project_Name', '').lower()
    if 'fema' in name or 'emergency' in name:
        projects.append({
            'Project_Name': r.get('Project_Name'),
            'Funding_Source': r.get('Funding_Source'),
            'Amount': int(r.get('Amount', 0))
        })

# Extract status
status_map = {}
for doc in civic:
    text = doc.get('text', '')
    txt_low = text.lower()
    
    # Status indicators
    if 'construction was completed' in txt_low:
        status_val = 'completed'
    elif 'under construction' in txt_low or 'out to bid' in txt_low:
        status_val = 'construction'
    elif 'design' in txt_low:
        status_val = 'design'
    elif 'not started' in txt_low:
        status_val = 'not_started'
    else:
        status_val = 'Unknown'
    
    # Extract project names
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i in range(len(lines)):
        line = lines[i]
        if (line and len(line) < 100 and not line.startswith('Page') 
            and not line.startswith('Agenda') and 'To:' not in line and 'From:' not in line
            and 'Subject:' not in line and 'Date:' not in line):
            
            if i+1 < len(lines):
                next_part = ' '.join(lines[i+1:min(i+5, len(lines))]).lower()
                if 'updates' in next_part or 'project schedule' in next_part:
                    status_map[line] = status_val

# Combine
result = []
for p in projects:
    name = p['Project_Name']
    stat = 'Unknown'
    
    if name in status_map:
        stat = status_map[name]
    else:
        base = name.split('(')[0].strip()
        for key, val in status_map.items():
            if base.lower() in key.lower():
                stat = val
                break
    
    result.append({
        'Project_Name': name,
        'Funding_Source': p['Funding_Source'],
        'Amount': p['Amount'],
        'Status': stat
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
