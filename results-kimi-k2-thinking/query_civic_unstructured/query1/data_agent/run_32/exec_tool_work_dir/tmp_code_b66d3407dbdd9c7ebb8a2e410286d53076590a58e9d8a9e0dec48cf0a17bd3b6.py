code = """import json
import re

civic_docs_path = var_functions.query_db:5
funding_path = var_functions.query_db:2

# Load data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Build funding dict
funding_dict = {}
for rec in funding_records:
    amt = int(rec.get('Amount', 0))
    if amt > 50000:
        funding_dict[rec.get('Project_Name', '')] = amt

found_projects = set()

# First pass: look in Design sections
for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        parts = txt.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_lines = parts[1].split('Capital Improvement Projects (Construction)')[0].split('\n')
            for line in design_lines:
                clean = line.strip()
                if len(clean) < 5 or clean.startswith('cid:') or clean.startswith('(cid:'):
                    continue
                skip_terms = ['Complete Design:', 'Advertise:', 'Begin Construction:', 'Final Design:', 'Project Schedule:', 'Updates:']
                if any(term in clean for term in skip_terms):
                    continue
                if clean.startswith('●') or clean.startswith('•'):
                    continue
                if 'Project is' in clean:
                    continue
                
                clean = re.sub(r'\(cid:\d+\)', '', clean).strip()
                if clean in funding_dict:
                    found_projects.add(clean)

# Second pass: broader search
for proj_name in funding_dict:
    if proj_name in found_projects:
        continue
    for doc in civic_docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            idx = txt.find(proj_name)
            context = txt[max(0, idx-300):min(len(txt), idx+len(proj_name)+300)].lower()
            if 'design' in context and 'fema' not in proj_name.lower() and 'disaster' not in context:
                found_projects.add(proj_name)
                break

count = len(found_projects)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
