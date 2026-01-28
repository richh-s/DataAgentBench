code = """import json
import re

# Load data sources
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Filter funding projects > $50,000
funding_lookup = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name'].strip()] = amt

# Extract capital design projects
project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        
        # Detect capital design section  
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
            
        # End of design section
        if in_design:
            if (line.startswith('Capital') and ('Construction' in line or 'Not Started' in line)) or \
               line.startswith('DISASTER'):
                in_design = False
                continue
                
        # Extract project name
        if in_design and line and len(line) > 5:
            # Skip metadata
            if any(x in line for x in ['Updates:', 'Schedule:', 'cid:', 'Page', 'Staff', 'City']):
                continue
            if re.search('Spring|Summer|Fall|Winter', line):
                continue
                
            clean = re.sub('\s+', ' ', line).strip()
            clean = re.sub('\s*\([^)]*\)$', '', clean)
            
            if clean and 'COMPLETE DESIGN' not in clean.upper() and 'ADVERTISE' not in clean.upper():
                project_names.append(clean)

# Deduplicate
unique_projects = list(set(project_names))

# Count matches with funding data
county = 0
for proj in unique_projects:
    for fund in funding_lookup.keys():
        if proj == fund or fund.startswith(proj + ' '):
            county += 1
            break

print('__RESULT__:', county)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
