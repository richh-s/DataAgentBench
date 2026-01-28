code = """import json

# Read funding data
funding_file = var_functions.query_db:8
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data
civic_file = var_functions.query_db:9
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_data))

# Check first few funding records
print('\nFirst 5 funding records:')
for i, record in enumerate(funding_data[:5]):
    print(f"{i+1}. {record['Project_Name']} - ${record['Amount']}")

# Check civic document structure
print('\nFirst civic document keys:', list(civic_data[0].keys()))
print('\nSample text from first document (first 1000 chars):')
print(civic_data[0]['text'][:1000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
