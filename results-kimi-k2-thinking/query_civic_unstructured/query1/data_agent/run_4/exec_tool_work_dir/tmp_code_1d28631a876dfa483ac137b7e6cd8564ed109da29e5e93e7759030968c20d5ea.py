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
funding_projects = {}
for item in funding_data:
    if int(item['Amount']) > 50000:
        funding_projects[item['Project_Name'].strip()] = int(item['Amount'])

# Find capital design projects
print('Extracting capital design projects from documents...')

design_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' not in text:
        continue
        
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check for design section header
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design_section = True
            continue
            
        # Check for section end
        if in_design_section:
            if line.startswith('Capital') and ('Construction' in line or 'Not Started' in line):
                in_design_section = False
                continue
            if line.startswith('DISASTER'):
                in_design_section = False
                continue
                
        # Extract project names
        if in_design_section and line and len(line) > 5 and len(line) < 150:
            # Skip metadata
            if any(x in line for x in ['Updates:', 'Schedule:', 'cid:', 'Page', 'Agenda']):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
                
            # Check for season/year lines to skip
            if re.search('Spring|Summer|Fall|Winter', line):
                continue
                
            clean_name = re.sub('\s+', ' ', line).strip()
            # Remove parenthetical suffixes
            clean_name = re.sub('\s*\([^)]*\)$', '', clean_name)
            
            if clean_name and 'COMPLETE DESIGN' not in clean_name.upper():
                design_names.append(clean_name)

# Deduplicate
design_names = list(set(design_names))
print(f'Found {len(design_names)} design projects')

# Match with funding
matched = 0
for design_name in design_names:
    for fund_name in funding_projects.keys():
        if design_name == fund_name:
            matched += 1
            break
        elif fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matched += 1
            break

print('__RESULT__:', matched)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
