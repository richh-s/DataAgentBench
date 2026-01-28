code = """import json

# Get the file paths from the stored variables
civic_docs_path = var_functions.query_db_14
funding_path = var_functions.query_db_3

# civic_docs_path = '/tmp/tmp2d2u8k1a.json'
# funding_path = '/tmp/tmp0k5s9q8h.json'

print('civic_docs_path:', civic_docs_path)
print('funding_path:', funding_path)

# Read civic documents
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded civic_docs:', len(civic_docs))
print('Loaded funding_data:', len(funding_data))

# Show summary of funding data
print('\nSample funding records:')
for i in range(min(3, len(funding_data))):
    print(f"  {funding_data[i]}")

# Show summary of civic docs
print('\nSample civic doc:')
print(f"  Filename: {civic_docs[0].get('filename')}")
print(f"  Text length: {len(civic_docs[0].get('text', ''))}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
