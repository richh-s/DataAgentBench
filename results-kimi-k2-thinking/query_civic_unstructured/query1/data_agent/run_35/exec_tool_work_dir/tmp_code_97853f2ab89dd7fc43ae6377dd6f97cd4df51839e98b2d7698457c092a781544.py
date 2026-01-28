code = """# Access the data directly from variables
import json

# The query results should be available as variables
# Let's check what variables are available
variables = list(locals().keys())
print('__RESULT__:')
print(json.dumps({'available_variables': variables[:20]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
