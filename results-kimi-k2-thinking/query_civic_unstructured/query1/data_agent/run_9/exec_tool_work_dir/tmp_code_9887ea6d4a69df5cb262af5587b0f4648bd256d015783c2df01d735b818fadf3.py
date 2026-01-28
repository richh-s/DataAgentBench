code = """import json, re, os

# Load data files
funding_path = locals()['var_functions.query_db:50']
civic_path = locals()['var_functions.query_db:8']

with open(funding_path) as f:
    funding_data = json.load(f)
with open(civic_path) as f:
    civic_docs = json.load(f)

# Build funding lookup map for projects > $50k
funding_map = {}
for rec in funding_data:
    name = rec['Project_Name'].lower().strip()
    amount = int(rec['Amount'])
    funding_map[name] = amount

# Extract project names from capital design section
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    marker = 'Capital Improvement Projects (Design)'
    if marker not in text:
        continue
    
    # Get design section
    idx = text.index(marker) + len(marker)
    section = text[idx:]
    
    # Truncate at next major heading
    end_markers = ['Capital Improvement Projects (Construction)', 
                   'Disaster Recovery Projects', 
                   'Capital Improvement Projects (Not Started)']
    for em in end_markers:
        if em in section:
            section = section[:section.index(em)]
    
    # Parse lines
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 8:
            continue
        
        # Skip metadata
        lower = line.lower()
        if any(x in lower for x in ['updates', 'schedule', 'page ', 'agenda item', '(cid:', 'complete design', 'advertise', 'construction']):
            continue
        
        # Check format
        if line[0].isupper() and not line.isupper():
            clean = re.sub(r'[^a-zA-Z0-9\s&\-\/\(\)]$', '', line)
            if len(clean) > 10:
                design_projects.append(clean.lower())

# Count unique matches
count = 0
seen = set()
for proj in design_projects:
    if proj in funding_map and proj not in seen:
        count += 1
        seen.add(proj)

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
