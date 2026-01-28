code = """import json
import re

# Load funding data with projects > $50,000
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup for projects > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        proj_name = item['Project_Name'].strip()
        funding_lookup[proj_name] = amount

# Track design projects found
design_projects = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_capital_design = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Detect capital design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_capital_design = True
            continue
            
        # Exit design section when hitting other sections
        if in_capital_design:
            if line.startswith('Capital') and 'Construction' in line:
                in_capital_design = False
                continue
            if line.startswith('DISASTER'):
                in_capital_design = False
                continue
            if 'PROJECTS (Construction)' in line.upper():
                in_capital_design = False
                continue
                
        # Extract project names in design section
        if in_capital_design and line and len(line) > 5:
            # Skip metadata lines
            skip_terms = ['Updates:', 'Schedule:', 'Complete Design', 'Advertise:', 'Begin Construction', 'Staff', 'City', 'RECOMMENDED', 'DISCUSSION', 'Page', 'Agenda', 'Item', 'cid:', '(cid:', 'Spring', 'Summer', 'Fall', 'Winter']
            if any(term in line for term in skip_terms):
                continue
                
            # Skip lines that look like dates or phases
            if re.search(r'(Spring|Summer|Fall|Winter)\s*(202\d)', line):
                continue
            if re.match(r'^(Complete|Advertise|Begin)\s*:', line):
                continue
                
            # Clean up project name
            clean_name = re.sub(r'\(.*\)$', '', line).strip()
            if clean_name and 5 < len(clean_name) < 150:
                design_projects.append(clean_name)

# Remove duplicates
design_projects = list(set(design_projects))

# Match with funding data
capital_design_count = 0
matches = []

for design_proj in design_projects:
    for fund_proj in funding_lookup.keys():
        # Check if design project matches funding project
        if design_proj == fund_proj or fund_proj.startswith(design_proj + ' '):
            capital_design_count += 1
            matches.append((design_proj, funding_lookup[fund_proj]))
            break

# Show some matches for debugging
print('Matches found:')
for m in matches[:10]:
    print(f'  {m[0]}: ${m[1]:,}')

print(f'__RESULT__: {capital_design_count}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
