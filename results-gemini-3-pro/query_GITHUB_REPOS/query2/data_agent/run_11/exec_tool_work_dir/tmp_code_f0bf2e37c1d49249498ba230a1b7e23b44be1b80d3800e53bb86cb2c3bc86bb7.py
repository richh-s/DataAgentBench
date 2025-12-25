code = """import json
import re

with open(locals()['var_function-call-17980906881355930812'], 'r') as f:
    data = json.load(f)

patterns = [
    r'duplicated (\d+) times',
    r'appearing (\d+) times',
    r'appears (\d+) times',
    r'copied (\d+) times',
    r'repeated (\d+) times',
    r'seen (\d+) times'
]

unmatched = []
max_copies = 0

for entry in data:
    desc = entry.get('repo_data_description', '')
    if 'non-binary' not in desc:
        continue
        
    copies = 0
    matched = False
    for pat in patterns:
        match = re.search(pat, desc)
        if match:
            copies = int(match.group(1))
            matched = True
            break
    
    if copies > max_copies:
        max_copies = copies
        
    if not matched and ('times' in desc or 'copies' in desc or 'duplicated' in desc):
        unmatched.append(desc)

print("__RESULT__:")
print(json.dumps({
    "max_copies": max_copies,
    "unmatched_count": len(unmatched),
    "unmatched_samples": unmatched[:5]
}))"""

env_args = {'var_function-call-5692874898437470406': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}], 'var_function-call-8543626187986734798': [{'count_star()': '105'}], 'var_function-call-17980906881355930812': 'file_storage/function-call-17980906881355930812.json', 'var_function-call-526667583648693898': [{'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'copies': 38, 'repo': 'uacaps/PageMenu', 'path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'desc': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}, {'id': 'a34c3d906831a12ffffa1b5d0fc30505126e9b69', 'copies': 35, 'repo': 'kostiakoval/Mirror', 'path': 'Pods/Nimble/Nimble/Expectation.swift', 'desc': 'The dataset includes this non-binary file, 1848 bytes in size and copied 35 times (mode: 33188).'}, {'id': 'c4d6ced29fbff41f82c1e9ebd9d4e5fe0c4fd795', 'copies': 31, 'repo': 'apple/swift', 'path': 'test/Driver/Dependencies/bindings-build-record.swift', 'desc': 'It is a non-binary file of 3880 bytes, repeated 31 times in the dataset under mode 33188.'}, {'id': '1ff86af65537e2973b533c27044763ffefd0347d', 'copies': 25, 'repo': 'slavapestov/swift', 'path': 'stdlib/public/SDK/Darwin/MachError.swift', 'desc': 'It is a non-binary file of 6960 bytes, repeated 25 times in the dataset under mode 33188.'}, {'id': 'd20a36a3d7064de9fc8f2438b5ed6d6c4df8cf56', 'copies': 25, 'repo': 'slavapestov/swift', 'path': 'test/Constraints/unchecked_optional.swift', 'desc': 'It is a non-binary file of 1789 bytes, repeated 25 times in the dataset under mode 33188.'}], 'var_function-call-1543198338971498008': [], 'var_function-call-16570986560373444208': [{'id': '316ad972693d0355c3504729fff14287419e004d', 'repo_name': 'np/ling'}, {'id': 'daa40d563068ee94f01b1e87952d607a6588a589', 'repo_name': 'np/ling'}, {'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a', 'repo_name': 'np/ling'}, {'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969', 'repo_name': 'np/ling'}, {'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6', 'repo_name': 'np/ling'}], 'var_function-call-1334904029853597433': [], 'var_function-call-13995254349312541100': [{'repo_name': 'uacaps/PageMenu', 'watch_count': '487'}], 'var_function-call-3498404794503639184': [{'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}]}

exec(code, env_args)
