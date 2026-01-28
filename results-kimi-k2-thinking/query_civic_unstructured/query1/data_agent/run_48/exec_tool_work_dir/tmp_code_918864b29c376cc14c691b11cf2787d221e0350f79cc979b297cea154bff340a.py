code = """import json

# Load funding data
funding_file = var_functions.query_db:0
f1 = open(funding_file)
funding = json.load(f1)
f1.close()

# Load civic data
civic_file = var_functions.query_db:2
f2 = open(civic_file)
docs = json.load(f2)
f2.close()

# Get projects with funding > $50,000
high_funding = set()
for r in funding:
    amount = int(r['Amount'])
    if amount > 50000:
        high_funding.add(r['Project_Name'])

# Extract capital design project names
design_projects = []

for doc in docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Extract section content
    design_part = text[design_start + 37:]  # Skip the header text
    
    # Find where design section ends
    next_section_pos = len(design_part)
    markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    for marker in markers:
        pos = design_part.find(marker)
        if pos > 0 and pos < next_section_pos:
            next_section_pos = pos
    
    design_content = design_part[:next_section_pos]
    
    # Find project names by splitting and filtering
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
        
        # Skip non-project lines
        if len(first_line) > 10 and not first_line.isupper():
            # Remove simple bullet prefixes
            clean_name = first_line
            if len(clean_name) > 2 and clean_name[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and clean_name[1] == '.':
                clean_name = clean_name[2:].strip()
            if len(clean_name) > 10 and 'Updates:' not in clean_name and 'Schedule:' not in clean_name:
                design_projects.append(clean_name)

# Match projects with funding using simple string comparison
matched_count = 0

for proj in design_projects:
    proj_lower = proj.lower()
    for fund_name in high_funding:
        fund_lower = fund_name.lower()
        # Check for direct match or substring match
        if proj_lower == fund_lower or proj in fund_name or fund_name in proj:
            matched_count += 1
            break
        # Check word overlap for multi-word names
        proj_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        if len(proj_words) >= 3 and len(fund_words) >= 3:
            common = proj_words.intersection(fund_words)
            if len(common) >= 2:
                matched_count += 1
                break

result = matched_count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
