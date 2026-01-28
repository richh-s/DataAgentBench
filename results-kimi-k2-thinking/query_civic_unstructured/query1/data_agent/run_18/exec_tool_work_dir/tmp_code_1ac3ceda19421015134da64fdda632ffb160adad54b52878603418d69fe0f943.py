code = """import json, re

# Load data
fund_file = var_functions.query_db:70
civic_file = var_functions.query_db:71

with open(fund_file, 'r') as f:
    funding = json.load(f)
with open(civic_file, 'r') as f:
    docs = json.load(f)

# Get funded project names
funded = [f['Project_Name'] for f in funding]

# Extract capital design projects
all_design = []

for doc in docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Extract section
    after = text[design_start:]
    end = len(after)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = after.find(marker)
        if pos > 0 and pos < end:
            end = pos
    
    section = after[:end]
    
    # Find project names in this section
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or ':' in line or 'cid:' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Design' in line:
            continue
        
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line).strip()
            if clean and len(clean) > 5:
                all_design.append(clean)

# Remove duplicates
design_projects = list(set(all_design))

# Count matches
count = 0

for proj in design_projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    if len(proj_words) < 2:
        continue
    
    for fund in funded:
        fund_lower = fund.lower()
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            break
        
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            break

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
