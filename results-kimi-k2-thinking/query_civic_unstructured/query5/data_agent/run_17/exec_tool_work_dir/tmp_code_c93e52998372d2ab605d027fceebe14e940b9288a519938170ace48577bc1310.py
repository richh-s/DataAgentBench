code = """import json, os, re
# Load funding data
funding_path = locals().get('var_functions.query_db:2')
print('Funding data path:', funding_path)
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
    print('Number of funding records:', len(funding_data))
    print('Sample funding records:')
    for rec in funding_data[:5]:
        print(rec)
else:
    print('Funding path is not a JSON file')

print('\n' + '='*50 + '\n')

# Load civic documents
civic_path = locals().get('var_functions.query_db:8')
print('Civic documents path:', civic_path)
if isinstance(civic_path, str) and civic_path.endswith('.json'):
    with open(civic_path, 'r') as f:
        civic_data = json.load(f)
    print('Number of civic documents:', len(civic_data))
    print('Sample civic document:')
    if civic_data:
        doc = civic_data[0]
        print('Filename:', doc.get('filename'))
        print('Text snippet:')
        print(doc.get('text')[:1000])
else:
    print('Civic path is not a JSON file')"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
