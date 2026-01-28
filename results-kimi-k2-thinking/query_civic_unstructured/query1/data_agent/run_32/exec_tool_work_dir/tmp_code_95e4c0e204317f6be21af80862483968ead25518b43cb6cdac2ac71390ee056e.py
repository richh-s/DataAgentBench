code = """import json
# Load the data files (they are JSON files in storage)
civic_file = locals()['var_functions.query_db:5']
funding_file = locals()['var_functions.query_db:30']

# First try to load the data
try:
    with open(civic_file) as f:
        docs = json.load(f)
except:
    # If it's a list already
    docs = locals()['var_functions.query_db:5']

try:
    with open(funding_file) as f:
        funding = json.load(f)
except:
    # If it's a list already
    funding = locals()['var_functions.query_db:30']

# Build funding dictionary for 50k+ projects
funded = {}
for rec in funding:
    name = rec['Project_Name']
    amt = int(rec['Amount'])
    funded[name] = amt

# Look for capital design projects in documents
capital_design = set()

for doc in docs:
    txt = doc.get('text', '')
    
    # Find Design section for Capital Improvement Projects
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt.split('Capital Improvement Projects (Design)')[1]
        next_section = section.split('Capital Improvement Projects (Construction)')[0]
        
        # Check each line for project names
        for line in next_section.split('\n'):
            clean = line.strip()
            if clean and clean in funded:
                capital_design.add(clean)

# Also search in general text
for proj_name in funded:
    if proj_name in capital_design:
        continue
    
    # Skip FEMA/disaster projects
    if 'fema' in proj_name.lower():
        continue
    
    # Check if mentioned anywhere
    for doc in docs:
        txt = doc.get('text', '')
        if proj_name in txt:
            capital_design.add(proj_name)
            break

result = len(capital_design)
print('__RESULT__:')
print(str(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
