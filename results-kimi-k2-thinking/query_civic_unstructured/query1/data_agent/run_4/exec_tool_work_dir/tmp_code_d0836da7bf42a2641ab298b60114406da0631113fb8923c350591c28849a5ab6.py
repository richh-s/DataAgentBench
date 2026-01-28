code = """import json

# Load data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

docs_path = locals()['var_functions.query_db:8']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        name = item['Project_Name'].strip()
        funding_lookup[name] = amount

# Extract capital design projects
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
        
        if in_design:
            if line.startswith('Capital'):
                if 'Construction' in line or 'Not Started' in line:
                    break
            if line.startswith('DISASTER'):
                break
            
            # Skip metadata
            if 'Updates:' in line or 'Schedule:' in line or 'Page' in line or 'Agenda' in line:
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                continue
            
            clean_name = line
            if '(' in clean_name:
                clean_name = clean_name.split('(')[0].strip()
            
            if clean_name and len(clean_name) > 5:
                design_projects.add(clean_name)

# Count matches with funding
matched = 0
for design in design_projects:
    for fund in funding_lookup.keys():
        if design == fund or fund.startswith(design + ' '):
            matched += 1
            break

print('__RESULT__:')
print(str(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
