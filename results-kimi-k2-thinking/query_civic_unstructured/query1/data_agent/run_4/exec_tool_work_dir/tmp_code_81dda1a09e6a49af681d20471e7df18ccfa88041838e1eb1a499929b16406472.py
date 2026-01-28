code = """import json

# Load the full data sets
f_path = locals()['var_functions.execute_python:2']
c_path = locals()['var_functions.query_db:8']

with open(f_path, 'r') as f:
    funding_all = json.load(f)

with open(c_path, 'r') as f:
    civic_all = json.load(f)

# Build set of funding projects > $50k
funding_names = set()
for item in funding_all:
    if int(item['Amount']) > 50000:
        funding_names.add(item['Project_Name'].strip())

# Extract design project names from all civic docs
all_design = set()

for doc in civic_all:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n') 
    in_capital_design = False
    
    for line in lines:
        line = line.strip()
        
        # Check for design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_capital_design = True
            continue
            
        # Exit conditions
        if in_capital_design and (line.startswith('Capital') or line.startswith('DISASTER')):
            in_capital_design = False
            continue
        
        # Extract project names
        if in_capital_design and line and len(line) > 5:
            # Skip obvious metadata
            if any(x in line for x in ['Updates:', 'Schedule:', 'Page', 'Agenda']):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                continue
            if 'COMPLETE DESIGN' in line.upper():
                continue
            
            # Clean name
            clean_name = line.split('(')[0].strip()
            if clean_name and len(clean_name) > 5:
                all_design.add(clean_name)

# Count matches
count = 0
for design_name in all_design:
    for fund_name in funding_names:
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            count += 1
            break

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7, 'var_functions.execute_python:102': 25}

exec(code, env_args)
