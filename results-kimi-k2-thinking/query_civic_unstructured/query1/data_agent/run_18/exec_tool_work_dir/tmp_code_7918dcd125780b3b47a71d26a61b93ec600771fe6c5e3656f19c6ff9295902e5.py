code = """import json
import re

# Load the data from files
funding_file = var_functions.query_db:1
civic_file = var_functions.query_db:2

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Get section after design start
    after_design = text[design_start:]
    
    # Find where design section ends
    end_pos = len(after_design)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = after_design.find(marker)
        if pos > 0 and pos < end_pos:
            end_pos = pos
    
    design_section = after_design[:end_pos]
    
    # Extract project names from lines
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) < 10 or line.startswith('(') or 'cid:' in line:
            continue
        
        skip_terms = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Project Description']
        if any(term in line for term in skip_terms):
            continue
        
        # Look for project-like lines
        indicators = ['Project', 'Improvements', 'Repairs', 'Master Plan', 'Study', 'Infrastructure', 'Replacement']
        if any(indicator in line for indicator in indicators):
            # Clean the name
            clean_name = re.sub(r'[^A-Za-z0-9\s]', '', line)
            clean_name = clean_name.strip()
            if clean_name:
                design_projects.append(clean_name)

# Remove duplicates
design_projects = list(set(design_projects))

# Get list of funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Match design projects with funded projects
matched = []
for design_proj in design_projects:
    design_lower = design_proj.lower()
    design_words = set(design_lower.split())
    
    for funded_name in funded_names:
        funded_lower = funded_name.lower()
        
        # Direct substring match
        if design_proj in funded_name or funded_name in design_proj:
            matched.append(design_proj)
            break
        
        # Word overlap matching
        funded_words = set(funded_lower.split())
        common = design_words & funded_words
        if len(common) >= 3:
            matched.append(design_proj)
            break

# Count matches
count = len(matched)

# Return result
print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
