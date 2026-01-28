code = """import json

# Read civic documents
civic_docs_path = '/tmp/tmp2d2u8k1a.json'
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_path = '/tmp/tmp0k5s9q8h.json'
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded civic_docs:', len(civic_docs))
print('Loaded funding_data:', len(funding_data))

# Show first few funding records to understand structure
print('\nFirst 5 funding records:')
for i in range(min(5, len(funding_data))):
    print(funding_data[i])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
