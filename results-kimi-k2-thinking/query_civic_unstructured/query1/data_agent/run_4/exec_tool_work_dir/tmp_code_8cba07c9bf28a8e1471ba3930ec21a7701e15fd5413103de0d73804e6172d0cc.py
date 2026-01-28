code = """import json

# Load data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for >$50k
funding_projects = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_projects[item['Project_Name'].strip()] = amount

# Extract design projects - simple heuristic
design_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    in_section = False
    
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_section = True
            continue
        
        if in_section and line.startswith('Capital') or line.startswith('DISASTER'):
            in_section = False
            continue
        
        if in_section and line and len(line) > 10:
            # Skip metadata by simple checks
            if line.startswith('Updates:') or line.startswith('Schedule:') or line.startswith('Page') or line.startswith('Agenda'):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            
            # Skip if contains seasons or dates
            skip = False
            for season in ['Spring', 'Summer', 'Fall', 'Winter']:
                if season in line:
                    skip = True
                    break
            if skip:
                continue
            
            if 'COMPLETE DESIGN' in line.upper():
                continue
            
            clean_name = line
            if '(' in clean_name:
                clean_name = clean_name.split('(')[0].strip()
            
            if clean_name and len(clean_name) > 5:
                design_names.append(clean_name)

# Count matches
unique_design = set(design_names)
matches = 0

for design_name in unique_design:
    for fund_name in funding_projects.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            matches += 1
            break
        elif fund_name.startswith(design_name + '('):
            matches += 1
            break

result = str(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
