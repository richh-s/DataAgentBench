code = """import json
import re

funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_docs_path = locals()['var_functions.query_db:8']  
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for >$50k projects
funding_lookup = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name'].strip()] = amt

# Extract capital design projects
design_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    design_section = False
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
            
        if 'Capital Improvement Projects' in line and 'Design' in line:
            design_section = True
            continue
        if design_section:
            if line.startswith('Capital') or line.startswith('DISASTER'):
                design_section = False
                continue
        
        if design_section and len(line) > 5:
            # Skip metadata and status lines
            skip_terms = ['Updates:', 'Schedule:', 'Complete Design', 'Advertise', 'Begin Construction', 'cid:', 'Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION']
            if any(term in line for term in skip_terms):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if re.search('Spring|Summer|Fall|Winter|2022|2023|2024', line):
                continue
                
            # Clean name
            clean_name = re.sub(r'\s+', ' ', line).strip()
            clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
            
            if clean_name and len(clean_name) > 5:
                design_names.add(clean_name)

# Count matches
matches = 0
for design in design_names:
    for fund_name in funding_lookup.keys():
        if design == fund_name or fund_name.startswith(design + ' ') or fund_name.startswith(design + '('):
            matches += 1
            break

print('__RESULT__:', matches)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
