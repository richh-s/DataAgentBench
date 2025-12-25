code = """import json
import re

with open(locals()['var_function-call-2899128053290960101'], 'r') as f:
    records = json.load(f)

def extract_copies(desc):
    match = re.search(r'(?:duplicated|appearing|appears|repeated|copied)\s+(\d+)\s+times', desc)
    if match:
        return int(match.group(1))
    return 0

processed = []
for r in records:
    copies = extract_copies(r['repo_data_description'])
    processed.append({
        'id': r['id'],
        'sample_repo_name': r['sample_repo_name'],
        'copies': copies
    })

processed.sort(key=lambda x: x['copies'], reverse=True)

# Print top 3 to check for ties
print("__RESULT__:")
print(json.dumps(processed[:3]))"""

env_args = {'var_function-call-1864135806914008847': ['languages', 'repos', 'licenses'], 'var_function-call-1864135806914008968': ['commits', 'contents', 'files'], 'var_function-call-8819191931707815277': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}], 'var_function-call-8819191931707815650': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}], 'var_function-call-530612945601902535': [{'count_star()': '89'}], 'var_function-call-2899128053290960101': 'file_storage/function-call-2899128053290960101.json', 'var_function-call-4759068712813435656': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.', 'sample_repo_name': 'uacaps/PageMenu', 'copies': 38}, 'var_function-call-3566647091671526141': [], 'var_function-call-16557175443876985544': [], 'var_function-call-15989981146579886149': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_function-call-3939093896435150584': [{'count_star()': '524077'}], 'var_function-call-4584724603781345818': [], 'var_function-call-9916202495416399067': [{'id': '316ad972693d0355c3504729fff14287419e004d', 'repo_name': 'np/ling'}, {'id': 'daa40d563068ee94f01b1e87952d607a6588a589', 'repo_name': 'np/ling'}, {'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a', 'repo_name': 'np/ling'}, {'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969', 'repo_name': 'np/ling'}, {'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6', 'repo_name': 'np/ling'}], 'var_function-call-12593007993013017062': []}

exec(code, env_args)
