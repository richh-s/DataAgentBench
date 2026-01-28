code = """import json

# Load a small sample of funding data to check structure
funding_file = locals()['var_functions.query_db:64']
with open(funding_file, 'r') as f:
    funding_sample = json.load(f)

# Examine the structure
print('Total records:', len(funding_sample))
if funding_sample:
    sample_record = funding_sample[0]
    print('Sample record keys:', list(sample_record.keys()))
    print('Sample record:', sample_record)

# Check civic docs structure too
civic_file = locals()['var_functions.query_db:40']
with open(civic_file, 'r') as f:
    civic_sample = json.load(f)

print('Total civic docs:', len(civic_sample))
if civic_sample:
    sample_doc = civic_sample[0]
    print('Civic doc keys:', list(sample_doc.keys()))
    print('Sample civic doc text snippet:', sample_doc.get('text', '')[:200])

# Print the actual data paths being used
print('Funding file:', funding_file)
print('Civic file:', civic_file)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
