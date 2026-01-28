code = """import json, re

# Load the data from stored variables
civic_docs = var_functions.query_db:2
funding_records = var_functions.query_db:5

# If they're file paths, load them
if isinstance(civic_docs, str):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

if isinstance(funding_records, str):
    with open(funding_records) as f:
        funding_records = json.load(f)

# Build funding lookup (project_name -> amount) for projects > $50,000
funding_lookup = {}
for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_lookup[rec['Project_Name']] = amount
    except:
        continue

# Extract capital projects with 'design' status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    section_marker = 'Capital Improvement Projects (Design)'
    
    if section_marker not in text:
        continue
    
    # Find the design section
    start = text.find(section_marker)
    end = len(text)
    
    # Find end of the section
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE']
    for marker in end_markers:
        pos = text.find(marker, start + 50)
        if pos > 0:
            end = min(end, pos)
    
    # Process lines in this section
    section = text[start:end]
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    
    for line in lines:
        if len(line) < 10:
            continue
        
        # Skip various non-project lines
        skip_patterns = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']
        has_skip = any(pattern in line for pattern in skip_patterns)
        if has_skip:
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line and line[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        skip_words = ['Staff', 'City', 'Complete', 'Advertise', 'Working', 'Submitted', 'Project is']
        if any(word in line for word in skip_words) and len(line.split()) < 6:
            continue
        
        clean_name = line.strip('•-—–  ')
        if clean_name and clean_name not in design_projects:
            design_projects.append(clean_name)

# Remove duplicates
design_projects = list(set(design_projects))

# Normalize names for matching
def normalize_name(name):
    if not name:
        return ''
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Build normalized funding lookup
funding_norm = {}
for fname, famount in funding_lookup.items():
    norm = normalize_name(fname)
    if norm:
        funding_norm[norm] = (fname, famount)

# Count matches
count = 0
matches = []

for dproject in design_projects:
    norm_d = normalize_name(dproject)
    if not norm_d:
        continue
    
    # Direct match
    if norm_d in funding_norm:
        count += 1
        orig, amt = funding_norm[norm_d]
        matches.append({'design': dproject, 'funding': orig, 'amount': amt})
        continue
    
    # Flexible matching
    matched = False
    for norm_f, (orig_f, amt_f) in funding_norm.items():
        # Substring match
        if norm_d in norm_f or norm_f in norm_d:
            count += 1
            matches.append({'design': dproject, 'funding': orig_f, 'amount': amt_f})
            matched = True
            break
        
        # Word overlap
        if len(norm_d) > 15 and len(norm_f) > 15:
            dwords = set(norm_d.split())
            fwords = set(norm_f.split())
            if len(dwords.intersection(fwords)) >= 3:
                count += 1
                matches.append({'design': dproject, 'funding': orig_f, 'amount': amt_f})
                matched = True
                break
    
    if matched:
        continue

# Get final count
final_result = {'total_count': count}
print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
