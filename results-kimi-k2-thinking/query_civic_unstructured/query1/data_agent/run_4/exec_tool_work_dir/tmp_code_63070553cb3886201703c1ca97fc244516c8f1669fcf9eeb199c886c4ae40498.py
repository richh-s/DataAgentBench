code = """import json

f_path = locals()['var_functions.execute_python:2']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

c_path = locals()['var_functions.query_db:8']
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for >$50k
funding_lookup = {}
for item in funding_data:
    if int(item['Amount']) > 50000:
        funding_lookup[item['Project_Name'].strip()] = int(item['Amount'])

# Extract design projects
names = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        if len(line) < 6:
            continue
        
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
        
        if in_design and (line.startswith('Capital') or line.startswith('DISASTER')):
            in_design = False
            continue
        
        if in_design:
            skip = False
            skip_terms = ['Updates:', 'Schedule:', 'Page', 'Agenda', 'Staff', 'City', 'Spring', 'Summer', 'Fall', 'Winter']
            for term in skip_terms:
                if term in line:
                    skip = True
                    break
            if skip or 'COMPLETE' in line.upper():
                continue
            
            import re
            clean = re.sub(r'\s+', ' ', line).strip()
            if '(' in clean:
                clean = clean.split('(')[0].strip()
            
            if clean and len(clean) > 5:
                names.append(clean)

design_set = set(names)

# Count matches
matches = 0
for design in design_set:
    for fund in funding_lookup.keys():
        if design == fund or fund.startswith(design + ' '):
            matches += 1
            break

result = str(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
