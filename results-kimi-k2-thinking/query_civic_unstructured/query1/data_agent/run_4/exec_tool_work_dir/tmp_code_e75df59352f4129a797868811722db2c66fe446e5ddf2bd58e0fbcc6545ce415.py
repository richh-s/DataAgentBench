code = """import json
import re

# Load data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding[item['Project_Name'].strip()] = amount

# Extract design projects
names = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_section = False
    
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_section = True
            continue
        if in_section and line.startswith('Capital'):
            if 'Construction' in line or 'Not Started' in line:
                in_section = False
                continue
        if in_section and line.startswith('DISASTER'):
            in_section = False
            continue
        if in_section and line and len(line) > 5:
            # Skip meta lines
            meta = ['Updates', 'Schedule', 'cid:', 'Page', 'Staff', 'City', 'RECOMMENDED', 'DISCUSSION']
            if any(m in line for m in meta):
                continue
            if re.search('Spring|Summer|Fall|Winter', line):
                continue
                
            # Clean name
            clean = re.sub('\s+', ' ', line).strip()
            clean = re.sub('\s*\([^)]*\)$', '', clean)
            if 'COMPLETE DESIGN' in clean.upper():
                continue
            names.append(clean)

# Count matches
unique_names = list(set(names))
count = 0
for design in unique_names:
    for fund_name in funding.keys():
        if design == fund_name or fund_name.startswith(design + ' '):
            count += 1
            break

print('__RESULT__:', count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
