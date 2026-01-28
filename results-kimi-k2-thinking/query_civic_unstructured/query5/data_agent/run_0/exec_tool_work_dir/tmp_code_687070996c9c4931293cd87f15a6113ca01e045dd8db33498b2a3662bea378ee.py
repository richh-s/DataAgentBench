code = """import json
import os

# Check what type of data we have
funding_key = 'var_functions.query_db:2'
civic_key = 'var_functions.query_db:3'

funding_data = locals()[funding_key]
civic_data = locals()[civic_key]

print('__RESULT__:')
print(json.dumps({
    'funding_type': str(type(funding_data)),
    'funding_preview': str(funding_data)[:200] if not isinstance(funding_data, str) else 'file_path',
    'civic_type': str(type(civic_data)),
    'civic_preview': str(civic_data)[:200] if not isinstance(civic_data, str) else civic_data[:200]
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
