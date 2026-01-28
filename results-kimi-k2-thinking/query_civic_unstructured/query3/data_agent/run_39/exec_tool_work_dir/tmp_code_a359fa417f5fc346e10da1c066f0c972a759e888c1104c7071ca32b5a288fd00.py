code = """import json, re

# Read the civic documents and funding data from files
civic_docs_file = globals()['var_functions.query_db:0']
funding_file = globals()['var_functions.query_db:2']

civic_docs = json.load(open(civic_docs_file))
funding_data = json.load(open(funding_file))

print('Loaded', len(civic_docs), 'civic documents and', len(funding_data), 'funding records')

# Extract projects
all_projects = []
for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    lines = text.split('\n')
    curr_proj = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('Page') or 'cid:' in line:
            continue
            
        # Check if line looks like a project name
        if (len(line) < 100 and (line.istitle() or 'Project' in line or 'Improvements' in line)
            and not line.isupper() and ':' not in line[:30]):
            
            # Save previous project
            if curr_proj:
                all_projects.append(curr_proj)
            
            # New project
            curr_proj = {
                'Project_Name': line,
                'topic': '',
                'type': 'disaster' if ('FEMA' in line or 'CalOES' in line) else 'capital',
                'status': '',
                'source_file': filename
            }
            
            # Extract topics
            topics = []
            if 'emergency' in line.lower(): topics.append('emergency warning')
            if 'FEMA' in line: topics.append('FEMA')
            if 'siren' in line.lower() or 'warning' in line.lower(): topics.append('emergency warning')
            if 'drain' in line.lower() or 'storm' in line.lower(): topics.append('drainage')
            if 'road' in line.lower(): topics.append('road')
            if 'park' in line.lower(): topics.append('park')
            curr_proj['topic'] = ', '.join(topics)
        
        elif curr_proj:
            line_lower = line.lower()
            # Extract status
            if 'design' in line_lower and not curr_proj['status']:
                curr_proj['status'] = 'design'
            elif 'construction' in line_lower:
                curr_proj['status'] = 'construction'
            elif 'completed' in line_lower and not curr_proj['status']:
                curr_proj['status'] = 'completed'
            elif 'not started' in line_lower:
                curr_proj['status'] = 'not started'
    
    if curr_proj:
        all_projects.append(curr_proj)

# Filter for emergency/FEMA
emergency_projects = []
for p in all_projects:
    if 'emergency' in p['Project_Name'].lower() or 'fema' in p['Project_Name'].lower() or 'emergency' in p['topic'].lower() or 'fema' in p['topic'].lower():
        emergency_projects.append(p)

# Match with funding
funding_lookup = {}
for f in funding_data:
    funding_lookup[f['Project_Name']] = f

results = []
for p in emergency_projects:
    if p['Project_Name'] in funding_lookup:
        f = funding_lookup[p['Project_Name']]
        results.append({
            'Project_Name': p['Project_Name'],
            'Funding_Source': f['Funding_Source'],
            'Amount': f['Amount'],
            'Status': p['status'] if p['status'] else 'Unknown',
            'Topic': p['topic']
        })

answer = []
for r in results:
    answer.append({
        'Project_Name': r['Project_Name'],
        'Funding_Source': r['Funding_Source'],
        'Amount': int(r['Amount']),
        'Status': r['Status'],
        'Topic': r['Topic']
    })

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
