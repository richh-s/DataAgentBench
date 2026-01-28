code = """import json
import re

# Read the Swift files data from the file path
swift_files_file = locals()['var_functions.query_db:22']
try:
    with open(swift_files_file, 'r') as f:
        swift_files = json.load(f)
except Exception as e:
    print(f"Error reading file: {e}")
    swift_files = []

print(f"Total Swift files to analyze: {len(swift_files)}")

# Parse repo_data_description to extract copy counts for non-binary files
file_copy_data = {}

for file_info in swift_files:
    if not isinstance(file_info, dict):
        continue
        
    description = file_info.get('repo_data_description', '')
    file_id = file_info.get('id')
    
    # Extract copy count using regex patterns looking for numbers followed by "times"
    match = re.search(r'(\d+)\s*(?:times|times,|times\))', description)
    if match:
        copy_count = int(match.group(1))
        file_copy_data[file_id] = {
            'count': copy_count,
            'repo': file_info.get('sample_repo_name'),
            'path': file_info.get('sample_path'),
            'description': description
        }

print(f"Files with extractable copy counts: {len(file_copy_data)}")

# Find the file with the highest copy count
if file_copy_data:
    max_file_id = max(file_copy_data.keys(), key=lambda x: file_copy_data[x]['count'])
    max_file = file_copy_data[max_file_id]
    
    print(f"Most frequently copied file ID: {max_file_id}")
    print(f"Copy count: {max_file['count']}")
    print(f"Repository: {max_file['repo']}")
    print(f"Path: {max_file['path']}")
    
    result = {
        'max_copies': max_file['count'],
        'file_id': max_file_id,
        'repository': max_file['repo'],
        'file_path': max_file['path'],
        'description': max_file['description']
    }
else:
    print("No valid copy count data found")
    result = {}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'type': "<class 'str'>", 'length': 105}}

exec(code, env_args)
