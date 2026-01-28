code = """import json

# Get file paths from storage
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:5']

# Load funding data
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Filter for funding > $50,000
high_funding_records = []
for record in funding_records:
    if int(record['Amount']) > 50000:
        high_funding_records.append(record)

# Step 2: Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if this document has a design section
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Split to get just the design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        
        # Extract lines that are project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines
            if not line:
                continue
            # Skip lines that are markers or metadata
            if line.startswith('(') or line.startswith('Capital Improvement Projects'):
                continue
            if 'To:' in line or 'From:' in line or 'Date:' in line or 'Subject:' in line:
                continue
            if 'RECOMMENDED' in line or 'DISCUSSION:' in line:
                continue
            if 'Updates:' in line or 'Project Schedule:' in line:
                continue
            # If it passes all filters and has reasonable length, it's a project name
            if len(line) > 5:
                design_capital_projects.append(line)

# Remove duplicates
unique_design_projects = list(set(design_capital_projects))

# Step 3: Count matches between design projects and high funding
matched_count = 0

for design_project in unique_design_projects:
    for funding_record in high_funding_records:
        funding_name = funding_record['Project_Name']
        # Match exact name or with suffix/prefix variations
        if (design_project == funding_name or 
            funding_name.startswith(design_project + ' ') or
            design_project.startswith(funding_name + ' ')):
            matched_count += 1
            break

# Return the result as JSON
print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
