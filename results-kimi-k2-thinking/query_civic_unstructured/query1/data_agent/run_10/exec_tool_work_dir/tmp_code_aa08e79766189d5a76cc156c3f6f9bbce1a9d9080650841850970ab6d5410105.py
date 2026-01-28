code = """import json, re

# Load data from the stored variables
civic_result = var_functions.query_db:2
funding_result = var_functions.query_db:5

# Load JSON files if needed
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result) as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result) as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

# Build funding lookup > $50k
funding_lookup = {}
for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_lookup[rec['Project_Name']] = amount
    except:
        continue

# Extract design projects from civic documents
design_list = []
header_terms = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Complete Design', 'Advertise', 'Begin Construction']

for doc in civic_docs:
    text = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Get design section boundaries
    design_start = text.find('Capital Improvement Projects (Design)')
    design_end = len(text)
    
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE']
    for marker in end_markers:
        marker_pos = text.find(marker, design_start + 50)
        if marker_pos > 0 and marker_pos < design_end:
            design_end = marker_pos
    
    section = text[design_start:design_end]
    lines = section.split('\n')
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        # Skip header/footer lines
        skip_line = False
        for term in header_terms:
            if term in stripped:
                skip_line = True
                break
        if skip_line:
            continue
        
        # Skip formatting
        if stripped and stripped[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        if stripped.isupper() and len(stripped) < 60:
            continue
        
        if len(stripped) < 10:
            continue
        
        # Skip update lines
        update_words = ['Staff', 'City', 'Complete', 'Advertise', 'Begin']
        if any(word in stripped for word in update_words) and len(stripped.split()) < 5:
            continue
        
        clean_name = stripped.strip('•-– ')
        if clean_name:
            design_list.append(clean_name)

# Remove exact duplicates
design_list = list(set(design_list))

# Normalize names for matching
def normalize_project(name):
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Build normalized funding lookup
funding_normalized = {}
for fname, famount in funding_lookup.items():
    normalized = normalize_project(fname)
    funding_normalized[normalized] = (fname, famount)

# Count matches
count = 0
matches = []

for design_name in design_list:
    norm_design = normalize_project(design_name)
    
    # Direct normalized match
    if norm_design in funding_normalized:
        count += 1
        orig_name, amount = funding_normalized[norm_design]
        matches.append({'design': design_name, 'funding': orig_name, 'amount': amount})
        continue
    
    # Substring match
    for norm_funding, (orig_funding, amount) in funding_normalized.items():
        if norm_design in norm_funding or norm_funding in norm_design:
            count += 1
            matches.append({'design': design_name, 'funding': orig_funding, 'amount': amount})
            break
        
        # Word overlap
        if len(norm_design) > 15 and len(norm_funding) > 15:
            d_words = set(re.findall(r'\b\w{4,}\b', norm_design))
            f_words = set(re.findall(r'\b\w{4,}\b', norm_funding))
            overlap = d_words.intersection(f_words)
            if len(overlap) >= 3:
                count += 1
                matches.append({'design': design_name, 'funding': orig_funding, 'amount': amount})
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
