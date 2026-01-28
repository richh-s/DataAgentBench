code = """import json, re

# Load funding data
funding = json.load(open('/tmp/tmp_hb9f3fdk.json', 'r'))
civic_docs = json.load(open('/tmp/tmp_cdv8r04p.json', 'r'))

# Create funding lookup
funding_lookup = {item['Project_Name']: int(item['Amount']) for item in funding}

# Extract projects
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        match = re.match(r'^([^(]+)\(([\w\s]+)\)$', line)
        if match and i + 4 < len(lines):
            name = match.group(1).strip()
            status = match.group(2).strip().lower()
            topic = lines[i+1].strip().replace('topic:', '').strip()
            type_val = lines[i+2].strip().replace('type:', '').strip()
            st = lines[i+3].strip().replace('st:', '').strip()
            et = lines[i+4].strip().replace('et:', '').strip()
            projects.append({'name': name, 'topic': topic, 'type': type_val, 'status': status, 'st': st, 'et': et})
        i += 1

# Filter 2022 disaster projects
disaster_2022 = []
for p in projects:
    if '2022' in p['st']:
        if p['type'] == 'disaster' or re.search(r'\((FEMA|CalJPIA|CalOES) Project\)', p['name'], re.I):
            disaster_2022.append(p)

# Remove duplicates
unique = {p['name']: p for p in disaster_2022}
filtered = list(unique.values())

# Calculate funding
total = 0
matched = []
for p in filtered:
    if p['name'] in funding_lookup:
        amount = funding_lookup[p['name']]
        total += amount
        matched.append({'name': p['name'], 'amount': amount})

result = {'total_funding': total, 'project_count': len(matched), 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
