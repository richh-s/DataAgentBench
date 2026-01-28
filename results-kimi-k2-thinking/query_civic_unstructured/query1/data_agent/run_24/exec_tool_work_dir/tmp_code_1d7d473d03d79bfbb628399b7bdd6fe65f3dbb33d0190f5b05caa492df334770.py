code = """import json

# Access the stored file paths correctly
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:5']

# Load the funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Filter funding records for Amount > 50000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

funding_project_names = set(r['Project_Name'] for r in high_funding)

# Step 2: Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Extract design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        
        # Extract project names (non-empty lines that aren't markers)
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                # Skip metadata headers
                if 'To:' not in line and 'From:' not in line and 'Date:' not in line:
                    if 'Subject:' not in line and 'RECOMMENDED' not in line:
                        if len(line) > 5:
                            design_projects.append(line)

# Remove duplicates
unique_design_projects = list(set(design_projects))

# Step 3: Count matches with funding records
matched_count = 0

for design_project in unique_design_projects:
    for funding_record in high_funding:
        funding_name = funding_record['Project_Name']
        if design_project == funding_name or funding_name.startswith(design_project + ' '):
            matched_count += 1
            break

# Output in required format
result = json.dumps(matched_count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
