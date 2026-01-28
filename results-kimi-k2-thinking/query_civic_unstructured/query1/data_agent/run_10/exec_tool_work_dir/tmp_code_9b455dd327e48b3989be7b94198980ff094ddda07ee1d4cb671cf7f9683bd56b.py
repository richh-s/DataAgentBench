code = """import json, re

# Access stored data
civic_docs = locals()['var_functions.query_db:2']
funding_recs = locals()['var_functions.query_db:5']

# Handle file paths
if isinstance(civic_docs, str):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

if isinstance(funding_recs, str):
    with open(funding_recs) as f:
        funding_recs = json.load(f)

# Build funding lookup for >$50k
funding_lookup = {}
for rec in funding_recs:
    try:
        amt = int(rec['Amount'])
        if amt > 50000:
            funding_lookup[rec['Project_Name']] = amt
    except:
        continue

# Extract capital design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    start = text.find('Capital Improvement Projects (Design)')
    end = len(text)
    
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = text.find(marker, start + 50)
        if pos > 0:
            end = min(end, pos)
    
    section = text[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        
        bad_patterns = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Updates', 'Project Schedule']
        if any(bp in line for bp in bad_patterns):
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line and line[0] in '•-◦(':
            continue
        
        if any(w in line for w in ['Staff', 'City', 'Complete']) and len(line.split()) < 5:
            continue
        
        clean = line.strip('•-– ')
        if clean:
            design_projects.append(clean)

# Deduplicate
design_projects = list(set(design_projects))

# Normalize for matching
def normalize(p):
    p = p.lower()
    p = re.sub(r'\s*\([^)]*\)$', '', p)
    p = p.replace('project', '')
    p = re.sub(r'[^a-z0-9\s]', '', p)
    return ' '.join(p.split())

funding_norm = {}
for name, amt in funding_lookup.items():
    norm = normalize(name)
    if norm:
        funding_norm[norm] = (name, amt)

# Count matches
count = 0
for proj in design_projects:
    norm_proj = normalize(proj)
    if not norm_proj:
        continue
    
    if norm_proj in funding_norm:
        count += 1
        continue
    
    for norm_f, (orig_f, amt_f) in funding_norm.items():
        if norm_proj in norm_f or norm_f in norm_proj:
            count += 1
            break
        
        if len(norm_proj) > 15 and len(norm_f) > 15:
            pw = set(norm_proj.split())
            fw = set(norm_f.split())
            if len(pw.intersection(fw)) >= 3:
                count += 1
                break

answer = {'count': count}
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
