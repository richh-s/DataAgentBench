code = """import json
import re

# Check what type of data we have
swift_files_data = locals()['var_functions.query_db:22']
print(f"Type of swift_files_data: {type(swift_files_data)}")
print(f"Content preview: {str(swift_files_data)[:200]}")

# If it's a string (file path), read the file
if isinstance(swift_files_data, str):
    try:
        with open(swift_files_data, 'r') as f:
            swift_files = json.load(f)
        print(f"Loaded {len(swift_files)} Swift files from file")
    except Exception as e:
        print(f"Error reading file: {e}")
        swift_files = []
else:
    swift_files = swift_files_data

print('__RESULT__:')
print(json.dumps({'type': str(type(swift_files_data)), 'length': len(swift_files) if isinstance(swift_files, list) else 0}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
