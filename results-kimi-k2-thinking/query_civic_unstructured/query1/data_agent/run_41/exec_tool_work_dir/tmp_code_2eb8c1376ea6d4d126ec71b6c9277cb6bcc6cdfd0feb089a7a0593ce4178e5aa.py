code = """import json
import re

# Load data
funding_data = locals()['var_functions.query_db:32']
civic_path = locals()['var_functions.query_db:6']

# Read civic documents from file
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    
    # Add base name without suffix
    base_name = name.split(' (')[0]
    funding_lookup[base_name] = amount

# Find design section and extract project names
design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        design_section = text[design_start:design_start+5000]  # Limit section size
        
        # Find end markers
        construction_start = design_section.find('Capital Improvement Projects (Construction)')
        if construction_start > 0:
            design_section = design_section[:construction_start]
        
        disaster_start = design_section.find('Disaster Recovery Projects')
        if disaster_start > 0:
            design_section = design_section[:disaster_start]
        
        # Look for project names in the section
        for line in design_section.split('\n'):
            line = line.strip()
            # Skip short or metadata lines
            if len(line) < 10:
                continue
            if line.startswith('(') or line.startswith('•') or 'Updates:' in line:
                continue
            if 'Project Schedule:' in line or 'Complete Design:' in line:
                continue
            
            # Clean name
            clean_name = line.rstrip('.,:;')
            
            # Check funding
            if clean_name in funding_lookup:
                amount = funding_lookup[clean_name]
                if amount > 50000:
                    design_projects.add((clean_name, amount))

# Output count
result = len(design_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
