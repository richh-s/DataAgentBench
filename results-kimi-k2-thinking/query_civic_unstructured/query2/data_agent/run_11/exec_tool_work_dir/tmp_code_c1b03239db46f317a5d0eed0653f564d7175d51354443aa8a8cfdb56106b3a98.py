code = """import json
import re

# Load civic documents data
civic_docs_file = '/tmp/tmp6m4v1i6w.json'  # This appears to be the temp file path
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

# Load funding data
funding_file = '/tmp/tmpv4a3m3o7.json'  # This appears to be the temp file path for funding
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs_data),
    'funding_records_count': len(funding_data),
    'civic_docs_sample': civic_docs_data[0] if civic_docs_data else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
