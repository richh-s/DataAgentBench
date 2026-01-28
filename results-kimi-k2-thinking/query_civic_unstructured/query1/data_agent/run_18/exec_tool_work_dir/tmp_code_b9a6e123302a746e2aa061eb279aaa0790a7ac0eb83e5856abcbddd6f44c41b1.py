code = """import json
import re

# Funding data is stored in var_functions.query_db:1
funding_storage = var_functions.query_db:1
if isinstance(funding_storage, str) and funding_storage.endswith('.json'):
    with open(funding_storage, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_storage

# Civic docs data is stored in var_functions.query_db:2  
civic_storage = var_functions.query_db:2
if isinstance(civic_storage, str) and civic_storage.endswith('.json'):
    with open(civic_storage, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_storage

# Now count capital design projects with funding > $50K
# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    after_design = text[design_start:]
    end_pos = len(after_design)
    
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        marker_pos = after_design.find(marker)
        if marker_pos > 0 and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_section = after_design[:end_pos]
    
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or 'cid:' in line or ':' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Complete Design' in line:
            continue
        
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Match with funded projects
funded_names = [f['Project_Name'] for f in funding_data]

matched = 0
for design in design_projects:
    design_lower = design.lower()
    design_words = set(design_lower.split())
    
    for funded in funded_names:
        funded_lower = funded.lower()
        
        if design_lower in funded_lower or funded_lower in design_lower:
            matched += 1
            break
        
        funded_words = set(funded_lower.split())
        if len(design_words & funded_words) >= 3:
            matched += 1
            break

# Return final count
print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
