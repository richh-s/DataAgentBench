code = """import json, re

# Load the data
civic_docs_file = var_functions.query_db:5
funding_50k_file = var_functions.query_db:30

civic_docs = json.load(open(civic_docs_file))
funding_records = json.load(open(funding_50k_file))

funding_dict = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records}

design_projects = set()

# Look in Design sections
for doc in civic_docs:
    txt = doc.get('text', '')
    design_section = txt.split('Capital Improvement Projects (Design)')
    if len(design_section) > 1:
        design_text = design_section[1].split('Capital Improvement Projects (Construction)')[0]
        for line in design_text.split('\n'):
            clean = line.strip()
            if clean and clean in funding_dict:
                design_projects.add(clean)

# Search for other design projects
for project_name in funding_dict:
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
