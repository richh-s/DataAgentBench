code = """import json

# Load data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding = json.load(f)

c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    docs = json.load(f)

# Build funding lookup for > $50k
funding_lookup = {}
for item in funding:
    if int(item['Amount']) > 50000:
        funding_lookup[item['Project_Name'].strip()] = int(item['Amount'])

# Extract design projects
design_list = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_capital_design = False
    
    for line in lines:
        line = line.strip()
        
        # Check for design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_capital_design = True
            continue
            
        # End of section
        if in_capital_design:
            if line.startswith('Capital'):
                if 'Construction' in line or 'Not Started' in line:
                    in_capital_design = False
                    continue
            if line.startswith('DISASTER'):
                in_capital_design = False
                continue
                
        # Get project names
        if in_capital_design and line and len(line) > 5:
            # Skip metadata
            skip_words = ['Updates', 'Schedule', 'cid:', 'Page', 'Staff', 'City', 'RECOMMENDED', 'DISCUSSION']
            if any(w in line for w in skip_words):
                continue
                
            # Clean name
            import re
            clean = re.sub(r'\s+', ' ', line).strip()
            clean = re.sub(r'\s*\([^)]*\)$', '', clean)
            
            if clean and 'COMPLETE DESIGN' not in clean.upper() and 'COMPLETE' not in clean.upper() and 'ADVERTISE' not in clean.upper():
                design_list.append(clean)

# Count unique projects with funding
design_set = set(design_list)
count = 0

for design_name in design_set:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            count += 1
            break

print('__RESULT__:', count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
