code = """import json
import re

# Load the Swift files data from the file path stored in the variable
with open('/var/lib/data/var_functions.query_db:20.json', 'r') as f:
    swift_files = json.load(f)

print('Total Swift files loaded:', len(swift_files))

# Find the file with maximum copy count by parsing repo_data_description
max_copies = 0
most_copied_repo = None
most_copied_file_id = None

for file_info in swift_files:
    desc = file_info.get('repo_data_description', '')
    # Look for patterns like "copied X times", "duplicated X times", "appearing X times", "repeated X times"
    match = re.search(r'(\d+)\s*times', desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            most_copied_repo = file_info.get('sample_repo_name')
            most_copied_file_id = file_info.get('id')

print('Most copied file details:')
print('Repository:', most_copied_repo)
print('File ID:', most_copied_file_id)
print('Copy count:', max_copies)

result = most_copied_repo

# Print in required format
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'total_rows': '24286'}], 'var_functions.query_db:7': [{'total_rows': '524077'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
