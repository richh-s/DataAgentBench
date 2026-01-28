code = """import json
import re

# Load data from files
with open(var_functions.query_db:1, 'r') as f:
    funding_data = json.load(f)

with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    dpos = text.find('Capital Improvement Projects (Design)')
    if dpos < 0:
        continue
    
    section = text[dpos:]
    
    # Find section end
    endpos = len(section)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        mpos = section.find(marker)
        if mpos > 0 and mpos < endpos:
            endpos = mpos
    
    design_section = section[:endpos]
    
    # Extract project names
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10 or line.startswith('('):
            continue
        if 'cid:' in line or 'Updates' in line or 'Schedule' in line:
            continue
        
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Match with funding data
funded_names = [f['Project_Name'] for f in funding_data]
count = 0

for proj in design_projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    for fund in funded_names:
        fund_lower = fund.lower()
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            break
        
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            break

# Return answer
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
