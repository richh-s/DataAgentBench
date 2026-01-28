code = """import json

# Check what variables are available in local scope
available_vars = [var for var in locals().keys() if not var.startswith('__')]
print("Available variables:", available_vars)

# Let's try to find the MongoDB results
if 'functions.query_db:0' in globals():
    result = globals()['functions.query_db:0']
    print("Found in globals")
    print(type(result))
    print(result[:500] if isinstance(result, str) else len(result))
else:
    print("Not found in globals")

if 'functions.query_db:0' in locals():
    result = locals()['functions.query_db:0']
    print("Found in locals")
    print(type(result))
    print(result[:500] if isinstance(result, str) else len(result))
else:
    print("Not found in locals")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
