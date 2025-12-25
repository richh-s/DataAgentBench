code = """import json
import re

# Load the data from the previous step
file_path = locals()['var_function-call-17828382134315719986']
with open(file_path, 'r') as f:
    data = json.load(f)

# Regex to extract copies
# Patterns: "duplicated X times", "appearing X times", "copied X times", "repeated X times", "seen X times"
pattern = re.compile(r'(duplicated|appearing|copied|repeated|seen)\s+(\d+)\s+times')

max_copies = -1
best_repo = None
best_id = None
best_desc = None

for item in data:
    desc = item.get('repo_data_description', '')
    # check for non-binary
    if 'non-binary' not in desc:
        continue
    
    match = pattern.search(desc)
    if match:
        copies = int(match.group(2))
        if copies > max_copies:
            max_copies = copies
            best_repo = item.get('sample_repo_name')
            best_id = item.get('id')
            best_desc = desc

print("__RESULT__:")
print(json.dumps({
    "max_copies": max_copies,
    "repository": best_repo,
    "file_id": best_id,
    "description": best_desc
}))"""

env_args = {'var_function-call-1904592251343950054': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}], 'var_function-call-6938816719353708932': [{'count_star()': '105'}], 'var_function-call-17828382134315719986': 'file_storage/function-call-17828382134315719986.json'}

exec(code, env_args)
