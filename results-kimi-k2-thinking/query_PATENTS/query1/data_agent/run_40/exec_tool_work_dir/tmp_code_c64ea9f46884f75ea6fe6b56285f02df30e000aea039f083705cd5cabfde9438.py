code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the result from the file
file_path = locals()['var_functions.query_db:2']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        records = json.load(f)
else:
    records = locals()['var_functions.query_db:2']

# Print first record to understand structure
print('__RESULT__:')
if records:
    result = json.dumps({
        'first_record_keys': list(records[0].keys()),
        'sample_cpc': records[0].get('cpc', '')[:200],
        'sample_pub_date': records[0].get('publication_date', '')
    })
    print(result)
else:
    print(json.dumps({'error': 'no records'}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
