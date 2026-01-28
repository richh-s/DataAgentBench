code = """import json, re

# Access the stored variables using locals()
civic_var = locals().get('var_functions.query_db:2')
funding_var = locals().get('var_functions.query_db:5')

# Load data from JSON files if needed
if isinstance(civic_var, str) and civic_var.endswith('.json'):
    with open(civic_var) as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_var

if isinstance(funding_var, str) and funding_var.endswith('.json'):
    with open(funding_var) as f:
        funding_records = json.load(f)
else:
    funding_records = funding_var

# Build funding lookup for projects > $50,000
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
    
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    design_end = len(text)
    
    # Find section end
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects', 'PUBLIC WORKS QUARTERLY UPDATE']:
        pos = text.find(marker, design_start + 50)
        if pos > 0:
            design_end = min(design_end, pos)
    
    section = text[design_start:design_end]
    lines = section.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers, footers, update lines
        if any(skip in line for skip in ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:']):
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line and line[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        if any(word in line for word in ['Staff', 'City', 'Complete', 'Advertise']) and len(line.split()) < 5:
            continue
        
        cleaned = line.strip('•-– ')
        if cleaned:
            design_projects.append(cleaned)

# Remove duplicates
design_projects = list(set(design_projects))

# Normalize names for flexible matching
def normalize_name(name):
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '').replace('replacement', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Build normalized funding lookup
funding_normalized = {}
for funding_name, amount in funding_lookup.items():
    norm = normalize_name(funding_name)
    funding_normalized[norm] = (funding_name, amount)

# Count matches
count = 0
for design_proj in design_projects:
    norm_design = normalize_name(design_proj)
    
    # Direct normalized match
    if norm_design in funding_normalized:
        count += 1
        continue
    
    # Flexible substring matching
    for norm_funding, (orig_funding, amount) in funding_normalized.items():
        if norm_design in norm_funding or norm_funding in norm_design:
            count += 1
            break
        
        # Word overlap for longer names
        if len(norm_design) > 15 and len(norm_funding) > 15:
            design_words = set(norm_design.split())
            funding_words = set(norm_funding.split())
            if len(design_words.intersection(funding_words)) >= 3:
                count += 1
                break

# Return final answer
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
