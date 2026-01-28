code = """import json

# Just load the data to see what we're working with
print('Loading funding data...')
funding_path = locals()['var_functions.query_db:40']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f'Number of funding records: {len(funding_data)}')
print(f'First few records:')
for i, rec in enumerate(funding_data[:5]):
    print(f'  {rec}')

print('\nLoading civic documents...')
civic_path = locals()['var_functions.query_db:5']
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

print(f'Number of civic docs: {len(civic_docs)}')
print(f'First doc preview:')
if civic_docs:
    print(f'  Filename: {civic_docs[0].get("filename")}')
    print(f'  Text length: {len(civic_docs[0].get("text", ""))}')
    
print('\\n__RESULT__:')
print(json.dumps({'status': 'loaded'}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
