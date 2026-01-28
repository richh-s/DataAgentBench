code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:64']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Step 1: Filter funding records for amount > 50000
funding_over_50k = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        funding_over_50k.append(record)

# Step 2: Parse civic documents to find capital projects in design status
design_projects = []

for doc in civic_data:
    full_text = doc.get('text', '')
    
    # Check if document contains the design section
    if '(Design)' in full_text and 'Capital Improvement Projects' in full_text:
        # Split into sections
        sections = full_text.split('\n')
        in_design_section = False
        
        for line in sections:
            line = line.strip()
            
            # Detect start of design section
            if 'Capital Improvement Projects (Design)' in line:
                in_design_section = True
                continue
                
            # Detect end of design section  
            if in_design_section and 'Capital Improvement Projects (' in line and 'Design' not in line:
                break
                
            # Extract project names (non-empty, not special markers)
            if in_design_section and line:
                # Skip metadata and markers
                if not line.startswith('(') and not line.startswith('Capital'):
                    if 'To:' not in line and 'From:' not in line and 'Date' not in line:
                        if 'Subject:' not in line and 'RECOMMENDED' not in line:
                            if 'Updates:' not in line and 'Project Schedule:' not in line:
                                if len(line) > 5 and line[0].isupper():
                                    design_projects.append(line)

# Remove duplicates
unique_design = list(set(design_projects))

# Step 3: Count matches with funding
matched = 0
funding_names = set(r['Project_Name'] for r in funding_over_50k)

for design_name in unique_design:
    for fund_name in funding_names:
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
