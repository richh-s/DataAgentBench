code = """import json, re

# Load the data
funding_path = var_functions.query_db:1
civic_path = var_functions.query_db:2

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Find design projects
design = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Locate design section
    dpos = text.find('Capital Improvement Projects (Design)')
    if dpos < 0: 
        continue
        
    after = text[dpos:]
    endpos = len(after)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        mpos = after.find(marker)
        if mpos > 0 and mpos < endpos:
            endpos = mpos
    
    section = after[:endpos]
    
    # Extract project names
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 10: continue
        if line.startswith('(') or 'cid:' in line: continue
        
        indicators = ['Project', 'Improvements', 'Repairs', 'Master Plan']
        for ind in indicators:
            if ind in line:
                clean = re.sub('[^A-Za-z0-9\s]', '', line)
                clean = clean.strip()
                if clean:
                    design.append(clean)
                break

# Remove duplicates
design = list(set(design))

# Get funded project names
funded = [f['Project_Name'] for f in funding_data]

# Count matches
count = 0
for proj in design:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    
    for fund in funded:
        if proj in fund or fund in proj:
            count += 1
            break
        
        fund_lower = fund.lower()
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            break

# Output
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
