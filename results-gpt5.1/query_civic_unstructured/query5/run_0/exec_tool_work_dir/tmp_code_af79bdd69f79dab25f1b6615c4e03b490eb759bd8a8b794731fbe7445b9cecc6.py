code = """import re, json
from pathlib import Path

path = Path(var_call_gnNOY96oVqE62NLbtCFV8FK7)
with open(path, 'r') as f:
    civic_docs = json.load(f)

funding = var_call_izbUARjQBSPPPZ0xPSfZsNrX

projects = {}
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        s = line.strip()
        if not s:
            continue
        if any(k in s for k in ['Project', 'Improvements', 'Repairs', 'Storm Drain', 'Slope', 'Warning', 'Fire', 'FEMA', 'CalOES', 'CalJPIA', 'Bridge', 'Culvert']):
            name = s
            if len(name) < 5 or len(name) > 200:
                continue
            if name not in projects:
                projects[name] = {'Project_Name': name, 'type': None, 'st': None}

for p in projects.values():
    n = p['Project_Name']
    if any(tag in n for tag in ['FEMA', 'CalOES', 'CalJPIA', 'Fire', 'Disaster', 'Slope Repairs', 'Storm Drain', 'Culvert', 'Bridge Repairs', 'Warning Sirens', 'Warning Signs']):
        p['type'] = 'disaster'
    else:
        p['type'] = 'capital'

for p in projects.values():
    if '2022' in p['Project_Name']:
        p['st'] = '2022'


disaster_2022_names = {p['Project_Name'] for p in projects.values() if p['type'] == 'disaster' and p['st'] == '2022'}

for row in funding:
    name = row['Project_Name']
    if ('2022' in name) and any(tag in name for tag in ['FEMA', 'CalOES', 'CalJPIA', 'Fire', 'Storm Drain', 'Culvert', 'Slope', 'Bridge', 'Warning']):
        disaster_2022_names.add(name)


total = 0
for row in funding:
    if row['Project_Name'] in disaster_2022_names:
        try:
            total += int(row['Amount'])
        except Exception:
            pass

result = {'total_funding_disaster_2022': total, 'matched_projects': sorted(list(disaster_2022_names))}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_gnNOY96oVqE62NLbtCFV8FK7': 'file_storage/call_gnNOY96oVqE62NLbtCFV8FK7.json', 'var_call_izbUARjQBSPPPZ0xPSfZsNrX': 'file_storage/call_izbUARjQBSPPPZ0xPSfZsNrX.json'}

exec(code, env_args)
