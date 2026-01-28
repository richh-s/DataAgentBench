code = """# First, let's see sample data from both databases
import json
print('__RESULT__:')
print('Loading publicationinfo sample...')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition']}

exec(code, env_args)
