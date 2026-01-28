code = """import json
import re

# Load funding data (this should be a list)
funding_data = locals()['var_functions.query_db:32']
print('Funding data loaded, type:', type(funding_data))
print('Funding records count:', len(funding_data))

# Load civic data (might be a file path)
civic_var = locals()['var_functions.query_db:6']
print('Civic var type:', type(civic_var))

if isinstance(civic_var, str) and civic_var.endswith('.json'):
    with open(civic_var, 'r') as f:
        civic_data = json.load(f)
    print('Loaded civic data from file')
else:
    civic_data = civic_var
    print('Using civic data directly')

print('Civic documents count:', len(civic_data))
print('First doc sample:', list(civic_data[0].keys()))

# Create funding lookup by project name
funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    
    # Also store without suffixes
    if ' (FEMA' in name:
        base = name.split(' (FEMA')[0]
        funding_lookup[base] = amount
    elif ' (Cal' in name:
        base = name.split(' (Cal')[0]
        funding_lookup[base] = amount

print('Funding lookup created with', len(funding_lookup), 'entries')

# Find capital projects in design status
design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Extract the design section
        start = text.find('Capital Improvement Projects (Design)')
        subsection = text[start:]
        
        # Find end of section
        end_pos = len(subsection)
        for marker in ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects']:
            pos = subsection.find(marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos
        
        design_section = subsection[:end_pos]
        
        # Look for project names (simple approach)
        for line in design_section.split('\n'):
            line = line.strip()
            # Skip lines that are too short or look like metadata
            if len(line) < 10 or line.startswith('(') or line.startswith('•') or 'Updates:' in line:
                continue
            if 'Project Schedule:' in line or 'Design:' in line or 'Advertise:' in line:
                continue
            
            # Clean the line
            clean_name = line.strip()
            while clean_name.endswith(('.', ':', ';', ',')):
                clean_name = clean_name[:-1]
            
            # Check if in funding lookup
            if clean_name in funding_lookup:
                amount = funding_lookup[clean_name]
                if amount > 50000:
                    design_projects.add((clean_name, amount))

print('Found', len(design_projects), 'design projects with funding > $50,000')
result = len(design_projects)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
