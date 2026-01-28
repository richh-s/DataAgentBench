code = """import json
import re

# Read data
swift_repos = var_functions.query_db:0
swift_files = var_functions.query_db:2

# Ensure we have lists
if isinstance(swift_repos, str) and '.json' in swift_repos:
    with open(swift_repos) as f:
        swift_repos = json.load(f)
if isinstance(swift_files, str) and '.json' in swift_files:
    with open(swift_files) as f:
        swift_files = json.load(f)

swift_repo_set = set([r['repo_name'] for r in swift_repos])

max_copies = 0
max_file = None

for f in swift_files:
    desc = f.get('repo_data_description', '')
    if 'binary' in desc.lower() and 'non-binary' not in desc.lower():
        continue
    
    m = re.search(r'\b(\d+)\s+times?\b', desc)
    if m:
        copies = int(m.group(1))
        if copies > max_copies:
            max_copies = copies
            max_file = f

result = None
if max_file:
    repo_name = max_file['sample_repo_name']
    is_swift = repo_name in swift_repo_set
    result = {
        'repo_name': repo_name,
        'file_id': max_file['id'],
        'file_path': max_file['sample_path'],
        'copy_count': max_copies,
        'is_swift_repo': is_swift
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
