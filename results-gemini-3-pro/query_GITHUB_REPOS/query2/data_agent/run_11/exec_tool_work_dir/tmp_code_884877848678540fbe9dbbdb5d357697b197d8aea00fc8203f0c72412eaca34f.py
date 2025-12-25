code = """import json
import re

# Load data
with open(locals()['var_function-call-17980906881355930812'], 'r') as f:
    data = json.load(f)

# Regex for copy count
# Patterns seen: 
# "duplicated 8 times"
# "appearing 8 times"
# "appears 9 times"
# "copied 12 times"
# "repeated 15 times"
# "seen 15 times"

patterns = [
    r'duplicated (\d+) times',
    r'appearing (\d+) times',
    r'appears (\d+) times',
    r'copied (\d+) times',
    r'repeated (\d+) times',
    r'seen (\d+) times'
]

results = []

for entry in data:
    desc = entry.get('repo_data_description', '')
    
    # Check non-binary
    if 'non-binary' not in desc:
        continue
        
    # Extract copies
    copies = 0
    for pat in patterns:
        match = re.search(pat, desc)
        if match:
            copies = int(match.group(1))
            break
            
    if copies > 0:
        results.append({
            'id': entry['id'],
            'copies': copies,
            'repo': entry['sample_repo_name'],
            'path': entry['sample_path'],
            'desc': desc
        })

# Sort by copies desc
results.sort(key=lambda x: x['copies'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-5692874898437470406': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}], 'var_function-call-8543626187986734798': [{'count_star()': '105'}], 'var_function-call-17980906881355930812': 'file_storage/function-call-17980906881355930812.json'}

exec(code, env_args)
