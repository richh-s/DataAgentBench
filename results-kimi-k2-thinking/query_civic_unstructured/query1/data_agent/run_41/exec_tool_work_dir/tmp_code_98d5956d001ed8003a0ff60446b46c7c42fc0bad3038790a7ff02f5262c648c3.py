code = """import json
import re

# Load funding data from file
funding_file = locals()['var_functions.query_db:84']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents from file  
civic_file = locals()['var_functions.query_db:54']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name] = amount
    
    # Also store base name without suffixes for matching
    base_name = project_name.split(' (')[0]
    funding_lookup[base_name] = amount

# Find all capital projects with design status and funding > 50000
design_capital_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Extract design section (up to next major section)
    design_section = text[design_start + 100:]  # Skip header
    
    # Find end of design section
    construction_start = design_section.find('Capital Improvement Projects (Construction)')
    disaster_start = design_section.find('Disaster Recovery Projects')
    
    end_pos = len(design_section)
    if construction_start > 0:
        end_pos = min(end_pos, construction_start)
    if disaster_start > 0:
        end_pos = min(end_pos, disaster_start)
    
    design_section = design_section[:end_pos]
    
    # Extract project names - look for title case lines that are not metadata
    for line in design_section.split('\n'):
        line = line.strip()
        
        # Skip empty lines and obvious metadata
        if (not line or 
            line.startswith('(') or 
            line.startswith('•') or 
            line.startswith('◦') or
            line.startswith('-') or
            'Updates:' in line or 
            'Project Schedule:' in line or 
            'Complete Design:' in line or
            'Advertise:' in line or
            'Begin Construction:' in line or
            'Page' in line or
            'Agenda Item' in line):
            continue
        
        # Project names should be reasonable length and contain mixed case
        if len(line) < 10 or len(line) > 200:
            continue
        
        # Clean project name
        project_name = line.rstrip('.,:;')
        
        # Check if this project has funding > 50000
        if project_name in funding_lookup and funding_lookup[project_name] > 50000:
            design_capital_projects.add(project_name)

# Output the final count
result = len(design_capital_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:82': [{'project_count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
