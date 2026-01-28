code = """import json

civic_docs_path = var_functions.query_db:5
funding_path = var_functions.query_db:2

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_dict = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if amount > 50000:
        funding_dict[name] = amount

design_projects = set()

# Method 1: Look in Design sections
for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        parts = txt.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            for line in section.split('\n'):
                clean = line.strip()
                if len(clean) < 5:
                    continue
                if clean.startswith('cid:') or clean.startswith('(cid:'):
                    continue
                skip_terms = ['Complete Design:', 'Advertise:', 'Begin Construction:']
                if any(term in clean for term in skip_terms):
                    continue
                skip_terms2 = ['Final Design:', 'Project Schedule:', 'Updates:']
                if any(term in clean for term in skip_terms2):
                    continue
                if 'Project is' in clean:
                    continue
                
                # Remove cid markers
                clean = clean.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                
                if clean and clean in funding_dict:
                    design_projects.add(clean)

# Method 2: Broad search
for proj_name in funding_dict:
    if proj_name in design_projects:
        continue
    
    for doc in civic_docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            idx = txt.find(proj_name)
            context = txt[max(0, idx-300):min(len(txt), idx+len(proj_name)+300)].lower()
            
            if 'design' in context and 'fema' not in proj_name.lower():
                design_projects.add(proj_name)
                break

count = len(design_projects)
print('__RESULT__:')
print(str(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
