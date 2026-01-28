code = """import json

# Load data
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Get projects with funding > $50,000
funding_over_50k = []
for record in funding:
    if int(record['Amount']) > 50000:
        funding_over_50k.append(record)

funding_project_names = set(r['Project_Name'] for r in funding_over_50k)

# Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Split and get the design section
    design_parts = text.split('Capital Improvement Projects (Design)')
    if len(design_parts) > 1:
        design_section = design_parts[1]
        
        # Extract project names from the section
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and line markers
            if not line or line.startswith('('):
                continue
            if line.startswith('Capital Improvement Projects'):
                continue
            # Skip metadata lines
            if 'To:' in line or 'From:' in line or 'Date' in line or 'Subject' in line:
                continue
            if 'RECOMMENDED' in line or 'DISCUSSION' in line:
                continue
            # Skip schedule/update markers
            if 'Updates:' in line or 'Project Schedule:' in line:
                continue
            # If line has reasonable length, it's likely a project name
            if len(line) > 5:
                design_capital_projects.append(line)

# Remove duplicates
unique_design_projects = list(set(design_capital_projects))

# Count matches with funding data
matched_count = 0

for design_project in unique_design_projects:
    for funding_record in funding_over_50k:
        funding_name = funding_record['Project_Name']
        # Check for exact match or funding name starting with design project name (for suffixes)
        if design_project == funding_name or funding_name.startswith(design_project + ' '):
            matched_count += 1
            break

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
