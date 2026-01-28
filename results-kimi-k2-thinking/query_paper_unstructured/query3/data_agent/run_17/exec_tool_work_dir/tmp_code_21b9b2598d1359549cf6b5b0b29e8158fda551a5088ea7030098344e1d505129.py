code = """# Let's see what variables are available in storage
import json
print('Available variables:')
for key in list(locals().keys()):
    if key.startswith('var_'):
        print(f'{key}: {locals()[key]}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
