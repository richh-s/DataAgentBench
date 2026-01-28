code = """import json

# Check what variables are available
available_vars = list(locals().keys())
print("Available variables:", available_vars)

# Try to access the MongoDB result from civic_docs_database
mongo_result_key = None
for key in available_vars:
    if 'query_db' in key and '2' in key:
        mongo_result_key = key
        break

print("MongoDB result key:", mongo_result_key)

if mongo_result_key:
    mongo_result = locals()[mongo_result_key]
    print("Mongo result type:", type(mongo_result))
    print("Mongo result value:", mongo_result[:200] if isinstance(mongo_result, str) else str(mongo_result)[:200])

# Also check for the first query result
first_result_key = None
for key in available_vars:
    if 'query_db' in key and '0' in key:
        first_result_key = key
        break

print("First result key:", first_result_key)
if first_result_key:
    first_result = locals()[first_result_key]
    print("First result type:", type(first_result))
    print("First result value preview:", str(first_result)[:300])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
