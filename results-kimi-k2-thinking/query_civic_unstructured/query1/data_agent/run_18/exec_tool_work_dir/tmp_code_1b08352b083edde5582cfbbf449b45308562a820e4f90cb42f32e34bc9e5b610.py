code = """import json
import re

# Load the two data files from the results
funding_file = var_functions.query_db:70
civic_file = var_functions.query_db:71

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Get list of funded project names
funded_names = []
for item in funding_data:
    funded_names.append(item['Project_Name'])

# Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    dpos = text.find('Capital Improvement Projects (Design)')
    if dpos < 0:
        continue
    
    # Find section end
    after = text[dpos:]
    end = len(after)
    markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Disaster Recovery Projects'
    ]
    for m in markers:
        p = after.find(m)
        if p > 0 and p < end:
            end = p
    
    section = after[:end]
    
    # Extract project names
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line == '-':
            continue
        if 'cid:' in line or 'Updates' in line or 'Schedule' in line:
            continue
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
unique_design = list(set(design_projects))

# Count how many design projects match funded projects
count = 0
matched = []

for proj in unique_design:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    if len(proj_words) < 2:
        continue
    
    for fund in funded_names:
        fund_lower = fund.lower()
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            matched.append(proj)
            break
        
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            matched.append(proj)
            break

# Return final count
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
