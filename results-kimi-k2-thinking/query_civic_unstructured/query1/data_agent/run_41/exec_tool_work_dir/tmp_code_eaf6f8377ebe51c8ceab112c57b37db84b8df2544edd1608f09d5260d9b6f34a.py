code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:92']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:54']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    proj_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[proj_name] = amount
    # Add base name for matching without suffixes
    base_name = proj_name.split(' (')[0]
    funding_lookup[base_name] = amount

# Find projects in design status
design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section start
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos < 0:
        continue
    
    # Extract design section (limit length to avoid parsing too much)
    design_part = text[design_pos + 100: design_pos + 5000]
    
    # Find construction section to mark end of design section
    cons_pos = design_part.find('Capital Improvement Projects (Construction)')
    if cons_pos > 0:
        design_part = design_part[:cons_pos]
    
    # Check each line for project names
    for line in design_part.split('\n'):
        line = line.strip()
        
        # Skip metadata and short lines
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•'):
            continue
        if 'Updates:' in line or 'Schedule:' in line:
            continue
        if 'Page' in line or 'Agenda' in line:
            continue
        
        # Clean project name
        project_name = line.rstrip('.,:;')
        
        # Check if project has funding > 50000
        if project_name in funding_lookup:
            if funding_lookup[project_name] > 50000:
                design_projects.add(project_name)

# Return the count
print('__RESULT__:')
print(len(design_projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:82': [{'project_count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json'}

exec(code, env_args)
