code = """import json, re

# Load data from stored variables
civic_docs = locals()['var_functions.query_db:58']
funding_records = locals()['var_functions.query_db:56']

# Load JSON files if needed
if isinstance(civic_docs, str):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

if isinstance(funding_records, str):
    with open(funding_records) as f:
        funding_records = json.load(f)

# Build funding lookup for projects > $50,000
funding_lookup = {}
for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_lookup[rec['Project_Name']] = amount
    except:
        continue

# Extract capital design projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find capital improvement projects in design phase
    design_marker = 'Capital Improvement Projects (Design)'
    if design_marker not in text:
        continue
    
    # Get section boundaries
    start = text.find(design_marker)
    end = len(text)
    
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE']
    for marker in end_markers:
        pos = text.find(marker, start + 50)
        if pos > 0 and pos < end:
            end = pos
    
    # Process lines
    section = text[start:end]
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    
    for line in lines:
        if len(line) < 10:
            continue
        
        # Skip headers
        if line.isupper() and len(line) < 60:
            continue
        
        # Skip unwanted content
        skip_content = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']
        has_skip = any(s in line for s in skip_content)
        if has_skip:
            continue
        
        # Skip bullets and parens
        if line and line[0] in ['•', '-', '◦', '(']:
            continue
        
        # Skip short update lines
        skip_words = ['Staff', 'City', 'Complete', 'Advertise', 'Working', 'Submitted', 'Project is']
        if any(w in line for w in skip_words) and len(line.split()) < 6:
            continue
        
        clean = line.strip('•-—– ')
        if clean and clean not in design_projects:
            design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Normalize names for flexible matching
def normalize_project_name(name):
    if not name:
        return ''
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Build normalized funding lookup
funding_normalized = {}
for proj_name, amount in funding_lookup.items():
    norm = normalize_project_name(proj_name)
    if norm:
        funding_normalized[norm] = (proj_name, amount)

# Count matching projects
count = 0
for dproj in design_projects:
    norm_d = normalize_project_name(dproj)
    if not norm_d:
        continue
    
    # Direct match
    if norm_d in funding_normalized:
        count += 1
        continue
    
    # Flexible matching
    matched = False
    for norm_f, (orig_f, amt_f) in funding_normalized.items():
        # Substring match
        if norm_d in norm_f or norm_f in norm_d:
            count += 1
            matched = True
            break
        
        # Word overlap for long names
        if len(norm_d) > 15 and len(norm_f) > 15:
            dwords = set(norm_d.split())
            fwords = set(norm_f.split())
            if len(dwords.intersection(fwords)) >= 3:
                count += 1
                matched = True
                break
    
    if matched:
        continue

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:50': {'test': 'test'}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
