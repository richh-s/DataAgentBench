code = """import json
import re

# Load data from stored results
civic_docs_data = globals()['var_functions.query_db:0']
funding_data_data = globals()['var_functions.query_db:2']

# Load JSON data
civic_docs = json.load(open(civic_docs_data))
funding_data = json.load(open(funding_data_data))

# Process documents
projects = []
for doc in civic_docs:
    lines = doc['text'].split('\n')
    curr = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith('Page') or 'cid:' in line: continue
        if len(line) < 100 and not line.isupper() and line.istitle() == True and ('Project' in line or 'Improvements' in line):
            if curr: projects.append(curr)
            curr = {'name': line}
            curr['type'] = 'disaster' if ('FEMA' in line or 'CalOES' in line) else 'capital'
            topics = []
            if 'emergency' in line.lower(): topics.append('emergency warning')
            if 'FEMA' in line: topics.append('FEMA')
            if 'siren' in line.lower(): topics.append('emergency warning')
            curr['topic'] = ', '.join(topics)
            curr['status'] = ''
        elif curr and curr.get('status') == '':
            low = line.lower()
            if 'design' in low: curr['status'] = 'design'
            elif 'construction' in low: curr['status'] = 'construction'
            elif 'completed' in low: curr['status'] = 'completed'
            elif 'not started' in low: curr['status'] = 'not started'
    if curr: projects.append(curr)

# Filter for emergency/FEMA
emergency = [p for p in projects if ('emergency' in p['name'].lower() or 'fema' in p['name'].lower() or len(p['topic']) > 0)]

# Match with funding
funding_lookup = {}
for f in funding_data:
    funding_lookup[f['Project_Name']] = f

results = []
for p in emergency:
    if p['name'] in funding_lookup:
        f = funding_lookup[p['name']]
        results.append({'Project': p['name'], 'Funding': f['Funding_Source'], 'Amount': int(f['Amount']), 'Status': p['status'], 'Topic': p['topic']})
        
# Build response
output = 'Found ' + str(len(results)) + ' emergency/FEMA related projects:\n\n'
for r in results:
    output += r['Project'] + '\n'
    output += '  Funding: ' + r['Funding'] + ' ($' + str(r['Amount']) + ')\n'
    output += '  Status: ' + r['Status'] + '\n'
    output += '  Topic: ' + r['Topic'] + '\n\n'

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
