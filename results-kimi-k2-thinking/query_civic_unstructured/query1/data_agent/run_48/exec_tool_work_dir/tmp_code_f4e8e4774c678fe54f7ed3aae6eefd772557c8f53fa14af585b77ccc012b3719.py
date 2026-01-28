code = """import json, re, os

# Load funding data
funding_path = var_functions.query_db:0
with open(funding_path) as f:
    funding = json.load(f)

# Load civic documents
with open(var_functions.query_db:2) as f:
    docs = json.load(f)

# Build set of high-funding projects (>50k)
high_funding = set()
for item in funding:
    if int(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

# Extract design project names
design_names = []
for doc in docs:
    txt = doc.get('text', '')
    
    # Find design section
    marker = 'Capital Improvement Projects (Design)'
    idx = txt.find(marker)
    if idx == -1:
        continue
    
    # Get section up to next header
    section = txt[idx + 37:]
    for end_marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        end = section.find(end_marker)
        if end != -1:
            section = section[:end]
            break
    
    # Extract names
    for block in section.split('\n\n'):
        block = block.strip()
        if block and len(block) > 10:
            first_line = block.split('\n')[0].strip()
            if len(first_line) > 10 and not first_line.isupper():
                clean = re.sub(r'^[A-Z]\.\s*', '', first_line)
                clean = re.sub(r'^\d+\.\s*', '', clean)
                if len(clean) > 10 and 'Updates:' not in clean:
                    design_names.append(clean)

# Match
normalize = lambda n: re.sub(r'[^a-z0-9]', '', n.lower().strip())
count = 0
for proj in design_names:
    proj_norm = normalize(proj)
    for fund in high_funding:
        fund_norm = normalize(fund)
        if proj_norm == fund_norm or (len(proj_norm) > 12 and proj_norm in fund_norm) or (len(fund_norm) > 12 and fund_norm in proj_norm):
            count += 1
            break

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
