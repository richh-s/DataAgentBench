code = """import json
import re

# Read stored query results
civic_docs_result = globals()['var_functions.query_db:0']
funding_result = globals()['var_functions.query_db:2']

# Load data based on whether it's already a list or a file path
civic_docs = civic_docs_result if isinstance(civic_docs_result, list) else json.load(open(civic_docs_result))
funding_data = funding_result if isinstance(funding_result, list) else json.load(open(funding_result))

# Show basic info
print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_data), 'funding records')

# Show sample records
sample_doc = civic_docs[0] if civic_docs else {}
sample_funding = funding_data[0] if funding_data else {}

print('Sample civic doc keys:', list(sample_doc.keys()))
print('Sample funding record:', sample_funding)

# Store counts for final result
counts = {
    'civic_docs': len(civic_docs),
    'funding_records': len(funding_data),
    'sample_civic_keys': list(sample_doc.keys()),
    'sample_funding': sample_funding
}

print('__RESULT__:')
print(json.dumps(counts))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
