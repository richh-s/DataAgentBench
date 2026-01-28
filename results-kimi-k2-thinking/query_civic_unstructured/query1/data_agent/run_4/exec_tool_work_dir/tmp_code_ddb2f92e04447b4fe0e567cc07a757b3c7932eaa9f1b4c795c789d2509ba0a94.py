code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup for projects > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name'].strip()] = amount

# Extract capital design project names
design_project_set = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        
        # Check for design section header
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
        
        # Exit design section
        if in_design and line.startswith('Capital'):
            if 'Construction' in line or 'Not Started' in line:
                in_design = False
                continue
        if in_design and line.startswith('DISASTER'):
            in_design = False
            continue
        
        # Get project names
        if in_design and line and len(line) > 5:
            # Skip metadata
            if any(x in line for x in ['Updates:', 'Schedule:', 'Page', 'Agenda', 'cid:', 'RECOMMENDED', 'DISCUSSION']):
                continue
            if line.startswith('Staff') or line.startswith('City') or line.startswith('Complete'):
                continue
            if re.search('Spring|Summer|Fall|Winter', line):
                continue
            # Clean name
            clean_name = re.sub(r'\s+', ' ', line)
            clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
            clean_name = clean_name.strip()
            if clean_name and 'COMPLETE DESIGN' not in clean_name.upper() and 'ADVERTISE' not in clean_name.upper():
                design_project_set.add(clean_name)

# Match with funding
matched_count = 0
for design_name in design_project_set:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matched_count += 1
            break

print('__RESULT__:', matched_count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
