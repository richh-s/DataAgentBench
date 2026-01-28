code = """import json
import re

# Load data
funding_result = locals()['var_functions.query_db:24']
civic_result = locals()['var_functions.query_db:6']

print('Funding records:', len(funding_result))
print('Civic docs:', len(civic_result))

# Build funding lookup
funding_lookup = {}
for item in funding_result:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    
    # Add base names without suffixes
    if ' (FEMA Project)' in name:
        base = name.replace(' (FEMA Project)', '')
        funding_lookup[base] = amount
    elif ' (CalJPIA Project)' in name:
        base = name.replace(' (CalJPIA Project)', '')
        funding_lookup[base] = amount
    elif ' (CalOES Project)' in name:
        base = name.replace(' (CalOES Project)', '')
        funding_lookup[base] = amount
    elif ' (FEMA/CalOES Project)' in name:
        base = name.replace(' (FEMA/CalOES Project)', '')
        funding_lookup[base] = amount

# Scan civic documents for capital projects in design phase
design_projects = set()

for doc in civic_result:
    text = doc.get('text', '')
    
    # Find the design section
    if 'Capital Improvement Projects (Design)' in text:
        # Get the section until next major heading
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            section = section.split('Disaster Recovery Projects')[0]
            
            # Look for project names (lines that are not bullet points and look like titles)
            for line in section.split('\n'):
                line = line.strip()
                if (line and not line.startswith('(') and not line.startswith('•') and 
                    not line.startswith('◦') and not line.startswith('-') and
                    'Updates:' not in line and 'Project Schedule:' not in line and
                    'Complete Design:' not in line and len(line) > 10):
                    
                    # Clean and check
                    proj_name = re.sub('\s+', ' ', line).strip()
                    if proj_name in funding_lookup:
                        amount = funding_lookup[proj_name]
                        if amount > 50000:
                            design_projects.add((proj_name, amount))

print('Found projects:', len(design_projects))
for name, amount in sorted(design_projects):
    print(f'  {name}: ${amount:,}')

result = len(design_projects)
print('__RESULT__:')
print(str(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
