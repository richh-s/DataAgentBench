code = """import json

# Check what variables are available
available_vars = list(locals().keys())

# Find the MongoDB query result
mongo_key = None
for key in available_vars:
    if 'query_db' in key and ('2' in key or '1' in key):
        mongo_key = key
        break

if mongo_key:
    mongo_result = locals()[mongo_key]
    result_info = {
        "key": mongo_key,
        "type": str(type(mongo_result)),
        "length": len(mongo_result) if hasattr(mongo_result, '__len__') else None
    }
else:
    result_info = {"error": "MongoDB result key not found", "available_vars": available_vars[:10]}

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
