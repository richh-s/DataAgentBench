code = """import json

# Load data from storage
civic_docs_file = locals()['var_functions.query_db:5']
funding_file = locals()['var_functions.query_db:30']

with open(civic_docs_file) as f:
    docs = json.load(f)

with open(funding_file) as f:
    funding = json.load(f)

# Create mapping from project name to amount
funded = {}
for rec in funding:
    name = rec['Project_Name']
    amt = int(rec['Amount'])
    funded[name] = amt

# Find capital projects with design status
capital_design = set()

for doc in docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt.split('Capital Improvement Projects (Design)')[1]
        section = section.split('Capital Improvement Projects (Construction)')[0]
        
        for line in section.split('\n'):
            clean = line.strip()
            if clean in funded:
                capital_design.add(clean)

# Extended search for capital design projects
for proj_name in funded:
    if proj_name in capital_design:
        continue
    
    # Skip disaster projects
    if 'fema' in proj_name.lower():
        continue
    
    for doc in docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            capital_design.add(proj_name)
            break

count = len(capital_design)
print('__RESULT__:')
print(str(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
