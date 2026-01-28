code = """import json

# Access the MongoDB results
mongo_result = locals()['var_functions.query_db:2']
print('Mongo result type:', type(mongo_result))
print('Mongo result (first 200 chars):', str(mongo_result)[:200])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
