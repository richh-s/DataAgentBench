code = """import json, re

# Load data
civic_docs = locals()['var_functions.query_db:2']
funding_records = locals()['var_functions.query_db:5']

# Handle file cases
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

if isinstance(funding_records, str) and funding_records.endswith('.json'):
    with open(funding_records) as f:
        funding_records = json.load(f)

# Funding > $50k
funding = {}
for rec in funding_records:
    try:
        a = int(rec['Amount'])
        if a > 50000:
            funding[rec['Project_Name']] = a
    except:
        continue

# Extract design projects
design = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    marker = 'Capital Improvement Projects (Design)'
    if marker not in text:
        continue
    
    start = text.index(marker)
    end = len(text)
    
    # Find end of section
    for m in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        p = text.find(m, start + 50)
        if p > 0 and p < end:
            end = p
    
    # Extract lines that look like project names
    section = text[start:end]
    lines = section.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        if line.isupper() and len(line) < 60:
            continue
        
        # Skip bullet points  
        if line and line[0] in '•-◦(':
            continue
        
        # Skip update lines
        if any(x in line for x in ['Updates:', 'Project Schedule', 'Estimated Schedule', 'RECOMMENDED ACTION', 'DISCUSSION', 'Prepared by', 'Approved by', 'Complete Design:', 'Advertise:', 'Begin Construction:']):
            continue
        
        if any(word in line for word in ['Staff', 'City', 'Complete', 'Advertise']) and len(line.split()) < 5:
            continue
        
        if 'Page' in line or 'Agenda Item' in line:
            continue
        
        clean = line.strip('•-– ')
        if clean:
            design.append(clean)

# Remove duplicates
design = list(set(design))

# Match projects using flexible string matching
def normalize_name(n):
    n = n.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    n = ' '.join(n.split())
    return n

# Build normalized funding lookup
funding_norm = {}
for fund_name, amount in funding.items():
    norm_name = normalize_name(fund_name)
    funding_norm[norm_name] = (fund_name, amount)

# Count matches
count = 0
for proj in design:
    norm_proj = normalize_name(proj)
    
    # Direct match
    if norm_proj in funding_norm:
        count += 1
        continue
    
    # Try substring matches
    matched = False
    for n_fund, (o_fund, amt) in funding_norm.items():
        if norm_proj in n_fund or n_fund in norm_proj:
            count += 1
            matched = True
            break
        
        # Word-level matching for complex names
        if len(norm_proj) > 15 and len(n_fund) > 15:
            proj_words = set(norm_proj.split())
            fund_words = set(n_fund.split())
            if len(proj_words.intersection(fund_words)) >= 3:
                count += 1
                matched = True
                break
    
    if matched:
        continue

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
