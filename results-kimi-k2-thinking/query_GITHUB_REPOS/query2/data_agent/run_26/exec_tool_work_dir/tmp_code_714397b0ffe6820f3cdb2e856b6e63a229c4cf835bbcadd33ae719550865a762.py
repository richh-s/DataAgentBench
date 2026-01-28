code = """import json
import re

# Get the data from locals since variable names with colons are not valid syntax
swift_files = locals()['var_functions.query_db:10']

print(f"Found {len(swift_files)} Swift files")
print(f"First few files: {swift_files[:2]}")

# Parse repo_data_description to extract copy counts and identify non-binary files
file_copy_counts = {}

for file_info in swift_files:
    description = file_info.get('repo_data_description', '')
    file_id = file_info.get('id')
    
    # Check if it's non-binary by looking for key phrases
    if 'non-binary' in description.lower() or 'duplicated' in description.lower() or 'copied' in description.lower():
        # Extract copy count using regex - look for patterns like "X times"
        match = re.search(r'(\d+) times|duplicated (\d+) times|copied (\d+) times|seen (\d+) times', description)
        if match:
            # Get the first non-None group (the actual number)
            copy_count = int([g for g in match.groups() if g is not None][0])
            file_copy_counts[file_id] = {
                'count': copy_count,
                'repo': file_info.get('sample_repo_name'),
                'path': file_info.get('sample_path'),
                'description': description
            }

print(f"Found {len(file_copy_counts)} non-binary Swift files with copy counts")

# Find the file with the highest copy count
if file_copy_counts:
    max_file_id = max(file_copy_counts.keys(), key=lambda x: file_copy_counts[x]['count'])
    max_file = file_copy_counts[max_file_id]
    print(f"Most copied file: {max_file_id}")
    print(f"Copy count: {max_file['count']}")
    print(f"Repository: {max_file['repo']}")
    print(f"Path: {max_file['path']}")
else:
    print("No non-binary Swift files found")
    max_file = None
    max_file_id = None

result = {
    'total_swift_files': len(swift_files),
    'non_binary_files': len(file_copy_counts),
    'max_copies': max_file['count'] if max_file else 0,
    'max_file_id': max_file_id,
    'max_file_repo': max_file['repo'] if max_file else None,
    'max_file_path': max_file['path'] if max_file else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': []}

exec(code, env_args)
