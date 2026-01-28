code = """import json, re

# Load data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding = json.load(f)

civic_path = locals()['var_functions.query_db:8']
with open(civic_path, 'r') as f:
    docs = json.load(f)

# Build funding set for > $50k projects
funding_names = set()
for item in funding:
    if int(item['Amount']) > 50000:
        funding_names.add(item['Project_Name'].strip())

# Extract capital design projects from civic documents
design_projects = set()

for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Parse line by line
    lines = text.split('NEWLINE_PLACEHOLDER_REPLACED')
    in_design_section = False
    
    for line in text.splitlines():
        line = line.strip()
        
        if not line or len(line) < 6:
            continue
        
        # Check for capital design section
        if 'Capital Improvement' in line and 'Design' in line:
            in_design_section = True
            continue
        
        # Check for section end
        if in_design_section:
            first_word = line.split()[0] if line.split() else ''
            if first_word == 'Capital' or first_word == 'DISASTER':
                in_design_section = False
                continue
        
        # Extract project names
        if in_design_section:
            # Skip metadata
            if any(word in line for word in ['Updates', 'Schedule', 'Page', 'Agenda', 'Staff', 'City']):
                continue
            if any(season in line for season in ['Spring', 'Summer', 'Fall', 'Winter']):
                continue
            if 'COMPLETE' in line:
                continue
            
            # Clean name
            clean_name = line.split('(')[0].strip()
            if clean_name and len(clean_name) > 5:
                design_projects.add(clean_name)

# Count design projects that have funding > $50,000
count = 0
for design in design_projects:
    for fund_name in funding_names:
        if design == fund_name or fund_name.startswith(design + ' '):
            count += 1
            break

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7, 'var_functions.execute_python:102': 25}

exec(code, env_args)
