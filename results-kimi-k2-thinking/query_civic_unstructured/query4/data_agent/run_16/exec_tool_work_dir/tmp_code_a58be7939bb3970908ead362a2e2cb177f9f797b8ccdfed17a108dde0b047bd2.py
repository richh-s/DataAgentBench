code = """import json

# First, let's check what we have access to
test_data = {
    'civic_docs_path': str(var_functions.query_db_6),
    'funding_path': str(var_functions.query_db_10)
}

print('DEBUG Access test:')
for key, value in test_data.items():
    print(f'  {key}: {value}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
