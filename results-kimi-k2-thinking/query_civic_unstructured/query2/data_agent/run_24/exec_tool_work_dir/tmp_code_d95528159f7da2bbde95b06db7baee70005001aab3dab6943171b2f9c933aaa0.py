code = """import json

# Get the file paths from the stored results
civic_docs_storage = locals()['var_functions.query_db:72']
funding_storage = locals()['var_functions.query_db:73']

print('Civic docs file:', civic_docs_storage)
print('Funding file:', funding_storage)

__RESULT__:
print('Files located')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs'], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
