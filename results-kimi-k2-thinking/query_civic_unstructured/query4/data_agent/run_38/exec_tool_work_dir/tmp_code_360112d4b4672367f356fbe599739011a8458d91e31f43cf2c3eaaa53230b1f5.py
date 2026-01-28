code = """import json

# Load civic docs data from file
civic_docs_file = '/var/results/var_functions.query_db:2.json'

# Read the full data
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

# Load funding data from file
funding_file = '/var/results/var_functions.query_db:8.json'

# Read the funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Number of civic documents: {len(civic_docs_data)}")
print(f"Number of funding records: {len(funding_data)}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
