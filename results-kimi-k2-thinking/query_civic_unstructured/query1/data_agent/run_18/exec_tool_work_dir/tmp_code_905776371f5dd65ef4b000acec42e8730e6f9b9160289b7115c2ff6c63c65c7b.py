code = """import json

# Load the funding data
funding_path = var_functions.query_db:50
civic_path = var_functions.query_db:51

with open(funding_path, 'r') as f:
    funding_projects = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    dpos = text.find('Capital Improvement Projects (Design)')
    if dpos < 0:
        continue
    
    section = text[dpos:]
    endpos = len(section)
    
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        mpos = section.find(marker)
        if mpos > 0 and mpos < endpos:
            endpos = mpos
    
    design_section = section[:endpos]
    
    for line in design_section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or ':' in line or 'cid:' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Complete Design' in line:
            continue
        
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = ''.join(c for c in line if c.isalnum() or c.isspace()).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Match with funding
funded_names = [f['Project_Name'] for f in funding_projects]
matches = []

for proj in design_projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    for funded in funded_names:
        funded_lower = funded.lower()
        if proj_lower in funded_lower or funded_lower in proj_lower:
            matches.append(proj)
            break
        
        funded_words = set(funded_lower.split())
        if len(proj_words & funded_words) >= 3:
            matches.append(proj)
            break

count = len(matches)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json'}

exec(code, env_args)
