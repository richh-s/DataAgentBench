code = """import json, re, os

# Get file paths
civic_path = globals()['var_functions.query_db:0']
funding_path = globals()['var_functions.query_db:2']

print('Civic path:', civic_path[:100])
print('Funding path:', funding_path[:100])

# Read files
civic_docs = json.load(open(civic_path))
funding_data = json.load(open(funding_path))

print('Loaded', len(civic_docs), 'civic docs and', len(funding_data), 'funding records')

# Extract projects
projects = []
for doc in civic_docs:
    lines = doc['text'].split('\n')
    curr = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith('Page') or 'cid:' in line: continue
        if len(line) < 100 and not line.isupper() and (line.istitle() or 'Project' in line):
            if curr: projects.append(curr)
            curr = {'name': line, 'topic': '', 'type': '', 'status': '', 'file': doc['filename']}
            if 'FEMA' in line or 'CalOES' in line: curr['type'] = 'disaster'
            else: curr['type'] = 'capital'
            topics = []
            if 'emergency' in line.lower(): topics.append('emergency warning')
            if 'FEMA' in line: topics.append('FEMA')
            if 'siren' in line.lower(): topics.append('emergency warning')
            curr['topic'] = ', '.join(topics)
        elif curr:
            if 'design' in line.lower(): curr['status'] = 'design'
            elif 'construction' in line.lower(): curr['status'] = 'construction'
            elif 'completed' in line.lower(): curr['status'] = 'completed'
            elif 'not started' in line.lower(): curr['status'] = 'not started'
    if curr: projects.append(curr)

# Filter emergency/FEMA
emergency = [p for p in projects if 'emergency' in p['name'].lower() or 'fema' in p['name'].lower() or 'emergency' in p['topic'].lower()]

# Match with funding
funding_lookup = {f['Project_Name']: f for f in funding_data}
results = []
for p in emergency:
    if p['name'] in funding_lookup:
        f = funding_lookup[p['name']]
        results.append({'Project': p['name'], 'Funding': f['Funding_Source'], 'Amount': int(f['Amount']), 'Status': p['status'], 'Topic': p['topic']})

# Output
output = f'Found {len(results)} emergency/FEMA projects:\n\n'
for r in results:
    output += f"{r['Project']}\n  Funding: {r['Funding']} (${r['Amount']:,})\n  Status: {r['Status']}\n  Topic: {r['Topic']}\n\n"

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
