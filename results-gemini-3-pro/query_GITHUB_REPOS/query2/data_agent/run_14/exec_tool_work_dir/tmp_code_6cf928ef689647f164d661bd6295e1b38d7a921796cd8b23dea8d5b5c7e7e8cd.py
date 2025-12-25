code = """import json
import re

file_path = locals()['var_function-call-17828382134315719986']
with open(file_path, 'r') as f:
    data = json.load(f)

pattern = re.compile(r'(duplicated|appearing|copied|repeated|seen)\s+(\d+)\s+times')

max_copies = -1
candidates = []

for item in data:
    desc = item.get('repo_data_description', '')
    if 'non-binary' not in desc:
        continue
    
    match = pattern.search(desc)
    if match:
        copies = int(match.group(2))
        if copies > max_copies:
            max_copies = copies
            candidates = [item]
        elif copies == max_copies:
            candidates.append(item)

print("__RESULT__:")
print(json.dumps({
    "max_copies": max_copies,
    "candidates": candidates
}))"""

env_args = {'var_function-call-1904592251343950054': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}], 'var_function-call-6938816719353708932': [{'count_star()': '105'}], 'var_function-call-17828382134315719986': 'file_storage/function-call-17828382134315719986.json', 'var_function-call-12595007085451203699': {'max_copies': 38, 'repository': 'uacaps/PageMenu', 'file_id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}, 'var_function-call-15283188719297696231': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_function-call-1827899923006742523': [], 'var_function-call-3303885191878298259': [{'id': '316ad972693d0355c3504729fff14287419e004d'}, {'id': 'daa40d563068ee94f01b1e87952d607a6588a589'}, {'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a'}, {'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969'}, {'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6'}], 'var_function-call-11848719904844716189': [], 'var_function-call-11568463175763808063': [{'count_star()': '524077'}], 'var_function-call-15027238197139595416': []}

exec(code, env_args)
