code = """import json
import os
import re

# Get the file paths from storage variables
funding_file_path = var_functions.query_db_70
civic_file_path = var_functions.query_db_71

# Load funding data
if isinstance(funding_file_path, str) and os.path.exists(funding_file_path):
    with open(funding_file_path, 'r') as f:
        funding_data = json.load(f)
else:
    # If it's not a file path, it's the actual data
    funding_data = var_functions.query_db_70

# Load civic documents  
if isinstance(civic_file_path, str) and os.path.exists(civic_file_path):
    with open(civic_file_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db_71

# Get funded project names
funded_names = [item['Project_Name'] for item in funding_data]

# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Extract design section
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
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('●'):
            continue
        if 'cid:' in line or ':' in line:
            continue
        
        # Skip update/schedule lines
        skip_terms = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction']
        if any(term in line for term in skip_terms):
            continue
        
        # Check for project indicators
        indicators = ['Project', 'Improvements', 'Repairs', 'Infrastructure', 'Master Plan',
                      'Study', 'Replacement', 'Facility', 'Road', 'Park', 'Beach', 'Highway']
        
        if any(indicator in line for indicator in indicators):
            # Clean the name
            clean = re.sub(r'[^A-Za-z0-9\s&]', '', line).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
unique_design = list(set(design_projects))

# Match design projects with funded projects
count = 0

for proj in unique_design:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    if len(proj_words) < 2:
        continue
    
    for funded in funded_names:
        funded_lower = funded.lower()
        
        # Direct substring match
        if proj_lower in funded_lower or funded_lower in proj_lower:
            count += 1
            break
        
        # Word overlap (3+ words)
        funded_words = set(funded_lower.split())
        if len(proj_words & funded_words) >= 3:
            count += 1
            break

# Return final answer
answer = json.dumps(count)
print('__RESULT__:')
print(answer)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.list_db:90': ['Funding'], 'var_functions.list_db:91': ['civic_docs']}

exec(code, env_args)
