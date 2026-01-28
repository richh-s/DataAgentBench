code = """import json
import re
from collections import defaultdict

# Load the civic docs data
civic_docs_path = var_functions.query_db:0
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = var_functions.query_db:1
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integer for summing
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Print sizes
print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
