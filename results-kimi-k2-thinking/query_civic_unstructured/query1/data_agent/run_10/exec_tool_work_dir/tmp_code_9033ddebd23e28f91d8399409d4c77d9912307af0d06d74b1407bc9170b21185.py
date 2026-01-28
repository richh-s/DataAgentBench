code = """import json, re

# Load civic documents
civic_result = locals()['var_functions.query_db:2']
funding_result = locals()['var_functions.query_db:5']

# Handle JSON file loading
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
funding_map = {}
for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        if amount > 50000:
            funding_map[rec['Project_Name'].strip()] = amount
    except:
        continue

# Find capital projects in design status
all_design = []
skip_headers = ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by']

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    start = text.index('Capital Improvement Projects (Design)')
    end = len(text)
    
    # Find section end
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = text.find(marker, start + 50)
        if pos > 0:
            end = min(end, pos)
    
    section = text[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip unwanted lines
        if any(h in line for h in skip_headers):
            continue
        if line.isupper() and len(line) < 60:
            continue
        if line and line[0] in ['•', '-', '◦', '(', ')']:
            continue
        if any(w in line for w in ['Staff', 'City', 'Complete', 'Advertise']) and len(line.split()) < 5:
            continue
        if 'Updates:' in line or 'Project Schedule:' in line or 'Estimated Schedule:' in line:
            continue
        
        clean = line.strip('•-– ')
        if clean:
            all_design.append(clean)

all_design = list(set(all_design))

# Normalize and match
def normalize(n):
    n = n.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '').replace('improvements', '').replace('improvement', '')
    n = n.replace('repairs', '').replace('repair', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

funding_norm = {normalize(k): (k, v) for k, v in funding_map.items()}

count = 0
for project in all_design:
    norm_proj = normalize(project)
    
    # Direct match
    if norm_proj in funding_norm:
        count += 1
        continue
    
    # Substring match or word overlap
    for norm_fund, (orig_fund, amount) in funding_norm.items():
        if norm_proj in norm_fund or norm_fund in norm_proj:
            count += 1
            break
        
        if len(norm_proj) > 15 and len(norm_fund) > 15:
            proj_words = set(norm_proj.split())
            fund_words = set(norm_fund.split())
            if len(proj_words.intersection(fund_words)) >= 3:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
