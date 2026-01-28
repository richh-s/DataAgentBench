code = """import json
import re

# Load data
f1 = open(var_functions.query_db:0)
funding_data = json.load(f1)
f1.close()

f2 = open(var_functions.query_db:2)
civic_docs = json.load(f2)
f2.close()

# Get high funding project names (> $50,000)
high_funding_names = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding_names.append(record['Project_Name'])

# Extract capital design project names from civic documents
design_project_names = []

design_header = 'Capital Improvement Projects (Design)'
construction_header = 'Capital Improvement Projects (Construction)'
not_started_header = 'Capital Improvement Projects (Not Started)'
disaster_header = 'Disaster Recovery Projects'

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find where design section starts
    header_start = text.find(design_header)
    if header_start == -1:
        continue
    
    # Extract section after header
    start_pos = header_start + len(design_header)
    section_text = text[start_pos:]
    
    # Find where design section ends (start of next major section)
    section_end = len(section_text)
    next_headers = [construction_header, not_started_header, disaster_header]
    
    for next_header in next_headers:
        header_pos = section_text.find(next_header)
        if header_pos > 0 and header_pos < section_end:
            section_end = header_pos
    
    # Design section content
    design_content = section_text[:section_end]
    
    # Split into blocks and extract project names
    blocks = design_content.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) < 10:
            continue
        
        # Get first line
        lines = block.split('\n')
        if not lines:
            continue
        
        first_line = lines[0].strip()
        
        # Simple filters for non-project lines
        if len(first_line) < 10:
            continue
        
        if first_line.isupper():
            continue
        
        if 'Updates:' in first_line or 'Schedule:' in first_line:
            continue
        
        # Clean bullet prefixes
        clean_name = first_line
        if len(clean_name) >= 3 and clean_name[0].isalpha() and clean_name[1] == '.':
            clean_name = clean_name[2:].strip()
        
        if len(clean_name) > 10:
            design_project_names.append(clean_name)

# Simplified matching approach
matched_count = 0

for proj_name in design_project_names:
    proj_lower = proj_name.lower()
    
    for fund_name in high_funding_names:
        fund_lower = fund_name.lower()
        
        # Check for exact match of names
        if proj_lower == fund_lower:
            matched_count += 1
            break
        
        # Check if project name is contained in funding name or vice versa
        if proj_name in fund_name or fund_name in proj_name:
            matched_count += 1
            break
        
        # Check for significant word overlap for multi-word names
        proj_words = proj_lower.split()
        fund_words = fund_lower.split()
        
        if len(proj_words) >= 3 and len(fund_words) >= 3:
            common_words = set(proj_words) & set(fund_words)
            if len(common_words) >= 2:
                matched_count += 1
                break

result = matched_count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
