code = """import json
import re

# Load the Swift repositories list
swift_repos_file = var_functions.query_db:0
if isinstance(swift_repos_file, str) and swift_repos_file.endswith('.json'):
    with open(swift_repos_file, 'r') as f:
        swift_repos = json.load(f)
else:
    swift_repos = var_functions.query_db:0

# Load the Swift files data
swift_files_file = var_functions.query_db:2
if isinstance(swift_files_file, str) and swift_files_file.endswith('.json'):
    with open(swift_files_file, 'r') as f:
        swift_files = json.load(f)
else:
    swift_files = var_functions.query_db:2

print(f"Number of Swift repositories: {len(swift_repos)}")
print(f"Number of Swift files: {len(swift_files)}")

# Create a set of Swift repo names for quick lookup
swift_repo_names = set(repo['repo_name'] for repo in swift_repos)

# Parse copy counts from repo_data_description
file_copy_counts = []

for file_info in swift_files:
    description = file_info.get('repo_data_description', '')
    
    # Check if it's non-binary (avoid binary files)
    if 'binary' in description.lower() and 'non-binary' not in description.lower():
        continue
        
    # Look for copy/duplicate count patterns
    copy_match = re.search(r'(duplicated|copied|appearing|appears)\s+(\d+)\s+times?', description, re.IGNORECASE)
    if copy_match:
        copy_count = int(copy_match.group(2))
        file_copy_counts.append({
            'id': file_info['id'],
            'repo_name': file_info['sample_repo_name'],
            'path': file_info['sample_path'],
            'copy_count': copy_count,
            'description': description
        })

# Sort by copy count descending
file_copy_counts.sort(key=lambda x: x['copy_count'], reverse=True)

# Get the file with maximum copy count
max_copy_file = None
is_swift_repo = False

if file_copy_counts:
    max_copy_file = file_copy_counts[0]
    print(f"File with max copies: ID={max_copy_file['id']}, Copies={max_copy_file['copy_count']}, Repo={max_copy_file['repo_name']}")
    
    # Check if the repository is in our Swift repos list
    is_swift_repo = max_copy_file['repo_name'] in swift_repo_names
    print(f"Is Swift repository: {is_swift_repo}")
    
    # Get top 10 files for verification
    print("\nTop 10 files by copy count:")
    for i, file_info in enumerate(file_copy_counts[:10]):
        in_swift_list = file_info['repo_name'] in swift_repo_names
        print(f"{i+1}. Copies: {file_info['copy_count']}, Repo: {file_info['repo_name']} (Swift: {in_swift_list}), Path: {file_info['path']}")

result = {
    'max_copy_file': max_copy_file,
    'is_swift_repo': is_swift_repo,
    'total_files_analyzed': len(file_copy_counts)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
