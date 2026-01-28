code = """import json, re

# Load data
civic_docs = json.load(open(str(var_functions.query_db:5)))
funding_recs = json.load(open(str(var_functions.query_db:30)))

# Build funding dictionary
funding = {r['Project_Name']: int(r['Amount']) for r in funding_recs}

design = set()

# Search for capital projects in design sections
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        part = text.split('Capital Improvement Projects (Design)')[1]
        part = part.split('Capital Improvement Projects (Construction)')[0]
        for line in part.split('\n'):
            clean = line.strip()
            if len(clean) > 4 and clean in funding:
                design.add(clean)

# Find other potential matches
for proj in funding:
    if proj in design: continue
    
    for doc in civic_docs:
        text = doc.get('text', '')
        if proj in text:
            pos = text.find(proj)
            snippet = text[max(0, pos-200):min(len(text), pos+len(proj)+200)]
            
            if 'design' in snippet.lower() and 'fema' not in proj.lower():
                design.add(proj)
                break

print('__RESULT__:')
print(str(len(design)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
