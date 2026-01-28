code = """import json
import re

# Get the data from previous step
funding_data_key = 'var_functions.query_db:70'
civic_docs_key = 'var_functions.query_db:71'

# Check if they're file paths or direct data
funding_file = var_functions.query_db:70
civic_file = var_functions.query_db:71

# Load funding data
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

# Load civic documents
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_file

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    dpos = text.find('Capital Improvement Projects (Design)')
    if dpos < 0:
        continue
    
    # Find section boundaries
    after = text[dpos:]
    end = len(after)
    
    markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    for m in markers:
        pos = after.find(m)
        if pos > 0 and pos < end:
            end = pos
    
    section = after[:end]
    
    # Extract project name lines
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('-'):
            continue
        if 'cid:' in line or ':' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Design' in line:
            continue
        
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = re.sub(r'[^A-Za-z0-9\s]', '', line).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Match design projects with funded projects
count = 0
matched = []

for proj in design_projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    if len(proj_words) < 2:
        continue
    
    for fund in funded_names:
        fund_lower = fund.lower()
        
        # Direct substring match
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            matched.append(proj)
            break
        
        # Word overlap
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            matched.append(proj)
            break

# Return final result
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.list_db:90': ['Funding'], 'var_functions.list_db:91': ['civic_docs'], 'var_functions.execute_python:96': {'funding_count': 276, 'civic_count': 5}}

exec(code, env_args)
