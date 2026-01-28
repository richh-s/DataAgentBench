code = """import json
import re
import pandas as pd

storage_keys = [key for key in vars().keys() if key.startswith('var_')]
result = {'storage_keys': storage_keys}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
