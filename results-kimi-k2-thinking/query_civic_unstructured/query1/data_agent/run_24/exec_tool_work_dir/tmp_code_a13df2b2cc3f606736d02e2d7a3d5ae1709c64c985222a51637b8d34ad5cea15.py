code = """import json

# Get the file paths from storage
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:5']

# Load funding data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Filter funding records for amount > $50,000
high_funding = []
for record in funding_records:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

# Step 2: Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check for design section
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Get the design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        
        # Split into lines and extract project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and markers
            if not line or line.startswith('('):
                continue
            if line.startswith('Capital Improvement Projects'):
                continue
            # Skip metadata lines
            if 'To:' in line or 'From:' in line or 'Date:' in line or 'Subject:' in line:
                continue
            if 'RECOMMENDED' in line or 'DISCUSSION:' in line:
                continue
            if 'Updates:' in line or 'Project Schedule:' in line or 'Estimated Schedule:' in line:
                continue
            # If line has reasonable length, consider it a project name
            if len(line) > 5:
                design_projects.append(line)

# Remove duplicates
unique_design_projects = list(set(design_projects))

# Step 3: Count matches with high funding records
matched_count = 0
funding_names = [r['Project_Name'] for r in high_funding]

for design_project in unique_design_projects:
    for funding_name in funding_names:
        # Check for exact match or with suffix (e.g., "Project (FEMA Project)")
        if (design_project == funding_name or 
            funding_name.startswith(design_project + ' ') or
            design_project.startswith(funding_name + ' ')):
            matched_count += 1
            break

# Output result
print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
