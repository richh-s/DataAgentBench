code = """import json
import re

# Load data from files
funding_file = locals()['var_functions.query_db:2']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find capital projects with design status from civic documents
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section and extract project names
    if 'Capital Improvement Projects (Design)' in text:
        # Get position of the design section
        start_idx = text.index('Capital Improvement Projects (Design)')
        
        # Find the end of this section (look for next major heading pattern)
        section_text = text[start_idx:]
        
        # Extract lines until we hit a bold heading or double newline
        lines = section_text.split('\n')
        for line in lines[2:]:  # Skip the heading itself
            line = line.strip()
            # Stop if we hit the next section heading
            if 'Capital Improvement Projects (Construction)' in line or 'DISASTER' in line:
                break
            # Skip empty lines or updates
            if not line or any(x in line for x in ['Updates', 'Project Schedule', 'Complete Design', ':']):
                continue
            # Add project names
            if len(line) > 5 and 'Project' in line:
                capital_design_projects.add(line)

# Clean up names and filter for actual capital projects
filtered_projects = set()
for name in capital_design_projects:
    exclude = ['FEMA', 'fema', 'disaster', 'Disaster', 'fire restoration']
    if not any(ex in name for ex in exclude):
        filtered_projects.add(name)

# Match with funding data > $50,000
matched_base_names = set()

for funding in funding_data:
    project_name = funding['Project_Name']
    amount = int(funding['Amount'])
    
    if amount <= 50000:
        continue
    
    # Remove suffixes like (FEMA Project), (CalOES Project), etc.
    base_name = re.sub(r'\s*\([^)]*\)$', '', project_name)
    
    # Check if matches any of our filtered projects
    if base_name in filtered_projects:
        matched_base_names.add(base_name)

final_count = len(matched_base_names)

result = {
    'count': final_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
