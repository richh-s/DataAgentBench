code = """# Read the raw file content to see what format we're dealing with
with open('var_functions.query_db:20.json', 'r') as f:
    content = f.read()

print(f"File length: {len(content)}")
print(f"First 500 chars:\n{content[:500]}")

# See if it looks like JSON
import json
try:
    data = json.loads(content)
    print(f"Successfully parsed JSON with {len(data)} records")
except Exception as e:
    print(f"JSON parse error: {e}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
