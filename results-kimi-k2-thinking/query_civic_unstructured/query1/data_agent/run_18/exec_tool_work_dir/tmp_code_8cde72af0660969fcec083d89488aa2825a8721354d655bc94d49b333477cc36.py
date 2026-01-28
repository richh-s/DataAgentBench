code = """import json, re

# Load funding data
f_file = var_functions.query_db:1
c_file = var_functions.query_db:2

with open(f_file) as f:
    funding = json.load(f)
with open(c_file) as f:
    docs = json.load(f)

# Extract design projects
design_list = []

for doc in docs:
    t = doc.get('text', '')
    
    dstart = t.find('Capital Improvement Projects (Design)')
    if dstart < 0:
        continue
        
    section = t[dstart:]
    dnext = section.find('Capital Improvement Projects (Construction)')
    if dnext < 0:
        dnext = section.find('Capital Improvement Projects (Not Started)')
    if dnext < 0:
        dnext = section.find('Disaster Recovery Projects')
    if dnext < 0:
        dnext = len(section)
    
    design_section = section[:dnext]
    
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or 'cid:' in line or ':' in line:
            continue
        if 'Updates' in line or 'Schedule' in line:
            continue
        
        # Check project indicators
        for indicator in ['Project', 'Improvements', 'Repairs', 'Master Plan']:
            if indicator in line:
                clean = re.sub(r'[^A-Za-z0-9\s]', '', line)
                clean = clean.strip()
                if clean:
                    design_list.append(clean)
                break

# Remove duplicates
design_list = list(set(design_list))

# Get funded names
funded = [f['Project_Name'] for f in funding]

# Count matches
count = 0

for proj in design_list:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    for fund in funded:
        fund_lower = fund.lower()
        
        if proj in fund or fund in proj:
            count += 1
            break
        
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            break

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
