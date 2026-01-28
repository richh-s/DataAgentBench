code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:70']
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic documents data
civic_file = locals()['var_functions.query_db:54']
with open(civic_file) as f:
    civic_data = json.load(f)

# Build funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name] = amount
    # Also add base name without parenthetical suffix
    base_name = project_name.split(' (')[0]
    funding_lookup[base_name] = amount

# Find capital projects in design status
found_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section start
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Get text from after design header
    design_section = text[design_start + 100:]
    
    # Find where construction section starts to limit our search
    construction_start = design_section.find('Capital Improvement Projects (Construction)')
    if construction_start > 0:
        design_section = design_section[:construction_start]
    
    # Extract lines that might be project names
    for line in design_section.split('\n'):
        line = line.strip()
        
        # Skip metadata and short lines
        if len(line) < 10 or line.startswith('(') or line.startswith('•'):
            continue
        if 'Updates:' in line or 'Schedule:' in line or 'Page' in line:
            continue
        
        # Clean project name
        project_name = line.rstrip('.,:;')
        
        # Check if it's a capital project with funding > 50000
        if project_name in funding_lookup and funding_lookup[project_name] > 50000:
            found_projects.add(project_name)

result_count = len(found_projects)
print('__RESULT__:')
print(result_count)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
