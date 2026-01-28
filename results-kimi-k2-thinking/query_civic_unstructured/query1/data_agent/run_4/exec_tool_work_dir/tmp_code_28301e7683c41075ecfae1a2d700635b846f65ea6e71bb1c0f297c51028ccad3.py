code = """import json

f_path = locals()['var_functions.execute_python:2']
c_path = locals()['var_functions.query_db:8']

with open(f_path, 'r') as f:
    funding = json.load(f)

with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for >$50k
funding_lookup = {}
for item in funding:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name'].strip()] = amount

# Extract design projects from documents
design_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Split section by section
    sections = text.split('\n\n')
    
    for section in sections:
        section = section.strip()
        
        # Check if this is a capital design section
        if 'Capital Improvement Projects' in section and 'Design' in section:
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                if not line or len(line) < 6:
                    continue
                
                # Skip metadata
                if line.startswith('Updates:') or line.startswith('Schedule:') or line.startswith('Page') or line.startswith('Agenda'):
                    continue
                if line.startswith('Staff') or line.startswith('City'):
                    continue
                if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                    continue
                if 'COMPLETE DESIGN' in line.upper() or 'COMPLETE' in line.upper():
                    continue
                
                # Clean name
                clean_name = line.split('(')[0].strip()
                if clean_name and len(clean_name) > 5:
                    design_names.add(clean_name)

# Count matches
counter = 0
for name in design_names:
    for fund_name in funding_lookup.keys():
        if name == fund_name or fund_name.startswith(name + ' '):
            counter += 1
            break

result = str(counter)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7, 'var_functions.execute_python:102': 25}

exec(code, env_args)
