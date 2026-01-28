code = """import json

# Load the funding data
funding_data = json.load(open(locals()['var_functions.query_db:6']))

# Load the civic documents
civic_data = json.load(open(locals()['var_functions.query_db:64']))

# Step 1: Get funding records with amount > 50000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

funding_names = set(r['Project_Name'] for r in high_funding)

# Step 2: Extract design capital projects from civic documents
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Split into parts and get the design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        
        # Extract lines
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and marker lines
            if not line or line.startswith('(') or line.startswith('Capital Improvement'):
                continue
            # Skip metadata
            if any(x in line for x in ['To:', 'From:', 'Date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:']):
                continue
            # Valid project names are at least 5 chars and likely start uppercase or include spaces
            if len(line) > 5 and line[0].isalpha():
                design_projects.append(line)

# Remove duplicates
unique_design = list(set(design_projects))

# Step 3: Count matches
matched = 0
for proj in unique_design:
    for fund_proj_name in funding_names:
        # Check if project name matches (exact or with suffix like (FEMA Project))
        if proj == fund_proj_name or fund_proj_name.startswith(proj + ' '):
            matched += 1
            break

# Output the result
print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
