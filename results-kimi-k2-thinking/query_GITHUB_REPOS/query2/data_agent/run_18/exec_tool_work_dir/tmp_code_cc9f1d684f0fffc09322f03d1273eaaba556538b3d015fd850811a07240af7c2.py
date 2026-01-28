code = """import json
import re

# Access variables using locals() to handle the colon in variable names
swift_repos_var = locals()['var_functions.query_db:0']
swift_files_var = locals()['var_functions.query_db:2']

# Load data from files if needed
if isinstance(swift_repos_var, str) and swift_repos_var.endswith('.json'):
    with open(swift_repos_var, 'r') as f:
        swift_repos = json.load(f)
else:
    swift_repos = swift_repos_var

if isinstance(swift_files_var, str) and swift_files_var.endswith('.json'):
    with open(swift_files_var, 'r') as f:
        swift_files = json.load(f)
else:
    swift_files = swift_files_var

# Create set of Swift repository names
swift_repo_set = set(repo['repo_name'] for repo in swift_repos)

# Find the non-binary Swift file with the most copies
max_copies = 0
best_file = None

for file_info in swift_files:
    desc = file_info.get('repo_data_description', '')
    
    # Skip if binary file
    if 'binary' in desc.lower():
        if 'non-binary' not in desc.lower():
            continue
    
    # Check for copy count
    match = re.search(r'(\d+)\s+times?', desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            repo_name = file_info['sample_repo_name']
            if repo_name in swift_repo_set:
                max_copies = copies
                best_file = file_info

result = None
if best_file:
    result = {
        'repository': best_file['sample_repo_name'],
        'file_id': best_file['id'],
        'file_path': best_file['sample_path'],
        'copy_count': max_copies
    }
else:
    result = {'error': 'No suitable Swift files found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
