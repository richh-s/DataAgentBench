code = """import json

f_path = locals()['var_functions.execute_python:2']
c_path = locals()['var_functions.query_db:8']

with open(f_path, 'r') as f:
    funding = json.load(f)

with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for > $50k
funding_lookup = {}
for item in funding:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name'].strip()] = amt

# Extract capital design projects from documents
names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    design_section = False
    
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects' in line and 'Design' in line:
            design_section = True
            continue
            
        if design_section and (line.startswith('Capital') or line.startswith('DISASTER')):
            design_section = False
            continue
        
        if design_section and line and len(line) > 10:
            # Skip metadata lines
            if line.startswith('Updates:') or line.startswith('Schedule:') or line.startswith('Page') or line.startswith('Agenda'):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
                
            # Skip lines with season info
            skip = False
            for season in ['Spring', 'Summer', 'Fall', 'Winter']:
                if season in line:
                    skip = True
                    break
            if skip:
                continue
                
            if 'COMPLETE DESIGN' in line.upper() or 'COMPLETE' in line.upper():
                continue
            
            # Clean name by removing parentheses content
            clean_name = line.split('(')[0].strip()
            if clean_name and len(clean_name) > 5:
                names.add(clean_name)

# Count matches
matched = 0
for name in names:
    for fund_name in funding_lookup.keys():
        if name == fund_name or fund_name.startswith(name + ' ') or fund_name.startswith(name + '('):
            matched += 1
            break

result = str(matched)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7, 'var_functions.execute_python:102': 25}

exec(code, env_args)
