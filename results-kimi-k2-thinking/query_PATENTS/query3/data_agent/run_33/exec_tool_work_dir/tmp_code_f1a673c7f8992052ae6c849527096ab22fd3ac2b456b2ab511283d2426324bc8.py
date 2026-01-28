code = """import json
import re

# The result path is stored in the local namespace variable
# Let me check what's available
print('__RESULT__:')
print(json.dumps(list(locals().keys())))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
