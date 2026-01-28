code = """import json, re

# Load funding data
f = open(var_functions.query_db:0)
funding_data = json.load(f)
f.close()

# Load civic docs  
f = open(var_functions.query_db:2)
civic_docs = json.load(f)
f.close()

# Get projects with funding > 50k
high_funding = set()
for r in funding_data:
    if int(r['Amount']) > 50000:
        high_funding.add(r['Project_Name'])

# Extract capital design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    
    design_section = text[start + 37:]
    for m in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        end = design_section.find(m)
        if end != -1:
            design_section = design_section[:end]
            break
    
    for block in design_section.split('\n\n'):
        block = block.strip()
        if block and len(block) > 10:
            line = block.split('\n')[0].strip()
            if len(line) > 10 and not line.isupper():
                clean = re.sub(r'^[A-Z]\.\s*', '', line)
                clean = re.sub(r'^\d+\.\s*', '', clean)
                if len(clean) > 10:
                    design_projects.append(clean)

# Match
normalize = lambda x: re.sub(r'[^a-z0-9]', '', x.lower().strip())
matched = 0
for p in design_projects:
    p_norm = normalize(p)
    if len(p_norm) < 8:
        continue
    for f in high_funding:
        f_norm = normalize(f)
        if p_norm == f_norm or (len(p_norm) > 12 and p_norm in f_norm) or (len(f_norm) > 12 and f_norm in p_norm):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
