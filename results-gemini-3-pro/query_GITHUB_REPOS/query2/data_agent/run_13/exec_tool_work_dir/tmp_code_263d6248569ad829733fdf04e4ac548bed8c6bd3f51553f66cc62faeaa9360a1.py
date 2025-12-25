code = """import json
import re

data = json.load(open('var_function-call-9948888079856787499.json'))

# Pattern to find copy count
# Patterns:
# "is duplicated 8 times"
# "appearing 8 times"
# "appears 9 times"
# "repeated 15 times"
# "copied 12 times"

regex = re.compile(r'(?:duplicated|appearing|appears|repeated|copied)\s+(\d+)\s+times')

results = []
for item in data:
    desc = item.get('repo_data_description', '')
    match = regex.search(desc)
    if match:
        count = int(match.group(1))
        results.append({
            'id': item['id'],
            'count': count,
            'sample_repo_name': item['sample_repo_name'],
            'sample_path': item['sample_path']
        })

# Sort by count descending
results.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-421206254122114556': ['commits', 'contents', 'files'], 'var_function-call-14995997162551538264': [{'id': 'a6fb31fa1e4b1647e8862580703add8c6205c6d1', 'copy_count': '4'}, {'id': '6066caa5e76b60fbd0f7bc2a096c6fd7c023609f', 'copy_count': '2'}, {'id': '49f5eda9ac693bf61324ee7f65a15d704f7f3411', 'copy_count': '2'}, {'id': 'a1615a71d1bdbb036d1dde0a94b8285fa8fca084', 'copy_count': '2'}, {'id': 'd1b6baa8d0bd3ac28e0765482e204e33340ccf8c', 'copy_count': '2'}, {'id': 'f64ee245678dcb26d658600708e2996a7608fc6e', 'copy_count': '2'}, {'id': 'e94c45ffe619fbd39e7f5df78a590bd33893d64a', 'copy_count': '2'}, {'id': '8af9111216436874eecfaa475d5c2f3ac650e3bc', 'copy_count': '2'}, {'id': '75c9123b0b91ca99402ed40efe80d21cb6bc3f90', 'copy_count': '2'}, {'id': '53496cde05c660feb3ab3335e825b363aa68a51a', 'copy_count': '2'}], 'var_function-call-16670457114105317735': [], 'var_function-call-15451713365687959615': [], 'var_function-call-9239782805473222517': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}], 'var_function-call-3622584659338368363': [{'count_star()': '89'}], 'var_function-call-9948888079856787499': 'file_storage/function-call-9948888079856787499.json'}

exec(code, env_args)
