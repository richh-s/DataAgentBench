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
        name = item['Project_Name'].strip()
        funding_lookup[name] = amount

# Extract capital projects with design status from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Split into lines
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check if entering capital design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design_section = True
            continue
        
        # Check if exiting the section
        if in_design_section and line.startswith('Capital'):
            if 'Construction' in line or 'Not Started' in line:
                in_design_section = False
                continue
        
        if in_design_section and line.startswith('DISASTER'):
            in_design_section = False
            continue
        
        # Extract project names
        if in_design_section and line and len(line) > 5 and len(line) < 150:
            # Skip metadata lines
            if 'Updates:' in line or 'Schedule:' in line or 'Page' in line or 'Agenda' in line:
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                continue
            if 'COMPLETE DESIGN' in line.upper():
                continue
            if line.startswith('(') or line.startswith('RECOMMENDED') or line.startswith('DISCUSSION'):
                continue
            
            # Clean the name (remove content in parentheses and extra spaces)
            clean_name = line
            if '(' in clean_name:
                clean_name = clean_name.split('(')[0].strip()
            clean_name = clean_name.strip()
            
            if clean_name:
                design_projects.add(clean_name)

# Match design projects with funding data and count
matched_count = 0
for design_name in design_projects:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name:
            matched_count += 1
            break
        elif fund_name.startswith(design_name + ' '):
            matched_count += 1
            break
        elif fund_name.startswith(design_name + '('):
            matched_count += 1
            break

result = str(matched_count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
