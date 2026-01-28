code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name'].strip()] = amount

# Extract capital projects with design status
print('Processing documents to extract design projects...')

design_project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Detect capital design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design_section = True
            continue
            
        # Exit conditions for design section
        if in_design_section:
            if line.startswith('Capital') or line.startswith('DISASTER'):
                section_check = line.split(' ')
                if len(section_check) > 2:
                    for word in section_check:
                        if 'Construction' in word or 'Not' in word:
                            in_design_section = False
                            break
                if 'DISASTER' in line:
                    in_design_section = False
                    continue
                    
        # Extract project names within design section
        if in_design_section and line and len(line) > 5:
            # Skip metadata and non-project lines
            metadata_terms = ['Updates:', 'Schedule:', 'Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION']
            if any(term in line for term in metadata_terms):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if re.search('Spring|Summer|Fall|Winter', line):
                continue
                
            # Clean and normalize project name
            clean_name = re.sub(r'\s+', ' ', line).strip()
            clean_name = re.sub(r'\s*\([^)]*\)$', '', clean_name)
            
            # Validate it's a project name (not a status line)
            if clean_name and 'COMPLETE DESIGN' not in clean_name.upper() and 'ADVERTISE' not in clean_name.upper():
                if 5 < len(clean_name) < 150:
                    design_project_names.add(clean_name)

# Match design projects with funding data
matched_count = 0
for design_name in design_project_names:
    for fund_name in funding_lookup.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matched_count += 1
            break

print(f'Final count of capital design projects with >$50k funding: {matched_count}')
print('__RESULT__:', matched_count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
