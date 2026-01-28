code = """import json
import re

# Load data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_items = json.load(f)

c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    civic_items = json.load(f)

# Filter funding > $50k
high_funding = {}
for item in funding_items:
    if int(item['Amount']) > 50000:
        high_funding[item['Project_Name'].strip()] = int(item['Amount'])

# Extract capital projects with design status
capital_design = []

for doc in civic_items:
    text = doc.get('text', '')
    # Pattern: look for capital design sections
    if 'Capital Improvement Projects' in text and 'Design' in text:
        # Split into lines and process
        lines = text.split('\n')
        capture = False
        
        for line in lines:
            line = line.strip()
            
            # Check if entering design section
            if 'Capital Improvement Projects' in line and 'Design' in line:
                capture = True
                continue
                
            # Check if leaving design section
            if capture and (line.startswith('Capital') or line.startswith('DISASTER')):
                if 'Construction' in line or 'Not Started' in line or line.startswith('DISASTER'):
                    capture = False
                    continue
                    
            # Extract project name
            if capture and line and len(line) > 5:
                # Skip metadata
                if any(term in line for term in ['Updates:', 'Schedule:', 'Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION']):
                    continue
                if line.startswith('Staff') or line.startswith('City'):
                    continue
                if re.search('Spring|Summer|Fall|Winter', line):
                    continue
                    
                # Clean the name
                clean_name = re.sub(r'\s+', ' ', line).strip()
                clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
                
                if clean_name and 'COMPLETE DESIGN' not in clean_name.upper() and 'ADVERTISE' not in clean_name.upper():
                    capital_design.append(clean_name)

# Remove duplicates
unique_design = list(set(capital_design))

# Match with funding - count unique matches
matched = 0
for design_name in unique_design:
    for fund_name in high_funding.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matched += 1
            break

print('__RESULT__:', matched)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
