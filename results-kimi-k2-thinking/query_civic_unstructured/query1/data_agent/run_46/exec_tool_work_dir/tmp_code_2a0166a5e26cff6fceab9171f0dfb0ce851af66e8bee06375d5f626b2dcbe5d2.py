code = """import json, re, os

# Debug: list available variables
available_vars = [name for name in dir() if name.startswith('var_')]

# Load the data using the correct variable names
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:8

result = {
    'funding_file_exists': os.path.exists(funding_path),
    'civic_file_exists': os.path.exists(civic_path),
    'funding_path': funding_path,
    'civic_path': civic_path
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
