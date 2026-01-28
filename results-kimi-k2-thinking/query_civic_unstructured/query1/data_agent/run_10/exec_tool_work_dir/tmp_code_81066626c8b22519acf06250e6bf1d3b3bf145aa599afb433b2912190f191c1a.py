code = """import json, re, os, sys

# Get the stored results by reading from the JSON files
civic_file = '/tmp/tmpk6o6l8s9.json'
funding_file = '/tmp/tmp_5n4g1j5.json'

# Load civic documents
with open(civic_file) as f:
    civic_docs = json.load(f)

# Load funding records
with open(funding_file) as f:
    funding_records = json.load(f)

# Build funding lookup for amounts > $50,000
funding_lookup = {}
for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_lookup[rec['Project_Name']] = amount
    except:
        continue

# Extract capital projects in design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for capital projects in design phase
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Find the start position of the design section
    design_start = text.index('Capital Improvement Projects (Design)')
    
    # Find where this section ends
    design_end = len(text)
    section_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)', 
        'Disaster Recovery Projects',
        'PUBLIC WORKS QUARTERLY UPDATE'
    ]
    
    for marker in section_markers:
        pos = text.find(marker, design_start + 50)
        if pos > 0 and pos < design_end:
            design_end = pos
    
    # Extract the design section text
    design_section = text[design_start:design_end]
    lines = design_section.split('\n')
    
    # Process each line to find project names
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip header lines, update lines, etc.
        if any(skip in line for skip in ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:']):
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line and line[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        if any(word in line for word in ['Staff', 'City', 'Complete', 'Advertise']) and len(line.split()) < 5:
            continue
        
        # Clean up and add project name
        cleaned = line.strip('•-– ')
        if cleaned:
            design_projects.append(cleaned)

# Remove duplicates
design_projects = list(set(design_projects))

# Normalize project names for matching
def normalize_project_name(name):
    """Normalize project names for better matching"""
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '').replace('replacement', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Create normalized lookup for funding projects
funding_normalized = {}
for funding_name, amount in funding_lookup.items():
    normalized = normalize_project_name(funding_name)
    funding_normalized[normalized] = (funding_name, amount)

# Count matching projects
count = 0
matches = []

for design_proj in design_projects:
    norm_design = normalize_project_name(design_proj)
    
    # Direct match
    if norm_design in funding_normalized:
        count += 1
        funding_name, amount = funding_normalized[norm_design]
        matches.append({
            'design_project': design_proj,
            'funding_project': funding_name,
            'amount': amount
        })
        continue
    
    # Substring matching
    for norm_funding, (orig_funding, amount) in funding_normalized.items():
        if norm_design in norm_funding or norm_funding in norm_design:
            count += 1
            matches.append({
                'design_project': design_proj,
                'funding_project': orig_funding,
                'amount': amount
            })
            break
        
        # Word overlap matching for longer project names
        if len(norm_design) > 15 and len(norm_funding) > 15:
            design_words = set(norm_design.split())
            funding_words = set(norm_funding.split())
            
            if len(design_words.intersection(funding_words)) >= 3:
                count += 1
                matches.append({
                    'design_project': design_proj,
                    'funding_project': orig_funding,
                    'amount': amount
                })
                break

# Return the final count
result = {'count': count, 'sample_matches': matches[:5]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
