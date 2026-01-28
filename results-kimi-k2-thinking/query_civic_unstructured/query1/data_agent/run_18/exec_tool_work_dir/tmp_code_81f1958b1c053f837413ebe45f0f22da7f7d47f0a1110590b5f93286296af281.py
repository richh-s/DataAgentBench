code = """import json
import re

# Load data from files
f = open(var_functions.query_db:70, 'r')
funding_data = json.load(f)
f.close()

c = open(var_functions.query_db:71, 'r')
civic_docs = json.load(c)
c.close()

# Get funded project names
funded = []
for item in funding_data:
    funded.append(item['Project_Name'])

# Extract capital design projects
design = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    dpos = text.find('Capital Improvement Projects (Design)')
    if dpos < 0:
        continue
    
    after = text[dpos:]
    end = len(after)
    
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = after.find(marker)
        if pos > 0 and pos < end:
            end = pos
    
    section = after[:end]
    
    # Extract lines
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('('):
            continue
        if 'cid:' in line or 'Updates' in line or 'Schedule' in line:
            continue
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line).strip()
            if clean and len(clean) > 5:
                design.append(clean)

# Remove duplicates
design = list(set(design))

# Count matches
count = 0
for proj in design:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    if len(proj_words) < 2:
        continue
    
    for fund in funded:
        fund_lower = fund.lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count = count + 1
            break
        
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count = count + 1
            break

result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
