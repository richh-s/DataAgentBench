code = """import json
import re

# Load datasets from files
with open(locals()['var_functions.query_db:92']) as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:54']) as f:
    civic_data = json.load(f)

# Build funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    proj_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[proj_name] = amount
    # Also store base name without suffixes
    base_name = proj_name.split(' (')[0]
    funding_lookup[base_name] = amount

# Find capital projects with design status
found_projects = set()

design_header = 'Capital Improvement Projects (Design)'
construction_header = 'Capital Improvement Projects (Construction)'

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find position of design section
    design_pos = text.find(design_header)
    if design_pos < 0:
        continue
    
    # Get a reasonable chunk after the header
    design_section = text[design_pos + len(design_header): design_pos + 5000]
    
    # Find construction section within this chunk to limit scope
    cons_pos = design_section.find(construction_header)
    if cons_pos > 0:
        design_section = design_section[:cons_pos]
    
    # Try to extract project names using a simple pattern
    # Look for title case headings that are not metadata
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        
        # Skip short lines and metadata
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('◦'):
            continue
        if 'Updates:' in line or 'Project Schedule:' in line:
            continue
        if 'Page' in line or 'Agenda Item' in line:
            continue
        if line.isupper():  # Skip all caps lines
            continue
            
        # Clean up the project name
        project_name = line.rstrip('.,:;')
        
        # Check if this project has funding > $50,000
        if project_name in funding_lookup and funding_lookup[project_name] > 50000:
            found_projects.add(project_name)

# Output final count
print('__RESULT__:')
print(len(found_projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:82': [{'project_count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json'}

exec(code, env_args)
