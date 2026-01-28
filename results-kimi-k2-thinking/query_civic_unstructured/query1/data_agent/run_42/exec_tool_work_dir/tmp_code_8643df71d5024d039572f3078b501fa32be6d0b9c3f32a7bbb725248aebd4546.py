code = """import json

# Access the stored result from the MongoDB query
mongo_result = var_functions.query_db_2

# Check if we can access it
print('Type of mongo_result:', type(mongo_result))
print('Value:', mongo_result[:100] if isinstance(mongo_result, str) else str(mongo_result)[:100])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
