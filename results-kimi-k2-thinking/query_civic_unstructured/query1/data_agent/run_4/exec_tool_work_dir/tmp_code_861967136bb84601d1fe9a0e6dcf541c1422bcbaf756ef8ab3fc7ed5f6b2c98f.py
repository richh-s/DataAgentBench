code = """import json
import re

# Load data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name'].strip()] = amount

# Extract capital design projects from civic documents
design_project_set = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_capital_design = False
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 6:
            continue
            
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_capital_design = True
            continue
            
        if in_capital_design and (line.startswith('Capital') or line.startswith('DISASTER')):
            in_capital_design = False
            continue
            
        if in_capital_design:
            skip_line = False
            if line.startswith('(') or line.startswith('cid:'):
                skip_line = True
            if 'Updates:' in line or 'Schedule:' in line or 'Page' in line or 'Agenda' in line:
                skip_line = True
            if line.startswith('Staff') or line.startswith('City'):
                skip_line = True
            if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                skip_line = True
            if 'COMPLETE DESIGN' in line.upper():
                skip_line = True
                
            if not skip_line:
                clean_name = re.sub(r'\s+', ' ', line).strip()
                clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
                if clean_name and len(clean_name) > 5:
                    design_project_set.add(clean_name)

# Count projects with funding > $50,000
matched_count = 0
for design_name in design_project_set:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matched_count += 1
            break

result = str(matched_count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
