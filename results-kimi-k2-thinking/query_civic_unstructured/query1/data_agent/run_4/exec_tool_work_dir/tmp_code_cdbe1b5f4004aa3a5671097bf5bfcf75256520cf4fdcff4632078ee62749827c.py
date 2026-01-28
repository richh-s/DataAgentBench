code = """import json

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
        funding_lookup[item['Project_Name'].strip()] = amount

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
        
        # Check for capital design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design = True
            continue
        
        # Check for section end
        if in_design and line.startswith('Capital'):
            if 'Construction' in line or 'Not Started' in line:
                break
        
        if in_design and line.startswith('DISASTER'):
            break
        
        # Extract project name
        if in_design:
            # Skip metadata by checking prefixes
            skip = False
            prefixes = ['Updates:', 'Schedule:', 'Page', 'Agenda', 'Staff', 'City', 'Spring', 'Summer', 'Fall', 'Winter', '(cid:', 'RECOMMENDED', 'DISCUSSION']
            for pref in prefixes:
                if line.startswith(pref) or pref in line:
                    skip = True
                    break
            
            if skip or 'COMPLETE DESIGN' in line.upper():
                continue
            
            # Clean name - remove parentheses content
            clean_name = line.strip()
            if '(' in clean_name:
                clean_name = clean_name.split('(')[0].strip()
            
            if clean_name and len(clean_name) > 5:
                design_projects.add(clean_name)

# Match design projects with funding > $50,000
matched_count = 0
for design_name in design_projects:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            matched_count += 1
            break

print('__RESULT__:')
print(str(matched_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
