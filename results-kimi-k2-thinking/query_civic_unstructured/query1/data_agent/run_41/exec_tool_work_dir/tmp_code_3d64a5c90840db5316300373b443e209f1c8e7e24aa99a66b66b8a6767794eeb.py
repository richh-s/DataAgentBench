code = """import json
import re

# Load datasets
funding_file = locals()['var_functions.query_db:70']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = locals()['var_functions.query_db:54']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name] = amount
    base_name = project_name.split(' (')[0]
    funding_lookup[base_name] = amount

# Extract capital projects in design status from civic documents
found_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    design_pos = text.find('Capital Improvement Projects (Design)')
    if design_pos < 0:
        continue
    
    # Get design section
    design_text = text[design_pos+100:]  # Skip the header
    construction_pos = design_text.find('Capital Improvement Projects (Construction)')
    if construction_pos > 0:
        design_text = design_text[:construction_pos]
    
    # Extract project names
    for line in design_text.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('◦'):
            continue
        if 'Updates:' in line or 'Project Schedule:' in line or 'Complete Design:' in line:
            continue
        if 'Page' in line or 'Agenda Item' in line:
            continue
        
        project_name = line.rstrip('.,:;')
        if project_name in funding_lookup and funding_lookup[project_name] > 50000:
            found_projects.add(project_name)

# Output the count
print('__RESULT__:')
print(str(len(found_projects)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
