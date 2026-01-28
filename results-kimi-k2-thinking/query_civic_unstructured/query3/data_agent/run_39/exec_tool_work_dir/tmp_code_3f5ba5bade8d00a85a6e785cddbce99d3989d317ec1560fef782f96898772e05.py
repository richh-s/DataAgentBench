code = """import json, re

# Read data
civic_path = globals()['var_functions.query_db:0']
funding_path = globals()['var_functions.query_db:2']
civic_docs = json.load(open(civic_path))
funding_data = json.load(open(funding_path))

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
            curr['type'] = 'disaster' if 'FEMA' in line or 'CalOES' in line else 'capital'
            topics = []
            if 'emergency' in line.lower(): topics.append('emergency warning')
            if 'FEMA' in line: topics.append('FEMA')
            if 'siren' in line.lower(): topics.append('emergency warning')
            curr['topic'] = ', '.join(topics)
        elif curr:
            low = line.lower()
            if 'design' in low: curr['status'] = 'design'
            elif 'construction' in low: curr['status'] = 'construction'
            elif 'completed' in low: curr['status'] = 'completed'
            elif 'not started' in low: curr['status'] = 'not started'
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

# Build result string
out = 'Found ' + str(len(results)) + ' emergency/FEMA projects:\n\n'
for r in results:
    out += r['Project'] + '\n'
    out += '  Funding: ' + r['Funding'] + ' ($' + str(r['Amount']) + ')\n'
    out += '  Status: ' + r['Status'] + '\n'
    out += '  Topic: ' + r['Topic'] + '\n\n'

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
