code = """import json, re

# Get stored variables
civic_key = 'var_functions.query_db:2'
funding_key = 'var_functions.query_db:5'

all_vars = locals()
civic_docs = all_vars.get(civic_key)
funding_recs = all_vars.get(funding_key)

# Load JSON files if strings
import os
if isinstance(civic_docs, str) and os.path.exists(civic_docs):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

if isinstance(funding_recs, str) and os.path.exists(funding_recs):
    with open(funding_recs) as f:
        funding_recs = json.load(f)

# Build funding lookup > $50,000
funding_over_50k = {}
for rec in funding_recs:
    try:
        amt = int(rec['Amount'])
        if amt > 50000:
            funding_over_50k[rec['Project_Name']] = amt
    except:
        pass

# Extract capital design projects from civic docs
capital_design = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_marker = 'Capital Improvement Projects (Design)'
    if design_marker not in text:
        continue
    
    start = text.find(design_marker)
    section_end = len(text)
    
    # Find end of section
    for end_marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = text.find(end_marker, start + 50)
        if pos > 0:
            section_end = min(section_end, pos)
    
    # Get section text and split lines
    design_section = text[start:section_end]
    lines = [l.strip() for l in design_section.split('\n') if l.strip()]
    
    for line in lines:
        # Skip short lines
        if len(line) < 10:
            continue
        
        # Skip obvious non-project lines
        skip_words = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']
        has_skip = any(word in line for word in skip_words)
        if has_skip:
            continue
        
        # Skip all-caps headers
        if line.isupper() and len(line) < 60:
            continue
        
        # Skip bullet points and parens
        if line and line[0] in ['•', '-', '◦', '■', '(']:
            continue
        
        # Skip update lines (short with keywords)
        short_words = ['Staff', 'City', 'Complete', 'Advertise', 'Working', 'Submitted']
        if any(w in line for w in short_words) and len(line.split()) < 6:
            continue
        
        clean_name = line.strip('•-—–  ')
        if clean_name and clean_name not in capital_design:
            capital_design.append(clean_name)

# Normalize project names for matching
def normalize_project_name(name):
    if not name:
        return ''
    # Lowercase and remove trailing parentheses content
    n = name.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    # Remove common project-related words
    n = n.replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '').replace('replacement', '')
    # Remove special characters
    n = re.sub(r'[^a-z0-9\s]', '', n)
    # Normalize whitespace
    return ' '.join(n.split())

# Build normalized funding lookup
funding_lookup_normalized = {}
for proj_name, amount in funding_over_50k.items():
    norm_name = normalize_project_name(proj_name)
    if norm_name:
        funding_lookup_normalized[norm_name] = (proj_name, amount)

# Count matching projects using flexible matching
count = 0
for design_proj in capital_design:
    norm_design = normalize_project_name(design_proj)
    if not norm_design:
        continue
    
    # Direct normalized match
    if norm_design in funding_lookup_normalized:
        count += 1
        continue
    
    # Check for partial/substring matches and word overlap
    matched = False
    for norm_funding, (orig_funding, amount) in funding_lookup_normalized.items():
        # Substring matching in either direction
        if norm_design in norm_funding or norm_funding in norm_design:
            count += 1
            matched = True
            break
        
        # Word overlap matching for longer project names
        if len(norm_design) > 15 and len(norm_funding) > 15:
            design_words = set(norm_design.split())
            funding_words = set(norm_funding.split())
            common_words = design_words.intersection(funding_words)
            if len(common_words) >= 3:
                count += 1
                matched = True
                break
    
    if matched:
        continue

# Return final answer
print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
