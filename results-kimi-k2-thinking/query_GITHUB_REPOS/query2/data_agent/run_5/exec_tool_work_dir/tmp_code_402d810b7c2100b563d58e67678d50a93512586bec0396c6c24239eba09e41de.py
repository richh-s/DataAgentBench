code = """# Access the stored query result directly
swift_files = var_functions.query_db:20
print('Total Swift files loaded:', len(swift_files))

# Extract copy counts and find maximum
max_copies = 0
most_copied_repo = None

import re

for file_info in swift_files:
    desc = file_info.get('repo_data_description', '')
    match = re.search(r'(\d+)\s*times', desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            most_copied_repo = file_info.get('sample_repo_name')

if most_copied_repo:
    print('Most copied non-binary Swift file is in repository:', most_copied_repo)
    print('Copy count:', max_copies)
else:
    print('No files with copy information found')

print('---RESULT---')
print(most_copied_repo)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'total_rows': '24286'}], 'var_functions.query_db:7': [{'total_rows': '524077'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
