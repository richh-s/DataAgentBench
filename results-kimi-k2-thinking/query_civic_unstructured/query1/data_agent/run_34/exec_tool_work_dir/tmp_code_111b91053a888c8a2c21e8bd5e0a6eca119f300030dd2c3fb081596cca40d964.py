code = """import json
import pandas as pd
import re

# Load civic_docs data from file
civic_docs_path = '/tmp/tmpvdv4v8m8.json'
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Load funding data from file
funding_path = '/tmp/tmpxm6h7qwk.json'
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs_data),
    'funding_records_count': len(funding_data),
    'sample_text': civic_docs_data[0]['text'][:300]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
