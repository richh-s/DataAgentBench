code = """import json
import os

# Read the file path
file_path = locals()['var_functions.query_db:22']
print('File path type:', type(file_path))
print('File path:', str(file_path)[:100])

# Read the content
with open(file_path, 'r') as file_handle:
    content = file_handle.read()

print('Content length:', len(content))
print('First 200 chars:', content[:200])
print('Last 50 chars:', content[-50:])

# Try to parse the JSON content
try:
    data = json.loads(content)
    print('Successfully parsed JSON, records:', len(data))
except Exception as e:
    print('JSON parse error:', str(e))

print('\n__RESULT__:')
print(json.dumps('completed'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
