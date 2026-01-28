code = """import json

fund_path = var_call_nYjJ4kxOjBZ2kYVMCMRSOBrL
with open(fund_path, 'r') as f:
    funding = json.load(f)
fund_projects = {r['Project_Name'] for r in funding}

civic_path = var_call_c8SLOLDsXLD0XVSWokAYJKiQ
with open(civic_path, 'r') as f:
    docs = json.load(f)

# Define 'design' status as any document text containing the project name in same doc that mentions '(Design)'
# More strict: only count if doc mentions 'Capital Improvement Projects (Design)' or 'Disaster Recovery Projects (Design)'

design_docs_text = []
for d in docs:
    t = d.get('text','')
    if ('Projects (Design)' in t) or ('Projects (Design'.lower() in t.lower()):
        if ('Capital Improvement Projects (Design)'.lower() in t.lower()) or ('Disaster Recovery Projects (Design)'.lower() in t.lower()):
            design_docs_text.append(t)

design_text = "\n".join(design_docs_text).lower()

matched = set()
for p in fund_projects:
    if p and p.lower() in design_text:
        matched.add(p)

print('__RESULT__:')
print(json.dumps({'count': len(matched)}))"""

env_args = {'var_call_cOYTFJ37fsmQ6vsv2BI5aIEd': ['Funding'], 'var_call_CoJ4YHLU3kaME3EK9Gh9N7k7': ['civic_docs'], 'var_call_nYjJ4kxOjBZ2kYVMCMRSOBrL': 'file_storage/call_nYjJ4kxOjBZ2kYVMCMRSOBrL.json', 'var_call_c8SLOLDsXLD0XVSWokAYJKiQ': 'file_storage/call_c8SLOLDsXLD0XVSWokAYJKiQ.json'}

exec(code, env_args)
