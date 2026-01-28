code = """import json

funding_data = locals()['var_functions.query_db:4']
civic_docs = locals()['var_functions.query_db:5']

print('Data loaded successfully')"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
