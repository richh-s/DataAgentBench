code = """import json
import re

# Read funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as file:
    funding_data = json.load(file)

# Read civic documents
civic_path = locals()['var_functions.query_db:5']
with open(civic_path, 'r') as file:
    civic_docs = json.load(file)

# Step 1: Get funding records with amount > $50,000
high_funding_records = []
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_records.append(record)

# Step 2: Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    design_section = text[design_start:]
    
    # Find where design section ends (next capital section)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'DISCUSSION:']:
        marker_pos = design_section.find(marker)
        if marker_pos > 0:
            design_section = design_section[:marker_pos]
            break
    
    # Extract project names from this section
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        # Skip empty lines and markers
        if not line or line.startswith('(') or line.startswith('Capital Improvement Projects'):
            continue
        # Skip metadata
        if any(keyword in line for keyword in ['To:', 'From:', 'Date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION']):
            continue
        # Skip update markers
        if any(marker in line for marker in ['Updates:', 'Project Schedule:', 'Estimated Schedule:']):
            continue
        # If passes all filters, it's a project name
        if len(line) > 5:
            design_capital_projects.append(line)

# Remove duplicates
unique_design_projects = list(set(design_capital_projects))

# Step 3: Count matches
matched_count = 0
matched_projects = []

funding_project_names = [r['Project_Name'] for r in high_funding_records]

for design_project in unique_design_projects:
    for funding_name in funding_project_names:
        # Check if design project name matches funding name (exact or with suffix)
        if design_project == funding_name or funding_name.startswith(design_project + ' '):
            matched_count += 1
            matched_projects.append(design_project)
            break

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
