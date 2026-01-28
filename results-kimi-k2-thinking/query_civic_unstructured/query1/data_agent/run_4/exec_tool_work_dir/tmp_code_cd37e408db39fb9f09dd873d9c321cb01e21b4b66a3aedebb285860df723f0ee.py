code = """import json
import re

# Load data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > 50000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        name = item['Project_Name'].strip()
        funding_lookup[name] = amount

# Extract capital design projects
design_set = set()

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
            if any(x in line for x in ['Updates:', 'Schedule:', 'cid:', 'Page']):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if re.search('Spring|Summer|Fall|Winter', line):
                continue
                
            clean_name = re.sub('\s+', ' ', line).strip()
            clean_name = re.sub('\s*\([^)]*\)$', '', clean_name)
            if clean_name and 'COMPLETE DESIGN' not in clean_name.upper():
                design_set.add(clean_name)

# Count matches with funding
count = 0
for design_name in design_set:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            count += 1
            break

print('__RESULT__:', count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
