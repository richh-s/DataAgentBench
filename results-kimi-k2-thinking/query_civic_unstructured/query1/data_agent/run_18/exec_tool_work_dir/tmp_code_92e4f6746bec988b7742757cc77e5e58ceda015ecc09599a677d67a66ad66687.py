code = """import json

# Load funding data
funding_file = var_functions.query_db:1
civic_file = var_functions.query_db:2

with open(funding_file) as f:
    funding_data = json.load(f)
with open(civic_file) as f:
    civic_docs = json.load(f)

# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section start
    dstart = text.find('Capital Improvement Projects (Design)')
    if dstart < 0:
        continue
    
    # Find section end
    section = text[dstart:]
    dnext = section.find('Capital Improvement Projects (Construction)')
    if dnext < 0:
        dnext = section.find('Capital Improvement Projects (Not Started)')
    if dnext < 0:
        dnext = section.find('Disaster Recovery Projects')
    if dnext < 0:
        dnext = len(section)
    
    design_section = section[:dnext]
    
    # Extract lines that might be project names
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or 'cid:' in line or ':' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Complete Design' in line:
            continue
        
        # Check for project indicators
        indicators = ['Project', 'Improvements', 'Repairs', 'Master Plan', 'Study', 'Replacement']
        if any(indicator in line for indicator in indicators):
            clean = line.replace('\u2022', '').strip()
            if clean:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Get funded project names
funded_names = [f['Project_Name'] for f in funding_data]

# Count matches
matched = 0

for proj in design_projects:
    proj_lower = proj.lower()
    
    for fund in funded_names:
        fund_lower = fund.lower()
        
        # Simple matching
        if proj in fund or fund in proj:
            matched += 1
            break
        
        proj_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            matched += 1
            break

# Return final count
answer = json.dumps({'count': matched})
print('__RESULT__:')
print(answer)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
