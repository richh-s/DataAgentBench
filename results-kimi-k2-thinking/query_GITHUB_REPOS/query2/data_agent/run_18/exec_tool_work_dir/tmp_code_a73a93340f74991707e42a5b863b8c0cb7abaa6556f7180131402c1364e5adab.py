code = """import json
import re
import os

# Load Swift repositories
swift_repos_data = var_functions.query_db:0
if isinstance(swift_repos_data, str) and os.path.exists(swift_repos_data):
    with open(swift_repos_data, 'r') as f:
        swift_repos = json.load(f)
else:
    swift_repos = swift_repos_data

# Load Swift files
swift_files_data = var_functions.query_db:2
if isinstance(swift_files_data, str) and os.path.exists(swift_files_data):
    with open(swift_files_data, 'r') as f:
        swift_files = json.load(f)
else:
    swift_files = swift_files_data

# Create lookup set for Swift repos
swift_repo_names = set(repo['repo_name'] for repo in swift_repos)

# Find max copies
max_copies = -1
max_file_info = None

for file_entry in swift_files:
    desc = file_entry.get('repo_data_description', '')
    
    # Skip binary files
    if 'binary' in desc.lower() and 'non-binary' not in desc.lower():
        continue
    
    # Extract copy count
    match = re.search(r'(\d+)\s+times?', desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            max_file_info = file_entry

# Build result
result = None
if max_file_info:
    repo_name = max_file_info['sample_repo_name']
    result = {
        'repository': repo_name,
        'file_id': max_file_info['id'],
        'file_path': max_file_info['sample_path'],
        'copy_count': max_copies,
        'is_swift_repository': repo_name in swift_repo_names
    }
else:
    result = {'error': 'No suitable files found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
