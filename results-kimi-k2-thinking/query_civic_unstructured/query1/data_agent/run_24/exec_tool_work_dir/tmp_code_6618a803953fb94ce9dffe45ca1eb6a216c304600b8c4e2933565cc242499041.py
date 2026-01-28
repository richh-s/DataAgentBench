code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as file:
    funding_data = json.load(file)

# Load civic documents
civic_path = locals()['var_functions.query_db:64']  
with open(civic_path, 'r') as file:
    civic_docs = json.load(file)

# Step 1: Get funding records with Amount > 50000
high_funding = [r for r in funding_data if int(r['Amount']) > 50000]

# Step 2: Extract capital projects in design phase from civic documents
design_project_names = []

for doc in civic_docs:
    full_text = doc.get('text', '')
    
    # Find the design section
    if 'Capital Improvement Projects (Design)' in full_text:
        # Get the part after the design header
        parts = full_text.split('Capital Improvement Projects (Design)', 1)
        if len(parts) > 1:
            design_section = parts[1]
            
            # Split into lines
            lines = design_section.split('\n')
            for line in lines:
                line = line.strip()
                # Skip empty, metadata and marker lines
                if not line or line.startswith('(') or line.startswith('Capital'):
                    continue
                if any(x in line for x in ['To:', 'From:', 'Date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION']):
                    continue  
                if any(marker in line for marker in ['Updates:', 'Project Schedule:', 'Estimated Schedule:']):
                    continue
                # Valid project names typically start with capital letter and have reasonable length
                if len(line) > 5 and line[0].isupper():
                    design_project_names.append(line)

# Remove duplicates
unique_design = list(set(design_project_names))

# Step 3: Count matches with funding data
funding_names = set(r['Project_Name'] for r in high_funding)
matched_count = 0

for design_name in unique_design:
    for fund_name in funding_names:
        # Check exact match or funding name starting with design name (for suffixes like (FEMA Project))
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            matched_count += 1
            break

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
