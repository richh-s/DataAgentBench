code = """import json

# Load funding data
fund_file = var_functions.query_db:58
if isinstance(fund_file, str):
    with open(fund_file, 'r') as f:
        funding = json.load(f)
else:
    funding = fund_file

# Load civic docs
civic_file = var_functions.query_db:59
if isinstance(civic_file, str):
    with open(civic_file, 'r') as f:
        docs = json.load(f)
else:
    docs = civic_file

# Extract design projects - simple approach
design = []

for doc in docs:
    text = doc.get('text', '')
    
    # Find design section
    dstart = text.find('Capital Improvement Projects (Design)')
    if dstart < 0:
        continue
    
    # Get section end
    section = text[dstart:]
    end = len(section)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = section.find(marker)
        if pos > 0 and pos < end:
            end = pos
    
    design_section = section[:end]
    
    # Simple line extraction
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('('):
            continue
        if 'cid:' in line or ':' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Complete Design' in line:
            continue
        
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = ''.join(c for c in line if c.isalnum() or c.isspace()).strip()
            if clean and len(clean) > 5:
                design.append(clean)

# Remove duplicates
design = list(set(design))

# Get funded names
funded = [f['Project_Name'] for f in funding]

# Count matches
count = 0

for proj in design:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    for fund in funded:
        fund_lower = fund.lower()
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            break
        
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            break

# Output result
result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json'}

exec(code, env_args)
