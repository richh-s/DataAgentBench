code = """import json, os

# List available variables starting with var_
for var_name in list(locals().keys()):
    if var_name.startswith('var_'):
        print(f"Variable: {var_name}")

# Check var_functions.query_db:2
if 'var_functions.query_db:2' in locals():
    result = locals()['var_functions.query_db:2']
    print(f"\nvar_functions.query_db:2 is a {type(result).__name__}")
    if isinstance(result, str) and '.json' in result:
        print(f"File path: {result}")
        if os.path.exists(result):
            print("File exists")
            with open(result, 'r') as f:
                data = json.load(f)
                print(f"Loaded {len(data)} records")
                # Show sample data
                for i, rec in enumerate(data[:5]):
                    print(f"  {i+1}: {rec.get('Patents_info', '')[:100]}")
        else:
            print("File does not exist")
    else:
        print(f"Value: {str(result)[:200]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
