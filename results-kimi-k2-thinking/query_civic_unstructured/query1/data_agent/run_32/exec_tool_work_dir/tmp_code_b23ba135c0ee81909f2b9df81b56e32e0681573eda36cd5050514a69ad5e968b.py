code = """import json

# Access the data from storage variables
civic_docs = var_functions.query_db:5
funding = var_functions.query_db:30

# If they are file paths, load them
if isinstance(civic_docs, str):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

if isinstance(funding, str):
    with open(funding) as f:
        funding = json.load(f)

# Build funding map for 50k+ projects
funded = {}
for rec in funding:
    funded[rec['Project_Name']] = int(rec['Amount'])

# Find capital design projects
capital_design = set()

for doc in civic_docs:
    txt = doc.get('text', '')
    
    # Look in Design section
    if 'Capital Improvement Projects (Design)' in txt:
        section = txt.split('Capital Improvement Projects (Design)')[1]
        section = section.split('Capital Improvement Projects (Construction)')[0]
        
        for line in section.split('\n'):
            clean = line.strip()
            if clean in funded:
                capital_design.add(clean)

# Count
result = len(capital_design)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
