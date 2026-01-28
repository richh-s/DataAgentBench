code = """import json, re

# Access stored data variables
civic_data = var_functions.query_db:2
funding_data = var_functions.query_db:5

# Load JSON files if needed
civic_docs = json.load(open(civic_data)) if isinstance(civic_data, str) else civic_data
funding_records = json.load(open(funding_data)) if isinstance(funding_data, str) else funding_data

# Build funding lookup: project_name -> amount for projects > $50k
funding_lookup = {}
skip_values = ['Page', 'Agenda Item', 'RECOMMENDED ACTION']

for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            pname = rec['Project_Name'].strip()
            funding_lookup[pname] = amount
    except:
        continue

# Extract capital projects with design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    section_marker = 'Capital Improvement Projects (Design)'
    
    if section_marker not in text:
        continue
    
    # Find the design section
    start_idx = text.find(section_marker)
    end_idx = len(text)
    
    # Find section boundaries
    for end_marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE']:
        marker_pos = text.find(end_marker, start_idx + len(section_marker))
        if marker_pos > 0 and marker_pos < end_idx:
            end_idx = marker_pos
    
    # Extract project names from this section
    section = text[start_idx:end_idx]
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    
    for line in lines:
        if len(line) < 10:
            continue
        
        # Skip lines with headers, footers, updates
        contains_skip = False
        for skip_term in ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Complete Design', 'Advertise', 'Begin Construction']:
            if skip_term in line:
                contains_skip = True
                break
        if contains_skip:
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line and line[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        skip_words = ['Staff', 'City', 'Complete', 'Advertise']
        if any(word in line for word in skip_words) and len(line.split()) < 5:
            continue
        
        clean_line = line.strip('•-– ')
        if clean_line and clean_line not in design_projects:
            design_projects.append(clean_line)

# Match projects using normalized string comparison
def normalize(name):
    if not name:
        return ''
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)  # Remove parenthetical suffixes
    n = n.replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)  # Remove special chars
    return ' '.join(n.split())  # Normalize whitespace

# Create normalized version of funding lookup
funding_norm = {}
for proj_name, amount in funding_lookup.items():
    norm_name = normalize(proj_name)
    if norm_name:
        funding_norm[norm_name] = (proj_name, amount)

# Count matches
count = 0
for dproj in design_projects:
    norm_dproj = normalize(dproj)
    if not norm_dproj:
        continue
    
    # Check for direct match
    if norm_dproj in funding_norm:
        count += 1
        continue
    
    # Check for substring matches
    matched = False
    for norm_fproj, (orig_fproj, amount) in funding_norm.items():
        # Substring match in either direction
        if norm_dproj in norm_fproj or norm_fproj in norm_dproj:
            count += 1
            matched = True
            break
        
        # Word-level matching for longer names (>= 3 matching words)
        if len(norm_dproj) > 15 and len(norm_fproj) > 15:
            d_words = set(norm_dproj.split())
            f_words = set(norm_fproj.split())
            common = d_words.intersection(f_words)
            if len(common) >= 3:
                count += 1
                matched = True
                break
    
    if matched:
        continue

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
