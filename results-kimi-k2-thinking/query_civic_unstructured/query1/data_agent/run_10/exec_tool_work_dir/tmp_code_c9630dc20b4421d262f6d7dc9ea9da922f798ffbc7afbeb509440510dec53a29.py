code = """import json, re

# Access stored data
civic_data = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:5']

# Load JSON files
if isinstance(civic_data, str):
    with open(civic_data) as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_data

if isinstance(funding_data, str):
    with open(funding_data) as f:
        funding_recs = json.load(f)
else:
    funding_recs = funding_data

# Build funding lookup
funding_lookup = {}
for rec in funding_recs:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_lookup[rec['Project_Name'].strip()] = amount
    except:
        continue

# Extract design projects
design_list = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    start = text.find('Capital Improvement Projects (Design)')
    end = len(text)
    
    # Find end of section
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE']:
        pos = text.find(marker, start + 50)
        if pos > 0:
            end = min(end, pos)
    
    section = text[start:end]
    
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip various non-project lines
        skip = False
        for pattern in ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Complete Design']:
            if pattern in line:
                skip = True
                break
        if skip:
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line and line[0] in '•-◦(':
            continue
        
        if any(word in line for word in ['Staff', 'City', 'Complete', 'Advertise']) and len(line.split()) < 5:
            continue
        
        clean = line.strip('•-– ')
        if clean:
            design_list.append(clean)

# Remove duplicates
design_list = list(set(design_list))

# Normalize names for matching
def normalize(p):
    p = p.lower()
    p = re.sub(r'\s*\([^)]*\)$', '', p)
    p = p.replace('project', '')
    p = re.sub(r'[^a-z0-9\s]', '', p)
    return ' '.join(p.split())

# Build normalized funding lookup
funding_norm = {}
for name, amt in funding_lookup.items():
    norm = normalize(name)
    if norm:
        funding_norm[norm] = (name, amt)

# Count matches
count = 0
for proj in design_list:
    norm_proj = normalize(proj)
    if not norm_proj:
        continue
    
    # Direct match
    if norm_proj in funding_norm:
        count += 1
        continue
    
    # Flexible matching
    for norm_f, (orig_f, amt_f) in funding_norm.items():
        if norm_proj in norm_f or norm_f in norm_proj:
            count += 1
            break
        
        # Word overlap for long names
        if len(norm_proj) > 15 and len(norm_f) > 15:
            pw = set(norm_proj.split())
            fw = set(norm_f.split())
            if len(pw.intersection(fw)) >= 3:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
