code = """import json, re

# Load data from files
with open(locals()['var_functions.query_db:92']) as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:54']) as f:
    civic_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    proj_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[proj_name] = amount
    # Also store base name after removing parenthetical parts
    if ' (FEMA' in proj_name:
        base = proj_name.split(' (FEMA')[0]
        funding_lookup[base] = amount
    elif ' (Cal' in proj_name:
        base = proj_name.split(' (Cal')[0]
        funding_lookup[base] = amount

# Find capital projects in design status
capital_design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Extract design section (limit to avoid parsing too much)
    design_part = text[design_start + 100:design_start + 5000]
    
    # Find end of design section
    construction_pos = design_part.find('Capital Improvement Projects (Construction)')
    if construction_pos > 0:
        design_part = design_part[:construction_pos]
    
    # Look for project names
    for line in design_part.split('\n'):
        line = line.strip()
        
        # Filter out noise
        if len(line) < 10 or line.startswith('(') or line.startswith('•'):
            continue
        if 'Updates:' in line or 'Project Schedule:' in line or 'Page' in line:
            continue
        
        project_name = line.rstrip('.,:;')
        
        # Check if this project has sufficient funding
        if project_name in funding_lookup:
            if funding_lookup[project_name] > 50000:
                capital_design_projects.add(project_name)

print('__RESULT__:')
print(len(capital_design_projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:82': [{'project_count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json'}

exec(code, env_args)
