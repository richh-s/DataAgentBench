code = """import json
import re

# Access the stored data directly
funding_data = locals()['var_functions.query_db:0']
civic_docs = locals()['var_functions.query_db:2']

# If these are file paths, load them
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding = json.load(f)
    with open(civic_docs, 'r') as f:
        docs = json.load(f)
else:
    # Already loaded data
    funding = funding_data
    docs = civic_docs

# Create funding lookup
funded = {}
for rec in funding:
    key = rec['Project_Name'].strip().lower()
    funded[key] = int(rec['Amount'])

# Extract design capital projects
design = []
for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        # Find the design section
        idx = text.find('(Design)')
        if idx != -1:
            section_start = idx
            section_end = text.find('(Construction)', idx)
            if section_end == -1:
                section_end = len(text)
            
            section = text[section_start:section_end]
            for line in section.split('\n'):
                line = line.strip()
                if line and len(line) > 5 and '▪' not in line and 'Updates:' not in line:
                    if 'Project Schedule:' not in line and 'Page' not in line and 'Capital Improvement' not in line:
                        if i + 1 < len(lines) and ('Updates:') in lines[i+1]:
                            design.append(line.lower())
                        elif 'Updates:' not in line:
                            design.append(line.lower())

# Try a different approach - look for key project names that show funding in the earlier preview
project_names = [
    'pcl median improvements project',
    'westward beach road drainage improvements project',
    'clover heights storm drainage improvements',
    'latigo canyon road retaining wall repair project',
    'storm drain master plan',
    'trancas canyon park playground',
    'permanent skate park',
    'pch at trancas canyon road right turn lane',
    'outdoor warning signs',
    'malibu bluffs park south walkway repairs',
    'malibu canyon road traffic study'
]

count = 0
for name in project_names:
    if name in funded and funded[name] > 50000:
        count += 1
    else:
        # Check partial matches
        for funded_name, amount in funded.items():
            if amount > 50000 and (name in funded_name or funded_name in name):
                count += 1
                break

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0}

exec(code, env_args)
