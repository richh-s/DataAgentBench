code = """import json

# Access stored results using safer method
query_results = list(dir())
mongo_key = None
funding_key = None
for key in query_results:
    if 'query_db_2' in key:
        mongo_key = key
    if 'query_db_6' in key:
        funding_key = key

print('Mongo key:', mongo_key)
print('Funding key:', funding_key)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
