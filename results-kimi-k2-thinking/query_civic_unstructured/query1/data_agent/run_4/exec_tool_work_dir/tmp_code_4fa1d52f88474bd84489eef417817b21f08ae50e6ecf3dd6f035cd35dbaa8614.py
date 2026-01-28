code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding dict for projects > $50,000  
funding_dict = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        proj_name = item['Project_Name'].strip()
        funding_dict[proj_name] = amount

# Find capital design projects in civic docs
design_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if we are entering design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design_section = True
            continue
            
        # Exit design section when hitting other sections
        if in_design_section:
            if (line.startswith('Capital') and 'Construction' in line) or \
               (line.startswith('Capital') and 'Not Started' in line) or \
               line.startswith('DISASTER') or \
               'DISASTER RECOVERY' in line.upper():
                in_design_section = False
                continue
                
        # Capture project names in design section
        if in_design_section and line and len(line) > 5:
            # Skip metadata lines
            if any(keyword in line for keyword in ['Updates:', 'Schedule:', 'COMPLETE DESIGN', 'ADVERTISE', 'BEGIN CONSTRUCTION', 'cid:', 'Page', 'Agenda']):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
            if any(season in line for season in ['Spring', 'Summer', 'Fall', 'Winter']):
                continue
                
            # Clean and add project name
            clean_name = re.sub('\s+', ' ', line).strip()
            clean_name = re.sub('\s*\([^)]*\)$', '', clean_name)
            
            if clean_name and clean_name not in ['RECOMMENDED ACTION', 'DISCUSSION']:
                design_project_names.append(clean_name)

# Remove duplicates
unique_design = list(set(design_project_names))

# Match with funding data
matched_count = 0
for design_name in unique_design:
    for fund_name in funding_dict.keys():
        if design_name == fund_name or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            matched_count += 1
            break

print('__RESULT__:', matched_count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
