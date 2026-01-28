code = """import json
import re
from collections import defaultdict

# Load the civic docs data
civic_docs_key = 'var_functions.query_db:0'
civic_docs_path = locals()[civic_docs_key]
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_key = 'var_functions.query_db:1'
funding_path = locals()[funding_key]
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert funding amounts to integer for summing
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Print size information
print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data),
    'sample_civic_doc_keys': list(civic_docs[0].keys()) if civic_docs else [],
    'sample_funding_keys': list(funding_data[0].keys()) if funding_data else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
