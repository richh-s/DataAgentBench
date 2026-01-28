code = """import json

# Load data from files
with open(locals()['var_functions.query_db:40'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:5'], 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Find capital design projects from civic documents by looking for specific patterns
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Design section and extract project names
    # Project names often appear as separate lines before update sections
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        clean_line = line.strip()
        
        # Start looking when we find the design header
        if 'Capital Improvement Projects (Design)' in clean_line:
            in_design = True
        # Stop when we hit the next major section
        elif 'Capital Improvement Projects (Construction)' in clean_line or 'Disaster Recovery' in clean_line:
            in_design = False
        # Extract project names while in design section
        elif in_design and clean_line:
            # Skip empty lines, update markers, schedule markers
            if (len(clean_line) > 10 and 'Project' in clean_line and 
                'Updates' not in clean_line and 'Schedule' not in clean_line and
                'fema' not in clean_line.lower() and 'disaster' not in clean_line.lower()):
                design_projects.add(clean_line)

# Match with funding data > $50,000
matched = set()

for funding in funding_data:
    amount = int(funding['Amount'])
    if amount > 50000:
        proj_name = funding['Project_Name']
        # Remove suffixes like (FEMA Project)
        if '(' in proj_name:
            base_name = proj_name.split('(')[0].strip()
        else:
            base_name = proj_name
        
        if base_name in design_projects:
            matched.add(base_name)

# Create result dictionary
result_dict = {'count': len(matched)}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
