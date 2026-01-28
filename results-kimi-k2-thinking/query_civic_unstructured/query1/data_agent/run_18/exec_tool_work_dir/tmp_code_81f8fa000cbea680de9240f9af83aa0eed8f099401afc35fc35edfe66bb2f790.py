code = """import json
import re

# Load the data from storage variables
with open('var_functions.query_db:1', 'r') as f:
    funding_data = json.load(f)
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Get section boundaries
    after_design = text[design_start:]
    end_pos = len(after_design)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        marker_pos = after_design.find(marker)
        if marker_pos > 0 and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_section = after_design[:end_pos]
    
    # Extract project names
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

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Count matches
matched_count = 0

for design in design_projects:
    design_lower = design.lower()
    design_words = set(design_lower.split())
    
    for funded in funded_names:
        funded_lower = funded.lower()
        
        # Direct substring match
        if design_lower in funded_lower or funded_lower in design_lower:
            matched_count += 1
            break
        
        # Word overlap (3+ words)
        funded_words = set(funded_lower.split())
        if len(design_words & funded_words) >= 3:
            matched_count += 1
            break

# Return result
print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
