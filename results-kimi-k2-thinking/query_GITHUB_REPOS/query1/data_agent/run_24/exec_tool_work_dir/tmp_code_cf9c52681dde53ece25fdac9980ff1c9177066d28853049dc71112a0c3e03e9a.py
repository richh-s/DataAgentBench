code = """import json
import re

# Check the structure of the data
languages_result = locals()['var_functions.query_db:0']
readme_result = locals()['var_functions.query_db:2']

# Check what we're dealing with
print('__RESULT__:')
print(json.dumps({
    'languages_type': str(type(languages_result)),
    'languages_preview': str(languages_result)[:200],
    'readme_type': str(type(readme_result)),
    'readme_preview': str(readme_result)[:200]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
