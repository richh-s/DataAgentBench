code = """import json, re

f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding = json.load(f)

c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    docs = json.load(f)

# Funding lookup for >$50k projects
high_funding = {}
for item in funding:
    if int(item['Amount']) > 50000:
        name = item['Project_Name'].strip()
        high_funding[name] = int(item['Amount'])

# Extract capital design projects
design_set = set()

for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 6:
            continue
        
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
        if in_design and (line.startswith('Capital') or line.startswith('DISASTER')):
            in_design = False
            continue
        
        if in_design:
            # Skip metadata
            if line.startswith('Updates:') or line.startswith('Schedule:') or line.startswith('Page') or line.startswith('Agenda'):
                continue
            if line.startswith('Staff ') or line.startswith('City '):
                continue
            if 'COMPLETE DESIGN' in line or 'ADVERTISE' in line:
                continue
            if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                continue
            
            # Clean name
            clean_name = re.sub(r'\s+', ' ', line).strip()
            clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
            
            if clean_name and len(clean_name) > 5:
                design_set.add(clean_name)

# Count matches
matches = 0
for design_name in design_set:
    for fund_name in high_funding.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matches += 1
            break

print('__RESULT__:')
print(str(matches))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
