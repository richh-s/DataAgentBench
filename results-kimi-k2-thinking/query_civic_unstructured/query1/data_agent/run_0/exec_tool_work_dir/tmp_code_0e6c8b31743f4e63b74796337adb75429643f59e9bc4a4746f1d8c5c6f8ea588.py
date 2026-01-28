code = """import json

# Try to access the funding data directly
funding_data_raw = var_functions.query_db:10
civic_docs_raw = var_functions.query_db:22

print('__RESULT__:')
print(json.dumps({
    'funding_data_type': str(type(funding_data_raw)),
    'civic_docs_type': str(type(civic_docs_raw)),
    'funding_data_preview': str(funding_data_raw)[:200]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'funding_path': 'file_storage/functions.query_db:10.json', 'civic_path': 'file_storage/functions.query_db:6.json', 'funding_path_type': "<class 'str'>", 'civic_path_type': "<class 'str'>"}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
