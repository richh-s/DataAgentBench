code = """import json
import re

with open(locals()['var_function-call-2857671841387729764'], 'r') as f:
    swift_repos = json.load(f)

with open(locals()['var_function-call-5872438344491573241'], 'r') as f:
    non_binary_files = json.load(f)

swift_non_binary_files = []
for file_info in non_binary_files:
    if file_info['sample_repo_name'] in swift_repos:
        swift_non_binary_files.append(file_info)

max_copies = -1
most_copied_file_repo = None

for file_info in swift_non_binary_files:
    description = file_info['repo_data_description']
    match = re.search(r'(?:seen|appearing|duplicated|copied) (\d+) times', description)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            most_copied_file_repo = file_info['sample_repo_name']

print('__RESULT__:')
print(json.dumps(most_copied_file_repo))"""

env_args = {'var_function-call-10437230453846877627': 'file_storage/function-call-10437230453846877627.json', 'var_function-call-2857671841387729764': 'file_storage/function-call-2857671841387729764.json', 'var_function-call-7960988833129329187': 'file_storage/function-call-7960988833129329187.json', 'var_function-call-5872438344491573241': 'file_storage/function-call-5872438344491573241.json'}

exec(code, env_args)
