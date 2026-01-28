code = """import json, re

civic_docs_file = locals()['var_functions.query_db:5']
funding_file = locals()['var_functions.query_db:30']

with open(civic_docs_file) as f:
    docs = json.load(f)

with open(funding_file) as f:
    funding = json.load(f)

# Build funding dict
funded = {rec['Project_Name']: int(rec['Amount']) for rec in funding}

capital_design = set()

for doc in docs:
    txt = doc.get('text', '')
    
    # Look in Design section
    start = txt.find('Capital Improvement Projects (Design)')
    if start != -1:
        end = txt.find('Capital Improvement Projects (Construction)', start)
        if end != -1:
            section = txt[start:end]
            for line in section.split('\n'):
                clean = line.strip()
                if clean and clean in funded:
                    capital_design.add(clean)

# Find other capital projects in design
for proj_name, amount in funded.items():
    if proj_name in capital_design:
        continue
    
    # Skip disaster projects (FEMA in name)
    if 'fema' in proj_name.lower():
        continue
    
    for doc in docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            idx = txt.find(proj_name)
            snippet = txt[max(0, idx-200):min(len(txt), idx+len(proj_name)+200)].lower()
            if 'design' in snippet:
                capital_design.add(proj_name)
                break

print('__RESULT__:')
print(str(len(capital_design)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
