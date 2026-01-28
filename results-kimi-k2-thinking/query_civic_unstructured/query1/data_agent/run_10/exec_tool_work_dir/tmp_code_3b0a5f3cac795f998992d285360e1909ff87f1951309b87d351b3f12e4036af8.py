code = """import json, re

# Load data directly from the variables
civic_data = var_functions.query_db:2
funding_data = var_functions.query_db:5

# Handle file path case for civic data
if isinstance(civic_data, str) and civic_data.endswith('.json'):
    with open(civic_data) as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_data

# Handle file path case for funding data  
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data) as f:
        funding_recs = json.load(f)
else:
    funding_recs = funding_data

# Build funding lookup for amounts > $50k
funding_over_50k = {}
for rec in funding_recs:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_over_50k[rec['Project_Name']] = amount
    except:
        continue

# Extract capital design projects from civic docs
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Find section
    start = text.index('Capital Improvement Projects (Design)')
    end = len(text)
    
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = text.find(marker, start + 50)
        if pos > 0:
            end = min(end, pos)
    
    # Get project names from this section
    section = text[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Skip headers
        if line.isupper() and len(line) < 60:
            continue
        
        # Skip various markers
        bad_markers = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']
        has_marker = False
        for marker in bad_markers:
            if marker in line:
                has_marker = True
                break
        if has_marker:
            continue
        
        # Skip bullets
        if line and line[0] in ['•', '-', '◦', '(']:
            continue
        
        # Skip short update lines
        skip_words = ['Staff', 'City', 'Complete', 'Advertise', 'Working', 'Submitted', 'Project is']
        has_short = False
        for word in skip_words:
            if word in line and len(line.split()) < 6:
                has_short = True
                break
        if has_short:
            continue
        
        # Add if not already there
        clean = line.strip('•-—– ')
        if clean and clean not in design_projects:
            design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Normalize for matching
def normalize(p):
    p = p.lower()
    p = re.sub(r'\s*\([^)]*\)$', '', p)
    p = p.replace('project', '')
    p = re.sub(r'[^a-z0-9\s]', '', p)
    return ' '.join(p.split())

# Build normalized lookup
funding_norm = {}
for name, amt in funding_over_50k.items():
    norm = normalize(name)
    if norm:
        funding_norm[norm] = (name, amt)

# Count matches
count = 0
for proj in design_projects:
    norm_proj = normalize(proj)
    if not norm_proj:
        continue
    
    # Direct match
    if norm_proj in funding_norm:
        count += 1
        continue
    
    # Flexible match
    matched = False
    for norm_f, (orig_f, amt_f) in funding_norm.items():
        # Substring
        if norm_proj in norm_f or norm_f in norm_proj:
            count += 1
            matched = True
            break
        
        # Word overlap for long names
        if len(norm_proj) > 15 and len(norm_f) > 15:
            d_words = set(norm_proj.split())
            f_words = set(norm_f.split())
            overlap = d_words.intersection(f_words)
            if len(overlap) >= 3:
                count += 1
                matched = True
                break
    
    if matched:
        continue

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:50': {'test': 'test'}}

exec(code, env_args)
