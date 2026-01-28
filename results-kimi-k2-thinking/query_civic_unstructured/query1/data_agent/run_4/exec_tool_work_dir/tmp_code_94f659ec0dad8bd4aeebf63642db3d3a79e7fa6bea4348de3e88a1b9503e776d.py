code = """import json

# Load funding data
f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > $50,000
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
    in_section = False
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 6:
            continue
        
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_section = True
            continue
        
        if in_section and (line.startswith('Capital') or line.startswith('DISASTER')):
            in_section = False
            continue
        
        if in_section:
            # Skip metadata
            metadata = ['Updates:', 'Schedule:', 'Page', 'Agenda', 'Staff', 'City', 'Spring', 'Summer', 'Fall', 'Winter', 'COMPLETE DESIGN']
            skip = False
            for term in metadata:
                if term in line:
                    skip = True
                    break
            if skip:
                continue
            
            # Clean name
            clean_name = line
            if '(' in clean_name:
                clean_name = clean_name.split('(')[0].strip()
            
            if clean_name and len(clean_name) > 5:
                design_projects.add(clean_name)

# Count matches
matched = 0
for design in design_projects:
    for fund in funding_lookup.keys():
        if design == fund or fund.startswith(design + ' ') or fund.startswith(design + '('):
            matched += 1
            break

result = str(matched)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
