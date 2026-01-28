code = """import json

# Load data
f1 = open(var_functions.query_db:70)
funding_data = json.load(f1)
f1.close()

f2 = open(var_functions.query_db:2)
civic_docs = json.load(f2)
f2.close()

# Filter high funding projects (> $50,000)
high_funding = set()
for f in funding_data:
    if int(f['Amount']) > 50000:
        high_funding.add(f['Project_Name'])

# Extract capital projects in design status from civic documents
# Use simple string operations
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Get section after design start
    design_section = text[design_start:]
    
    # Cut at next major section
    construction_pos = design_section.find('Capital Improvement Projects (Construction)')
    notstarted_pos = design_section.find('Capital Improvement Projects (Not Started)')
    disaster_pos = design_section.find('Disaster Recovery Projects')
    
    end_pos = len(design_section)
    for pos in [construction_pos, notstarted_pos, disaster_pos]:
        if pos > 0 and pos < end_pos:
            end_pos = pos
    
    design_section = design_section[:end_pos]
    
    # Split into blocks to find project names
    blocks = design_section.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 20:
            # Get first line
            lines = block.split('\n')
            if lines and len(lines[0].strip()) > 15:
                name = lines[0].strip()
                if not name.isupper():
                    design_projects.append(name)

# Simple matching - check if names match or overlap
matched = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for fund in high_funding:
        fund_lower = fund.lower()
        
        # Direct match or substring
        if proj_lower == fund_lower or proj in fund or fund in proj:
            matched += 1
            break
        
        # Word overlap
        proj_words = proj_lower.split()
        fund_words = fund_lower.split()
        if len(proj_words) >= 3 and len(fund_words) >= 3:
            common_words = set(proj_words) & set(fund_words)
            if len(common_words) >= 2:
                matched += 1
                break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
