code = """import json

# Load data files
f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:7']

with open(f_path) as f:
    funding = json.load(f)
with open(c_path) as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding))
print('Civic docs:', len(civic_docs))
print('Sample disaster projects from funding:')

# Look at FEMA/CalOES/etc projects in funding
disaster_funding = {}
for r in funding:
    name = r.get('Project_Name', '')
    amount = int(r.get('Amount', 0))
    if 'FEMA' in name.upper() or 'CALOES' in name.upper() or 'CALJPIA' in name.upper():
        disaster_funding[name] = disaster_funding.get(name, 0) + amount

for name, amt in list(disaster_funding.items())[:10]:
    print(f'  {name}: ${amt}')

# Search civic docs for projects with 2022 dates
doc_text = civic_docs[0].get('text', '')
lines = doc_text.split('\n')
print('\nLooking for 2022 dates in text:')
for line in lines:
    if '2022' in line:
        print(f'  {line.strip()}')

print('__RESULT__:')
print(json.dumps({'funding_count': len(funding), 'civic_docs_count': len(civic_docs), 'disaster_funding_count': len(disaster_funding)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
