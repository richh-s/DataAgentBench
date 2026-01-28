code = """import json

civic_docs_path = locals()['var_functions.query_db:5']
funding_path = locals()['var_functions.query_db:30']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_records = json.load(f)

funding_dict = {rec['Project_Name']: int(rec['Amount']) for rec in funding_records}

# Look for capital projects with design status
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the Design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start != -1:
        section = text[design_start:text.find('Capital Improvement Projects (Construction)')]
        
        # For each line in that section
        for line in section.split('\n'):
            clean = line.strip()
            if len(clean) > 4 and clean in funding_dict:
                design_projects.add(clean)

# Extended search
for project_name in funding_dict:
    if project_name in design_projects:
        continue
    
    for doc in civic_docs:
        text = doc.get('text', '')
        if project_name in text:
            idx = text.find(project_name)
            snippet = text[max(0, idx-200):min(len(text), idx+len(project_name)+200)]
            
            if 'design' in snippet.lower() and 'fema' not in project_name.lower():
                design_projects.add(project_name)
                break

print('__RESULT__:')
print(str(len(design_projects)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
