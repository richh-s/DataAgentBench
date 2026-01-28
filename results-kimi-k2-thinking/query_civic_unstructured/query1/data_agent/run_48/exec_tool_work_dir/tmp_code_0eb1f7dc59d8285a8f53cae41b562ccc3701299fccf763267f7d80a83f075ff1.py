code = """import json

# Load funding data in > $50k
f1 = open(var_functions.query_db:0)
funding_data = json.load(f1)
f1.close()

# Load civic documents
f2 = open(var_functions.query_db:2)
civic_docs = json.load(f2)
f2.close()

# Get high funding project names
high_funding_names = set()
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_names.add(record['Project_Name'])

# Extract capital design project names from civic documents
design_project_names = []

# Define section headers
DESIGN_HEADER = 'Capital Improvement Projects (Design)'
CONSTRUCTION_HEADER = 'Capital Improvement Projects (Construction)'
NOT_STARTED_HEADER = 'Capital Improvement Projects (Not Started)'
DISASTER_HEADER = 'Disaster Recovery Projects'

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    header_start = text.find(DESIGN_HEADER)
    if header_start == -1:
        continue
    
    # Extract section after header
    start_pos = header_start + len(DESIGN_HEADER)
    section_text = text[start_pos:]
    
    # Find where design section ends (look for next major section)
    section_end = len(section_text)
    next_headers = [CONSTRUCTION_HEADER, NOT_STARTED_HEADER, DISASTER_HEADER]
    
    for next_header in next_headers:
        header_pos = section_text.find(next_header)
        if header_pos > 0 and header_pos < section_end:
            section_end = header_pos
    
    # Extract design section content
    design_content = section_text[:section_end]
    
    # Parse project names from content
    blocks = design_content.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) < 10:
            continue
        
        # Get first line of block
        lines = block.split('\n')
        if not lines:
            continue
        
        first_line = lines[0].strip()
        
        # Apply filters to identify project names
        if len(first_line) < 10:
            continue
        
        if first_line.isupper():
            continue
        
        if 'Updates:' in first_line or 'Schedule:' in first_line:
            continue
        
        # Remove bullet point prefixes if present
        clean_name = first_line
        if len(clean_name) >= 3:
            if clean_name[0].isalpha() and clean_name[1] == '.':
                clean_name = clean_name[2:].strip()
        
        # Add if still long enough
        if len(clean_name) > 10:
            design_project_names.append(clean_name)

# Match design projects with funding
matched_count = 0

import re

# Normalize for comparison function
def normalize_name(name):
    name = name.lower().strip()
    name = name.replace('\\n', ' ')
    name = name.replace('\\r', ' ')
    name = re.sub('[^a-z0-9 ]', '', name)
    name = ' '.join(name.split())
    return name

for proj_name in design_project_names:
    proj_normalized = normalize_name(proj_name)
    
    if len(proj_normalized) < 8:
        continue
    
    for fund_name in high_funding_names:
        fund_normalized = normalize_name(fund_name)
        
        # Check for exact match
        if proj_normalized == fund_normalized:
            matched_count += 1
            break
        
        # Check if project name is contained in funding name
        if proj_normalized in fund_normalized and len(proj_normalized) > 12:
            matched_count += 1
            break
        
        # Check if funding name is contained in project name
        if fund_normalized in proj_normalized and len(fund_normalized) > 12:
            matched_count += 1
            break

result = matched_count

# Format output
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
