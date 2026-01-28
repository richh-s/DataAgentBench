code = """import json, re

# Get the stored results from the local variables
civic_key = 'var_functions.query_db:2'
funding_key = 'var_functions.query_db:5'

all_vars = locals()
civic_data = all_vars.get(civic_key)
funding_data = all_vars.get(funding_key)

# Load JSON if needed
if isinstance(civic_data, str) and civic_data.endswith('.json'):
    with open(civic_data) as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_data

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data) as f:
        funding_recs = json.load(f)
else:
    funding_recs = funding_data

# Build funding lookup for projects > $50k
funding_map = {}
for rec in funding_recs:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_map[rec['Project_Name']] = amount
    except:
        continue

# Extract capital design projects from civic docs
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find capital design projects section
    design_section_start = 'Capital Improvement Projects (Design)'
    if design_section_start not in text:
        continue
    
    start = text.find(design_section_start)
    end = len(text)
    
    # Find section end
    end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE']
    for marker in end_markers:
        pos = text.find(marker, start + 50)
        if pos > 0 and pos < end:
            end = pos
    
    # Extract potential project names
    section = text[start:end]
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    
    for line in lines:
        if len(line) < 10:
            continue
        
        # Skip headers, update lines, etc.
        if any(skip in line for skip in ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by:', 'Approved by:', 'Updates', 'Project Schedule']):
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line and line[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        skip_words = ['Staff', 'City', 'Complete', 'Advertise', 'Begin Construction',
                     'Advertise:', 'Begin Construction:', 'Complete Design:', 'Estimated Schedule:',
                     'Project Schedule:', 'Updates:']
        if any(word in line for word in skip_words) and len(line.split()) < 6:
            continue
        
        clean_project = line.strip('•-– ')
        if clean_project and clean_project not in design_projects:
            design_projects.append(clean_project)

# Remove duplicates
design_projects = list(set(design_projects))

# Normalize project names for matching
def normalize_project_name(name):
    if not name:
        return ''
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '').replace('replacement', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Create normalized funding lookup
funding_normalized = {}
for proj_name, amount in funding_map.items():
    norm_name = normalize_project_name(proj_name)
    if norm_name:
        funding_normalized[norm_name] = (proj_name, amount)

# Count matching projects
count = 0
for design_proj in design_projects:
    norm_design = normalize_project_name(design_proj)
    if not norm_design:
        continue
    
    # Check for direct match
    if norm_design in funding_normalized:
        count += 1
        continue
    
    # Check for substring matches in either direction
    matched = False
    for norm_fproj, (orig_fproj, amount) in funding_normalized.items():
        if norm_design in norm_fproj or norm_fproj in norm_design:
            count += 1
            matched = True
            break
        
        # Word-level matching for longer names
        if len(norm_design) > 15 and len(norm_fproj) > 15:
            d_words = set(norm_design.split())
            f_words = set(norm_fproj.split())
            common = d_words.intersection(f_words)
            if len(common) >= 3:
                count += 1
                matched = True
                break
    
    if matched:
        continue

# Return the total count
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
