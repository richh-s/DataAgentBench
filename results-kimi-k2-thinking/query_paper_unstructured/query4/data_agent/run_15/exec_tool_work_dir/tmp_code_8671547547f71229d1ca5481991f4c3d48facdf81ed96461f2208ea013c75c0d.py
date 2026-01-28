code = """import json
import os

# Check the value and try to read it
result_var = var_functions.query_db:2
print(f"Result var type: {type(result_var)}")
print(f"Result var value: {result_var[:500] if isinstance(result_var, str) else str(result_var)[:500]}")

# If it's a file path, list files in current directory to see what's available
print("\nFiles in current directory:")
for f in os.listdir('.'):
    if f.endswith('.json'):
        print(f"  {f}")

# Try to access the variable from local context
try:
    data = json.loads(result_var)
    print(f"\nSuccessfully parsed JSON, found {len(data)} records")
    print('__RESULT__:')
    print(json.dumps({"record_count": len(data)}))
except Exception as e:
    print(f"\nError parsing: {e}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
