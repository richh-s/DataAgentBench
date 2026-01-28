code = """# Get all local variables
all_vars = locals()
query_result = all_vars.get('var_functions.query_db:0')
print("Query result variable:", query_result)

if query_result:
    import json
    with open(query_result, 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data)} records")
    print("__RESULT__:")
    print(json.dumps(data[:5]))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "Query result not found"}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
