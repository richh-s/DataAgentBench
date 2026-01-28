code = """import json
import re

# Load funding data with > $50k
funding_path = var_functions.query_db:0
with open(funding_path) as f:
    funding = json.load(f)

# Load civic documents
with open(var_functions.query_db:2) as f:
    docs = json.load(f)

# Get high funding projects
high_funding = set()
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding.add(r['Project_Name'])

# Extract design sections and project names
project_names = []
for doc in docs:
    text = doc.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    design_section = text[start + 37:]
    
    # Cut at next section
    end_pos = len(design_section)
    for marker in ['Capital Improvement Projects (Construction)','Capital Improvement Projects (Not Started)','Disaster Recovery Projects']:
        pos = design_section.find(marker)
        if pos > 0:
            end_pos = min(end_pos, pos)
    
    design_section = design_section[:end_pos]
    
    # Find project names
    for block in design_section.split('\n\n'):
        block = block.strip()
        if not block or len(block) < 10:
            continue
        
        first_line = block.split('\n')[0].strip()
        if len(first_line) >= 10 and not first_line.isupper():
            clean_name = re.sub(r'^[A-Z]\.\s*', '', first_line)
            clean_name = re.sub(r'^\d+\.\s*', '', clean_name)
            if 'Updates:' not in clean_name and len(clean_name) > 10:
                project_names.append(clean_name)

# Normalize and match
def normalize(n):
    return re.sub(r'[^a-z0-9]', '', n.lower().strip())

count = 0
for proj in project_names:
    proj_norm = normalize(proj)
    for fund_name in high_funding:
        fund_norm = normalize(fund_name)
        if proj_norm == fund_norm or (len(proj_norm) > 12 and proj_norm in fund_norm) or (len(fund_norm) > 12 and fund_norm in proj_norm):
            count += 1
            break

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
