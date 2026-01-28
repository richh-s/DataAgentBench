code = """import json

# Load funding data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name'].strip()] = amount

# Extract capital projects with design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        
        if not line or len(line) < 6:
            continue
        
        # Check for capital design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
        
        # Exit conditions
        if in_design and (line.startswith('Capital') or line.startswith('DISASTER')):
            in_design = False
            continue
        
        # Extract project name
        if in_design:
            # Skip metadata
            if line.startswith('Updates:') or line.startswith('Schedule:') or line.startswith('Page') or line.startswith('Agenda'):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                continue
            
            clean_name = line
            # Remove content in parentheses if present
            if '(' in clean_name:
                clean_name = clean_name.split('(')[0].strip()
            
            if clean_name and len(clean_name) > 5:
                design_projects.add(clean_name)

# Match design projects with funding
matched_count = 0
for design in design_projects:
    for fund_name in funding_lookup.keys():
        if design == fund_name or fund_name.startswith(design + ' '):
            matched_count += 1
            break

result = str(matched_count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
