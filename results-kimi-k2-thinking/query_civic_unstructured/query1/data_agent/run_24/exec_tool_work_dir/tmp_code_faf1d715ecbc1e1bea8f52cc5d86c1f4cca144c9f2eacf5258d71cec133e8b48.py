code = """import json

# Load funding data from file path stored in variable
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents from file path stored in variable
civic_path = locals()['var_functions.query_db:64']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Step 1: Filter funding for amounts greater than $50,000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

funding_names = [r['Project_Name'] for r in high_funding]

# Step 2: Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Look for design section
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Split text to get design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        
        # Find project names (lines that aren't metadata or markers)
        lines = design_section.split('\n')
        for line in lines:
            line_stripped = line.strip()
            if line_stripped and not line_stripped.startswith('('):
                if not line_stripped.startswith('Capital'):
                    if 'To:' not in line and 'From:' not in line and 'Date' not in line:
                        if 'Subject:' not in line and 'RECOMMENDED' not in line:
                            if len(line_stripped) > 5 and line_stripped[0].isupper():
                                design_projects.append(line_stripped)

# Remove duplicates
unique_design = list(set(design_projects))

# Step 3: Count matches with funding records
matched_count = 0

for design_name in unique_design:
    for fund_name in funding_names:
        # Check if names match
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            matched_count += 1
            break

# Output the result
print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
