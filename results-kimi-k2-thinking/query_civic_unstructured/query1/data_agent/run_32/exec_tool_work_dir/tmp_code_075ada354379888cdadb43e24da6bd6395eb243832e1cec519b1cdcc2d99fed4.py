code = """import json, re

civic_docs = json.load(open(var_functions.query_db:5))
funding_records = json.load(open(var_functions.query_db:2))

funding = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records if int(rec['Amount']) > 50000}

found = set()

for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        part = txt.split('Capital Improvement Projects (Design)')[1].split('Capital Improvement Projects (Construction)')[0]
        for line in part.split('\n'):
            clean = line.strip()
            if len(clean) < 5: continue
            if clean.startswith('cid:'): continue
            if 'Complete Design:' in clean: continue
            if 'Advertise:' in clean: continue
            if 'Begin Construction:' in clean: continue
            if 'Final Design:' in clean: continue
            if 'Project Schedule:' in clean: continue
            if 'Updates:' in clean: continue
            if 'Project is' in clean: continue
            clean = clean.replace('(cid:190)', '').replace('(cid:131)', '').strip()
            if clean in funding:
                found.add(clean)

for proj in funding:
    if proj in found: continue
    for doc in civic_docs:
        txt = doc.get('text', '')
        if proj in txt:
            idx = txt.find(proj)
            ctx = txt[max(0, idx-300):min(len(txt), idx+len(proj)+300)].lower()
            if 'design' in ctx and 'fema' not in proj.lower():
                found.add(proj)
                break

print('__RESULT__:')
print(json.dumps(str(len(found))))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
