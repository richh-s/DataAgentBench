code = """import json
import re
from datetime import datetime

# Get the civic documents data from the storage variable
civic_docs_result = var_functions.query_db:5

# Check if it's a file path or actual data
if isinstance(civic_docs_result, str) and '/tmp/' in civic_docs_result:
    with open(civic_docs_result, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs_result

# Get the funding data from the storage variable
funding_result = var_functions.query_db:6

# Check if it's a file path or actual data
if isinstance(funding_result, str) and '/tmp/' in funding_result:
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs_data),
    'funding_records_count': len(funding_data),
    'sample_doc': civic_docs_data[0].get('text', '')[:500] if civic_docs_data else 'No data'
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
