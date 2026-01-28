code = """import json

# Access the actual data from the variables
civic_docs_data = var_functions.query_db:0
funding_data = var_functions.query_db:1

# Check the type of data
result = {
    'civic_docs_type': str(type(civic_docs_data)),
    'funding_data_type': str(type(funding_data)),
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:14': {'available_variables': ['var_functions.query_db:0', 'var_functions.query_db:1', '__builtins__', 'json']}}

exec(code, env_args)
