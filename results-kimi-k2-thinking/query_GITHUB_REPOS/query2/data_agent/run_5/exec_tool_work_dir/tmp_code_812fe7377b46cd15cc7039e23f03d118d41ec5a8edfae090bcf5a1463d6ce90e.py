code = """import json
import re

# Load the Swift files data
swift_files_path = var_functions.query_db:20

with open(swift_files_path, 'r') as f:
    swift_files = json.load(f)

print('Total Swift files loaded:', len(swift_files))

# Find the file with maximum copy count
max_copies = 0
most_copied_file = None

copy_pattern = re.compile(r'(\d+)\s*times')

for file_info in swift_files:
    desc = file_info.get('repo_data_description', '')
    match = copy_pattern.search(desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            most_copied_file = file_info

if most_copied_file:
    print('Most copied file:')
    print('ID:', most_copied_file['id'])
    print('Repository:', most_copied_file['sample_repo_name'])
    print('Copy count:', max_copies)
    print('Description:', most_copied_file['repo_data_description'])
    
    result = most_copied_file['sample_repo_name']
else:
    print('No files with copy information found')
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'total_rows': '24286'}], 'var_functions.query_db:7': [{'total_rows': '524077'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
