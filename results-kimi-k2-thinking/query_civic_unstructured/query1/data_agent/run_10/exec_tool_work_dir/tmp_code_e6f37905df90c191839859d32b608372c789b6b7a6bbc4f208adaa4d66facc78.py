code = """import json
import re

# Access the file paths from the stored results
funding_file = var_functions.query_db:62
civic_file = var_functions.query_db:58

# Load funding data (already filtered for > $50,000)
with open(funding_file) as f:
    funding_records = json.load(f)

# Load civic documents
with open(civic_file) as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        funding_lookup[rec['Project_Name']] = amount
    except:
        continue

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Find section end
    design_end = len(text)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = text.find(marker, design_start + 50)
        if pos > 0:
            design_end = min(design_end, pos)
    
    # Process lines
    section = text[design_start:design_end]
    for line in section.split('\n'):
        line = line.strip()
        if len(line) < 10:
            continue
        
        # Skip headers
        if line.isupper() and len(line) < 60:
            continue
        
        # Skip unwanted patterns
        skip_patterns = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by:', 'Approved by:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']
        if any(p in line for p in skip_patterns):
            continue
        
        # Skip bullets
        if line and line[0] in ['•', '-', '◦', '(']:
            continue
        
        # Skip short updates
        skip_words = ['Staff', 'City', 'Complete', 'Advertise']
        if any(w in line for w in skip_words) and len(line.split()) < 5:
            continue
        
        clean = line.strip('•-—– ')
        if clean and clean not in design_projects:
            design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Normalize for matching
def normalize(n):
    n = n.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

# Build normalized lookup
funding_norm = {}
for name, amt in funding_lookup.items():
    norm = normalize(name)
    if norm:
        funding_norm[norm] = (name, amt)

# Count matches
count = 0
matches = []

for proj in design_projects:
    norm_proj = normalize(proj)
    if not norm_proj:
        continue
    
    # Direct match
    if norm_proj in funding_norm:
        count += 1
        orig, amt = funding_norm[norm_proj]
        matches.append({'design': proj, 'funding': orig, 'amount': amt})
        continue
    
    # Flexible match
    for norm_f, (orig_f, amt_f) in funding_norm.items():
        # Substring
        if norm_proj in norm_f or norm_f in norm_proj:
            count += 1
            matches.append({'design': proj, 'funding': orig_f, 'amount': amt_f})
            break
        
        # Word overlap
        if len(norm_proj) > 15 and len(norm_f) > 15:
            pw = set(norm_proj.split())
            fw = set(norm_f.split())
            if len(pw.intersection(fw)) >= 3:
                count += 1
                matches.append({'design': proj, 'funding': orig_f, 'amount': amt_f})
                break

print('__RESULT__:')
print(json.dumps({'count': count, 'sample_matches': matches[:5]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:50': {'test': 'test'}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
