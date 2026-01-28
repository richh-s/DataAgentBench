code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
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
    lines = text.split('\n')
    in_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_section = True
            continue
            
        if in_section and (line.startswith('Capital') or line.startswith('DISASTER')):
            in_section = False
            continue
            
        if in_section and len(line) > 5:
            skip = False
            if line.startswith('(') or line.startswith('cid:'):
                skip = True
            if any(x in line for x in ['Updates:', 'Schedule:', 'Page', 'Agenda']):
                skip = True
            if line.startswith('Staff') or line.startswith('City'):
                skip = True
            if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                skip = True
            if 'COMPLETE DESIGN' in line.upper():
                skip = True
                
            if not skip:
                import re
                clean_name = re.sub(r'\s+', ' ', line).strip()
                clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
                if clean_name:
                    design_projects.add(clean_name)

# Count matches
matches = 0
for design_name in design_projects:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matches += 1
            break

result = str(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
