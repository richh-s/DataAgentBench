code = """import json
import re

# Load data sources
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup for projects > $50,000
high_funding = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        high_funding[item['Project_Name'].strip()] = amount

# Extract capital projects with design status from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_capital_design = False
    
    for line in lines:
        line = line.strip()
        
        # Detect capital design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_capital_design = True
            continue
        
        # End of section checks
        if in_capital_design:
            if line.startswith('Capital') and ('Construction' in line or 'Not Started' in line):
                in_capital_design = False
                continue
            if line.startswith('DISASTER'):
                break
        
        # Extract project names
        if in_capital_design and line and 5 < len(line) < 150:
            # Skip metadata
            if any(term in line for term in ['Updates:', 'Schedule:', 'Page', 'Agenda', 'cid:', 'RECOMMENDED', 'DISCUSSION']):
                continue
            if line.startswith('Staff') or line.startswith('City') or line.startswith('Complete'):
                continue
                
            # Clean the name
            clean_name = re.sub(r'\s+', ' ', line)
            clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
            clean_name = clean_name.strip()
            
            # Skip phase/date lines
            if re.search('Spring|Summer|Fall|Winter|2022|2023|2024', clean_name):
                continue
            if 'COMPLETE DESIGN' in clean_name.upper() or 'ADVERTISE' in clean_name.upper():
                continue
                
            if clean_name:
                design_projects.add(clean_name)

# Match with funding data
matched_count = 0
for design_name in design_projects:
    for fund_name in high_funding.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matched_count += 1
            break

print('__RESULT__:', matched_count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
