code = """import json

# Check the type and content of the stored result
result = var_functions.query_db:0
print(f"Type: {type(result)}")
print(f"Content: {str(result)[:500]}")  # Print first 500 chars 

# If it's a string (file path), read it
if isinstance(result, str):
    try:
        with open(result, 'r') as f:
            data = json.load(f)
        print(f"Loaded {len(data)} records")
        print(f"First record: {data[0]}")
    except Exception as e:
        print(f"Error reading file: {e}")
else:
    print(f"Data is already a list with {len(result)} records")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
