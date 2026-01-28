code = """import json, re

# Load funding data - high amounts only
funding_path = var_functions.query_db:0
with open(funding_path) as f:
    funding = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:2
with open(civic_path) as f:
    docs = json.load(f)

# Get just the names of high-funding projects
high_funding_names = set()
for item in funding:
    if int(item['Amount']) > 50000:
        high_funding_names.add(item['Project_Name'])

# Extract design project names
extracted_names = []

for doc in docs:
    txt = doc.get('text', '')
    
    # Find the design section
    design_idx = txt.find('Capital Improvement Projects (Design)')
    if design_idx == -1:
        continue
    
    # Get design section text
    design_part = txt[design_idx:]
    
    # Cut off at next major section
    for section_marker in ['Capital Improvement Projects (Construction)', 
                           'Capital Improvement Projects (Not Started)', 
                           'Disaster Recovery Projects']:
        end_idx = design_part.find(section_marker)
        if end_idx > 0:
            design_part = design_part[:end_idx]
            break
    
    # Find project names
    chunks = design_part.split('\n\n')
    for chunk in chunks:
        chunk = chunk.strip()
        if chunk and len(chunk) > 10:
            first = chunk.split('\n')[0].strip()
            if len(first) >= 10 and first[0].isalpha() and not first.isupper():
                cleaned = re.sub(r'^[A-Z]\.\s*', '', first)
                cleaned = re.sub(r'^\d+\.\s*', '', cleaned)
                if len(cleaned) > 10 and 'Updates:' not in cleaned and 'Schedule:' not in cleaned:
                    extracted_names.append(cleaned)

# Normalize for comparison
def normalize(name):
    return re.sub(r'[^a-z0-9]', '', name.lower())

# Match
matched = 0
for proj in extracted_names:
    proj_norm = normalize(proj)
    if len(proj_norm) < 8:
        continue
    
    for fund in high_funding_names:
        fund_norm = normalize(fund)
        if proj_norm == fund_norm or (len(proj_norm) > 10 and proj_norm in fund_norm) or (len(fund_norm) > 10 and fund_norm in proj_norm):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
