code = """import json

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Load civic docs
path = locals()['var_functions.query_db:8']
with open(path, 'r') as f:
    docs = json.load(f)

# Build funding set for >$50k
funding_names = set()
for item in funding:
    if int(item['Amount']) > 50000:
        funding_names.add(item['Project_Name'].strip())

# Simple extraction of design projects
capital_design = set()

for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    design_mode = False
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        
        # Detect design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            design_mode = True
            continue
        
        if design_mode and (line.startswith('Capital') or line.startswith('DISASTER')):
            design_mode = False
            continue
        
        if design_mode and len(line) > 6:
            # Skip metadata lines
            if line.startswith('Updates') or line.startswith('Schedule') or line.startswith('Page') or line.startswith('Agenda'):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                continue
            if 'COMPLETE' in line:
                continue
            
            # Clean name
            clean = line.split('(')[0].strip()
            if clean and len(clean) > 5:
                capital_design.add(clean)

# Count matches
matches = 0
for design in capital_design:
    for fund in funding_names:
        if design == fund or fund.startswith(design + ' '):
            matches += 1
            break

print('__RESULT__:')
print(matches)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7, 'var_functions.execute_python:102': 25}

exec(code, env_args)
