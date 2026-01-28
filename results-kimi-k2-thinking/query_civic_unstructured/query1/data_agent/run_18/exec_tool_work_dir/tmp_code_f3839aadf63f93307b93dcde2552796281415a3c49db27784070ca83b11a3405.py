code = """import json
import re

# Load funding data (projects > $50K)
funding_file = var_functions.query_db:70
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

# Load civic documents
civic_file = var_functions.query_db:71
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

# Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find design section end (next major section)
    after_design = text[design_start:]
    end_pos = len(after_design)
    
    section_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Disaster Recovery Projects'
    ]
    
    for marker in section_markers:
        marker_pos = after_design.find(marker)
        if marker_pos > 0 and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_section = after_design[:end_pos]
    
    # Extract project names from design section
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        
        # Skip short lines and metadata
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('●'):
            continue
        if 'cid:' in line or ':' in line:
            continue
        
        # Skip update/schedule lines
        skip_terms = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction',
                     'Project Description', 'Project Schedule', 'Estimated Schedule']
        if any(term in line for term in skip_terms):
            continue
        
        # Look for project indicators
        indicators = ['Project', 'Improvements', 'Repairs', 'Infrastructure', 'Master Plan',
                     'Study', 'Replacement', 'Facility', 'Road', 'Park', 'Beach', 'Highway']
        
        if any(indicator in line for indicator in indicators):
            # Clean the project name
            clean = re.sub(r'[^A-Za-z0-9\s&]', '', line).strip()
            clean = ' '.join(clean.split())  # Normalize whitespace
            
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
unique_design = list(set(design_projects))

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Match projects
matches = 0
for design_proj in unique_design:
    design_lower = design_proj.lower()
    design_words = set(design_lower.split())
    
    if len(design_words) < 2:
        continue
    
    for funded in funded_names:
        funded_lower = funded.lower()
        
        # Direct substring match
        if design_proj in funded or funded in design_proj:
            matches += 1
            break
        
        # Word overlap
        funded_words = set(funded_lower.split())
        common = design_words & funded_words
        
        # Match if 3+ words or key terms
        key_terms = {'road', 'park', 'beach', 'highway', 'bridge', 'drain', 'storm', 'canyon'}
        if len(common) >= 3 or len(common & key_terms) >= 2:
            matches += 1
            break

# Return final count
print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
