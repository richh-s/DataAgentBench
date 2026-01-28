code = """import json, os

vars_dict = locals()
print('Keys:', vars_dict.keys())

# Check what files we have
files = [f for f in os.listdir('/tmp') if f.endswith('.json')]
print('JSON files:', files)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
