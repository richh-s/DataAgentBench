code = """import json

# Debug the data structures first
civics = var_functions.query_db:2
funds = var_functions.query_db:5

# Determine what type of data we're getting
print('__RESULT__:')
print(json.dumps({
    'civic_type': str(type(civics)),
    'civic_is_str': isinstance(civics, str),
    'funding_type': str(type(funds)),
    'funding_is_str': isinstance(funds, str)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
