code = """import json
import re

# Check what variables are available
print('__RESULT__:')
print(json.dumps({
    'mongo_var': str(var_functions.query_db:2)[:100],
    'citations_var': str(var_functions.query_db:5)[:100]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
