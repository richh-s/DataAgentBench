code = """import json, re

civic_docs_path = var_functions.query_db:5 + ''
funding_path = var_functions.query_db:30 + ''

civic_docs = json.load(open(civic_docs_path))
funding_records = json.load(open(funding_path))

funding_50k = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records}

design_projects = set()

for doc in civic_docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        part = txt.split('Capital Improvement Projects (Design)')[1].split('Capital Improvement Projects (Construction)')[0]
        for line in part.split('\n'):
            clean = line.strip()
            if clean and clean in funding_50k:
                design_projects.add(clean)

for project_name in funding_50k:
    if project_name in design_projects:
        continue
    
    for doc in civic_docs:
        txt = doc.get('text', '')
        if project_name in txt:
            idx = txt.find(project_name)
            snippet = txt[max(0, idx-200):min(len(txt), idx+len(project_name)+200)]
            
            if 'design' in snippet.lower() and 'fema' not in project_name.lower():
                design_projects.add(project_name)
                break

print('__RESULT__:')
print(str(len(design_projects)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
