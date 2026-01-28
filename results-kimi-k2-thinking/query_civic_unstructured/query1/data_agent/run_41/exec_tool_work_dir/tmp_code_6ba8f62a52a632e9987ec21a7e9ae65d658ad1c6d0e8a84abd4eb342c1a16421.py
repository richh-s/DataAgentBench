code = """import json
import re

funding_data = locals()['var_functions.query_db:58']
civic_file = locals()['var_functions.query_db:54']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name] = amount
    base_name = project_name.split(' (')[0]
    funding_lookup[base_name] = amount

# Find capital projects in design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Get text after header
    text_after = text[design_start + 100:]
    
    # Find end of design section
    cons_start = text_after.find('Capital Improvement Projects (Construction)')
    if cons_start > 0:
        design_text = text_after[:cons_start]
    else:
        disaster_start = text_after.find('Disaster Recovery Projects')
        design_text = text_after[:disaster_start] if disaster_start > 0 else text_after[:5000]
    
    # Extract project names
    for line in design_text.split('\n'):
        line = line.strip()
        # Skip metadata
        if (not line or line.startswith('(') or line.startswith('•') or 
            'Updates:' in line or 'Project Schedule:' in line or 'Page' in line):
            continue
        
        # Check length
        if len(line) < 10 or len(line) > 200:
            continue
        
        project_name = line.rstrip('.,:;')
        
        # Check funding
        if project_name in funding_lookup and funding_lookup[project_name] > 50000:
            design_projects.add(project_name)

# Output result
result = len(design_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
