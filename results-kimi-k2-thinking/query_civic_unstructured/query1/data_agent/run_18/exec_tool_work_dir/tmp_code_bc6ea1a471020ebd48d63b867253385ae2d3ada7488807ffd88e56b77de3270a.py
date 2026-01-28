code = """import json, re

# Load funding and civic data
funding_path = var_functions.query_db:1
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Find capital projects with design status
design_projects = []

for doc in civic_docs:
    t = doc.get('text', '')
    if not t:
        continue
    
    # Locate design section
    design_pos = t.find('Capital Improvement Projects (Design)')
    if design_pos < 0:
        continue
        
    # Get section boundaries
    after_design = t[design_pos:]
    end_pos = len(after_design)
    
    for end_marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        marker_pos = after_design.find(end_marker)
        if marker_pos > 0 and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_section = after_design[:end_pos]
    
    # Extract project lines
    lines = [line.strip() for line in design_section.split('\n')]
    for line in lines:
        # Skip metadata
        if len(line) < 10 or line.startswith('(') or 'cid:' in line:
            continue
        
        skip_terms = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction', 'Project Description']
        if any(term in line for term in skip_terms):
            continue
        
        # Check for project indicators
        for indicator in ['Project', 'Improvements', 'Repairs', 'Master Plan']:
            if indicator in line:
                # Clean name
                clean_name = re.sub(r'[^A-Za-z0-9\s]', '', line)
                clean_name = clean_name.strip()
                if clean_name and len(clean_name) > 5:
                    design_projects.append(clean_name)
                break

# Remove duplicates
design_projects = list(set(design_projects))

# Get funded project names from funding table
funded_names = [f['Project_Name'] for f in funding_data]

# Count matches between design and funded projects
matched_count = 0

for design_name in design_projects:
    design_lower = design_name.lower()
    design_words = set(design_lower.split())
    
    for funded_name in funded_names:
        funded_lower = funded_name.lower()
        
        # Case-insensitive substring match
        if design_name in funded_name or funded_name in design_name:
            matched_count += 1
            break
        
        # Word overlap matching (at least 3 words in common)
        funded_words = set(funded_lower.split())
        common_words = design_words & funded_words
        if len(common_words) >= 3:
            matched_count += 1
            break

# Return result
result = json.dumps({'count': matched_count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
