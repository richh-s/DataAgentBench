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

# Build funding lookup for projects > 50000
funding_by_name = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        proj = item['Project_Name'].strip()
        funding_by_name[proj] = amount

# Find capital projects with design status
all_design_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_capital_design = False
    
    for line in lines:
        line = line.strip()
        
        # Start of capital design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_capital_design = True
            continue
            
        # End of section check
        if in_capital_design:
            if (line.startswith('Capital') and 'Construction' in line) or \
               (line.startswith('Capital') and 'Not Started' in line) or \
               line.startswith('DISASTER'):
                in_capital_design = False
                continue
                
        # Capture project name
        if in_capital_design and line and len(line) > 5:
            # Skip non-project lines
            if any(x in line for x in ['Updates:', 'Schedule:', 'rec', 'cid:', 'Page', 'Agenda']):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if re.search(r'(Spring|Summer|Fall|Winter)', line):
                continue
                
            # Clean the name
            clean_name = re.sub(r'\s+', ' ', line).strip()
            clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
            
            if clean_name and 'COMPLETE DESIGN' not in clean_name.upper() and 'ADVERTISE' not in clean_name.upper():
                all_design_names.append(clean_name)

# Remove duplicates
unique_design = list(set(all_design_names))

# Count matches with funding
design_capital_count = 0
for design_name in unique_design:
    for fund_name in funding_by_name.keys():
        if design_name == fund_name or \
           fund_name.startswith(design_name + ' ') or \
           fund_name.startswith(design_name + '('):
            design_capital_count += 1
            break

print('__RESULT__:', design_capital_count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
