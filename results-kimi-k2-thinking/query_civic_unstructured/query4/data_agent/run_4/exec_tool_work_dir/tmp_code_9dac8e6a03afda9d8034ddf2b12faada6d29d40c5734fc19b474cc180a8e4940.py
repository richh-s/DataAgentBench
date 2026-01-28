code = """import json
import re
from datetime import datetime

# Load the full MongoDB results from the file
civic_docs_file = var_functions.list_db:0
civic_docs = []
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_file if isinstance(civic_docs_file, list) else []

# Load the full Funding data from the file
funding_file = var_functions.query_db:4
funding_data = []
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file if isinstance(funding_file, list) else []

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_data_count': len(funding_data),
    'first_doc_keys': list(civic_docs[0].keys()) if civic_docs else [],
    'first_funding_keys': list(funding_data[0].keys()) if funding_data else []
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
