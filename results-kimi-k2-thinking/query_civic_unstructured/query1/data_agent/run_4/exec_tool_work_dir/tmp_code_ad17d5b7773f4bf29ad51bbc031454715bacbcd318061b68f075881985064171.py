code = """import json

# Load funding data and civic documents
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_path = locals()['var_functions.query_db:8']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create lookup for funding > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        name = item['Project_Name'].strip()
        funding_lookup[name] = amount

# Extract capital projects with design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find capital design sections and extract project names
    sections = text.split('\n\n')
    in_design_section = False
    
    for section in sections:
        if 'Capital Improvement Projects' in section and 'Design' in section:
            in_design_section = True
            # Extract lines from this section
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 5:
                    # Skip metadata lines
                    if line.startswith('Updates:') or line.startswith('Schedule:') or line.startswith('Page') or line.startswith('Agenda'):
                        continue
                    if line.startswith('Staff ') or line.startswith('City '):
                        continue
                    if 'COMPLETE DESIGN' in line.upper() or 'ADVERTISE' in line.upper():
                        continue
                    if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                        continue
                    if line.startswith('Capital Improvement Projects') and 'Design' in line:
                        continue
                    
                    # Clean the name (remove parenthetical content)
                    import re
                    clean_name = re.sub('\s+', ' ', line).strip()
                    clean_name = re.sub('\s*\([^)]*\)$', '', clean_name)
                    
                    if clean_name and len(clean_name) > 5:
                        design_projects.add(clean_name)

# Match design projects with funding data
capital_design_with_funding = 0

for design_name in design_projects:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            capital_design_with_funding += 1
            break

print('RESULT:', capital_design_with_funding)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
