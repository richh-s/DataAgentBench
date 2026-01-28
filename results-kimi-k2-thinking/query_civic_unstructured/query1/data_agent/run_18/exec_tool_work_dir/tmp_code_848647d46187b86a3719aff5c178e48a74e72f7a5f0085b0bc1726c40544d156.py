code = """import json

# Load the data directly
funding_path = var_functions.query_db:1
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section position
    dpos = text.find('Capital Improvement Projects (Design)')
    if dpos < 0:
        continue
        
    # Find section end position
    section = text[dpos:]
    end_pos = len(section)
    
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        marker_pos = section.find(marker)
        if marker_pos > 0 and marker_pos < end_pos:
            end_pos = marker_pos
    
    design_text = section[:end_pos]
    
    # Extract project names by looking for indicator words
    for line in design_text.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('('):
            continue
        if 'cid:' in line or 'Updates' in line or 'Schedule' in line:
            continue
        
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line or 'Master Plan' in line:
            clean = line.replace('\u2022', '').strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Count matches
matched = 0
for proj in design_projects:
    for fund in funded_names:
        # Case-insensitive matching
        proj_lower = proj.lower()
        fund_lower = fund.lower()
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matched += 1
            break
        
        # Check word overlap
        proj_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            matched += 1
            break

# Output result
print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
