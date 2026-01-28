code = """import json, re

civic_result = var_functions.query_db:2
funding_result = var_functions.query_db:5

# Load files if needed
civic_docs = json.load(open(civic_result)) if isinstance(civic_result, str) and civic_result.endswith('.json') else civic_result
funding_records = json.load(open(funding_result)) if isinstance(funding_result, str) and funding_result.endswith('.json') else funding_result

# Get funding > $50k
funding = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records if int(rec['Amount']) > 50000}

# Extract capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    start = text.find('Capital Improvement Projects (Design)')
    end = len(text)
    
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = text.find(marker, start + 50)
        if pos > 0:
            end = min(end, pos)
    
    section = text[start:end]
    lines = section.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers and update lines
        if any(x in line for x in ['Page', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Updates:', 'Project Schedule']):
            continue
        
        if line.isupper() and len(line) < 60:
            continue
        
        if line[0] in ['•', '-', '◦', '(', ')']:
            continue
        
        if any(word in line for word in ['Staff', 'City', 'Complete', 'Advertise']) and len(line.split()) < 5:
            continue
        
        clean = line.strip('•-– ')
        if clean:
            design_projects.append(clean)

design_projects = list(set(design_projects))

# Normalize and match
def normalize(n):
    n = n.lower()
    n = re.sub(r'\s*\([^)]*\)$', '', n)
    n = n.replace('project', '')
    n = re.sub(r'[^a-z0-9\s]', '', n)
    return ' '.join(n.split())

normalized_funding = {normalize(k): k for k, v in funding.items()}

count = 0
for dproj in design_projects:
    nd = normalize(dproj)
    
    if nd in normalized_funding:
        count += 1
        continue
    
    for nf, of in normalized_funding.items():
        if nd in nf or nf in nd:
            count += 1
            break
        
        if len(nd) > 15 and len(nf) > 15:
            dwords = set(re.findall(r'\b\w{4,}\b', nd))
            fwords = set(re.findall(r'\b\w{4,}\b', nf))
            if len(dwords.intersection(fwords)) >= 3:
                count += 1
                break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
