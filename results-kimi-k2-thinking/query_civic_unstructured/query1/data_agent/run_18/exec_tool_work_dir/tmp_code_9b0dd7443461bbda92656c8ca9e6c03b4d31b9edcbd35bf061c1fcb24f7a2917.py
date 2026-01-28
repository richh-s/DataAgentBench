code = """import json

# Load data from files
with open(var_functions.query_db:70, 'r') as f:
    funding_data = json.load(f)

with open(var_functions.query_db:71, 'r') as f:
    civic_docs = json.load(f)

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    # Find design section end
    section = text[design_start:]
    end_pos = len(section)
    
    markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    for marker in markers:
        pos = section.find(marker)
        if pos > 0 and pos < end_pos:
            end_pos = pos
    
    design_section = section[:end_pos]
    
    # Extract project names line by line
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or ':' in line:
            continue
        if 'cid:' in line or 'Updates' in line or 'Schedule' in line:
            continue
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = ''.join(c for c in line if c.isalnum() or c.isspace()).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Count matches with funded projects
matched = 0

for proj in design_projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    if len(proj_words) < 2:
        continue
    
    for fund in funded_names:
        fund_lower = fund.lower()
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matched += 1
            break
        
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
