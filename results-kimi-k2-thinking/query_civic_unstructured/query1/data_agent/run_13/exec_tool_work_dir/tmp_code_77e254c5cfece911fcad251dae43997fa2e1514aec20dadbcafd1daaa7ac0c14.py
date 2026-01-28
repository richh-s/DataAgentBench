code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:0
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

funding_names = [record['Project_Name'] for record in funding_records]

# Load civic documents
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Find capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Find design section
    start = text.find('capital improvement projects (design)')
    if start == -1:
        continue
    
    # Find end of section
    end1 = text.find('capital improvement projects (construction)', start)
    end2 = text.find('capital improvement projects (not started)', start)
    
    end = end1 if end1 != -1 else len(text)
    if end2 != -1 and end2 < end:
        end = end2
    
    section = text[start:end]
    
    # Extract project names
    lines = section.split('\n')
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip update/schedule lines
        if 'updates:' in line or 'schedule:' in line or 'advertise:' in line:
            continue
        if 'staff' in line or 'city' in line or 'project is' in line:
            continue
        if line.startswith('to:') or line.startswith('prepared') or line.startswith('approved'):
            continue
        if line.startswith('date') or line.startswith('meeting') or line.startswith('subject:'):
            continue
        if line.startswith('agenda') or line.startswith('item') or line.startswith('page'):
            continue
        if line.startswith('public works') or line.startswith('commission'):
            continue
        if line.startswith('(cid') or line.startswith('('):
            continue
        
        # Add project name
        proj_name = line.title().strip()
        if proj_name and proj_name not in design_projects:
            design_projects.append(proj_name)

# Match with funding
matched = []

for design_proj in design_projects:
    clean_design = re.sub(r'\s*\([^)]+\)$', '', design_proj).strip().lower()
    
    for fund_proj in funding_names:
        clean_fund = re.sub(r'\s*\([^)]+\)$', '', fund_proj).strip().lower()
        
        if design_proj.lower() == clean_fund or clean_design == clean_fund:
            if design_proj not in matched:
                matched.append(design_proj)
        elif clean_design in clean_fund or clean_fund in clean_design:
            if design_proj not in matched:
                matched.append(design_proj)

# Create result
count = len(matched)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
