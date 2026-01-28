code = """import json, os, re
print('Starting data analysis')
funding_path = locals().get('var_functions.query_db:14')
print('funding_path type:', type(funding_path))

# Read funding data
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = []

print('Funding records:', len(funding_data))

# Read civic data
civic_path = locals().get('var_functions.query_db:8')
print('civic_path type:', type(civic_path))
if isinstance(civic_path, str) and civic_path.endswith('.json'):
    with open(civic_path, 'r') as f:
        civic_data = json.load(f)
else:
    civic_data = []

print('Civic documents:', len(civic_data))

# Find disaster projects with 2022 dates
disaster_projs = []
for doc in civic_data:
    text = doc.get('text', '')
    # Find project blocks with potential dates
    for line in text.splitlines():
        if any(k in line for k in ['(FEMA', '(CalJPIA', '(CalOES']):
            if '2022' in text and ('Start' in text or 'Begin' in text or '2022-' in text or '2022-' in line):
                disaster_projs.append(line.strip())

print('Potential disaster projects with 2022 mention:', len(disaster_projs))
for dp in disaster_projs[:10]:
    print('  -', dp[:100])

# Simple matching from funding data
disaster_names = set()
for f in funding_data:
    pname = f.get('Project_Name', '')
    if any(indicator in pname for indicator in ['(FEMA', '(CalJPIA', '(CalOES']):
        disaster_names.add(pname)

print('Disaster projects in funding DB:', len(disaster_names))

# Sum funding for these
amount = sum(int(f.get('Amount', 0)) for f in funding_data 
             if f.get('Project_Name') in disaster_names)
print('Total funding for disaster projects:', amount)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
