code = """import json, re

# Load funding data
funding_path = var_functions.query_db:0
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents  
civic_path = var_functions.query_db:2
with open(civic_path) as f:
    civic_docs = json.load(f)

# Get high value funding project names
high_funding = set()
for f in funding_data:
    if int(f['Amount']) > 50000:
        high_funding.add(f['Project_Name'])

# Extract design projects from civic docs
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_idx = text.find('Capital Improvement Projects (Design)')
    if design_idx == -1:
        continue
    
    # Get section up to next major heading
    design_part = text[design_idx:]
    for marker in ['Capital Improvement Projects (Construction)', 
                   'Capital Improvement Projects (Not Started)', 
                   'Disaster Recovery Projects']:
        end_idx = design_part.find(marker)
        if end_idx != -1:
            design_part = design_part[:end_idx]
            break
    
    # Extract potential project names
    blocks = design_part.split('\n\n')
    for block in blocks:
        block = block.strip()
        if block and len(block) > 10:
            first = block.split('\n')[0].strip()
            if len(first) >= 10 and not first.isupper():
                # Remove bullet prefixes
                clean = re.sub(r'^[A-Z]\.\s*', '', first)
                clean = re.sub(r'^\d+\.\s*', '', clean)
                if len(clean) > 10 and 'Updates:' not in clean:
                    design_projects.append(clean)

# Normalize names and match
normalize = lambda name: re.sub(r'[^a-z0-9]', '', name.lower().strip())

matched = 0
for proj in design_projects:
    proj_norm = normalize(proj)
    if len(proj_norm) < 8:
        continue
    
    for fund in high_funding:
        fund_norm = normalize(fund)
        if proj_norm == fund_norm or (len(proj_norm) > 12 and proj_norm in fund_norm) or (len(fund_norm) > 12 and fund_norm in proj_norm):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
