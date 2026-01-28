code = """import json
import re

# Load the Swift files query result
swift_files_result = locals()['var_functions.query_db:10']

if isinstance(swift_files_result, str):
    with open(swift_files_result, 'r') as f:
        swift_files = json.load(f)
else:
    swift_files = swift_files_result

print(f"Processing {len(swift_files)} Swift files")

# Parse copy counts from descriptions
copy_pattern = re.compile(r'(seen|appearing|duplicated)\s+(\d+)\s+times?', re.IGNORECASE)

copy_counts = []
for file in swift_files:
    desc = file.get('repo_data_description', '')
    match = copy_pattern.search(desc)
    if match:
        count = int(match.group(2))
        copy_counts.append({
            'id': file['id'],
            'count': count,
            'repo': file['sample_repo_name'],
            'path': file['sample_path']
        })

print(f"Found copy counts for {len(copy_counts)} files")
if copy_counts:
    # Find file with max copies
    max_file = max(copy_counts, key=lambda x: x['count'])
    print(f"Max copies: {max_file['count']} for file {max_file['id']} in repo {max_file['repo']}")

print('__RESULT__:')
print(json.dumps({
    'total_files': len(swift_files),
    'files_with_counts': len(copy_counts),
    'max_copies': max_file if copy_counts else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'count': 42605, 'sample': [{'repo_name': 'e-Sixt/Swen'}, {'repo_name': 'ApplauseOSS/Swifjection'}, {'repo_name': 'vizifit/GenericPasswordRow'}, {'repo_name': 'cxy921126/SoftSwift'}, {'repo_name': 'cwwise/CWWeChat'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
