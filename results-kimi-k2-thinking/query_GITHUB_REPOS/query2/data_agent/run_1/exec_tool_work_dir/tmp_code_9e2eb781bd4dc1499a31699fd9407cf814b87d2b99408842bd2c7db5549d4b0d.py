code = """import json
import re

# Load all Swift files
swift_files_path = locals()['var_functions.query_db:16']

if isinstance(swift_files_path, str):
    with open(swift_files_path, 'r') as f:
        swift_files = json.load(f)
else:
    swift_files = swift_files_path

print('Total Swift files to process: %d' % len(swift_files))

# Regular expression to extract copy count from repo_data_description
copy_pattern = re.compile(r'(seen|appearing|duplicated|appears)\s+(\d+)\s+times?', re.IGNORECASE)

# Process files and extract copy counts
file_copy_counts = []
for file in swift_files:
    desc = file.get('repo_data_description', '')
    match = copy_pattern.search(desc)
    if match:
        count = int(match.group(2))
        file_copy_counts.append({
            'id': file['id'],
            'count': count,
            'repo': file['sample_repo_name'],
            'path': file['sample_path'],
            'description': desc
        })

print('Files with copy count information: %d' % len(file_copy_counts))

max_file = None
if file_copy_counts:
    # Find file with maximum copies
    max_file = max(file_copy_counts, key=lambda x: x['count'])
    print('File with most copies:')
    print('  File ID: %s' % max_file['id'])
    print('  Copies: %d' % max_file['count'])
    print('  Repository: %s' % max_file['repo'])
    print('  Path: %s' % max_file['path'])
else:
    print('No copy count information found in Swift files')

# Also check if any file has binary in description to filter out
binary_files = [f for f in swift_files if 'binary' in f.get('repo_data_description', '').lower()]
print('Binary Swift files: %d' % len(binary_files))

print('__RESULT__:')
result = {
    'total_swift_files': len(swift_files),
    'files_with_copy_counts': len(file_copy_counts),
    'max_copies': max_file,
    'binary_files_count': len(binary_files)
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'count': 42605, 'sample': [{'repo_name': 'e-Sixt/Swen'}, {'repo_name': 'ApplauseOSS/Swifjection'}, {'repo_name': 'vizifit/GenericPasswordRow'}, {'repo_name': 'cxy921126/SoftSwift'}, {'repo_name': 'cwwise/CWWeChat'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'total_files': 20, 'files_with_counts': 11, 'max_copies': {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'count': 15, 'repo': 'practicalswift/swift-compiler-crashes', 'path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift'}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
