code = """import json
import re

# Load data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for >$50k
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name'].strip()] = amount

# Extract capital design project names
design_set = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
            
        if in_design and line.startswith('Capital') or line.startswith('DISASTER'):
            in_design = False
            continue
            
        if in_design and line and len(line) > 5:
            # Skip metadata
            if any(x in line for x in ['Updates:', 'Schedule:', 'cid:', 'Page', 'Staff', 'City', 'RECOMMENDED']):
                continue
            if re.search('Spring|Summer|Fall|Winter', line):
                continue
            # Clean the name - remove parentheticals
            clean = re.sub(r'\s+', ' ', line).strip()
            # Remove parentheses and content
            clean = re.sub(r'\s*\(.+\)$', '', clean)
            if clean and 'COMPLETE' not in clean.upper():
                design_set.add(clean)

# Match with funding
matched = 0
for design_name in design_set:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            matched += 1
            break

print('__RESULT__:', matched)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
