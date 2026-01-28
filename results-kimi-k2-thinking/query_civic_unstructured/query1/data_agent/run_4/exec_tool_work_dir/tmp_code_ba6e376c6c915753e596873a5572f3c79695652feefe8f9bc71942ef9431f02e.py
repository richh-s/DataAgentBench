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

# Find design projects
design_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Design' not in text:
        continue
        
    # Simple pattern matching
    in_design = False
    for line in text.split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
        if in_design and line.startswith('Capital'):
            if 'Construction' in line or 'Not Started' in line:
                break
        if in_design and line.startswith('DISASTER'):
            break
        if in_design and line and len(line) > 5:
            # Skip metadata
            if any(x in line for x in ['Updates', 'Schedule', 'cid:', 'Page']):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
                
            # Clean name
            clean = re.sub('\s+', ' ', line).strip()
            clean = re.sub('\s*\([^)]*\)$', '', clean)
            if 'COMPLETE DESIGN' in clean.upper():
                continue
            design_names.append(clean)

# Count matches
unique_design = list(set(design_names))
count = 0

for design in unique_design:
    for fund in funding_lookup.keys():
        if design == fund or fund.startswith(design + ' '):
            count += 1
            break

print('__RESULT__:', count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
