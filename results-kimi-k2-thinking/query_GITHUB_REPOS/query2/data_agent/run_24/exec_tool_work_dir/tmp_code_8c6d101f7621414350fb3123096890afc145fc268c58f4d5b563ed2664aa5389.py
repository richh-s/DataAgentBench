code = """import json
import re

# Load the full result from the file
result_file = var_functions.query_db:8
with open(result_file, 'r') as f:
    swift_files = json.load(f)

print(f"Total Swift files retrieved: {len(swift_files)}")

# Parse each file entry to extract copy count and verify non-binary status
file_data = []
for file in swift_files:
    repo_data_desc = file.get('repo_data_description', '').lower()
    
    # Check if it's non-binary
    is_non_binary = 'non-binary' in repo_data_desc
    
    # Extract copy count
    copy_count = 0
    if is_non_binary:
        # Look for patterns like "duplicated X times", "appearing X times", "copied X times", etc.
        match = re.search(r'(\d+) times', repo_data_desc)
        if match:
            copy_count = int(match.group(1))
    
    file_data.append({
        'id': file['id'],
        'repo_name': file['sample_repo_name'],
        'path': file['sample_path'],
        'is_non_binary': is_non_binary,
        'copy_count': copy_count,
        'original_desc': file.get('repo_data_description', '')
    })

# Filter for non-binary files with copies > 0
non_binary_files = [f for f in file_data if f['is_non_binary'] and f['copy_count'] > 0]

print(f"Found {len(non_binary_files)} non-binary Swift files with copy information")

# Sort by copy count descending
non_binary_files.sort(key=lambda x: x['copy_count'], reverse=True)

# Show top 10 files
print("\nTop 10 most copied non-binary Swift files:")
for i, f in enumerate(non_binary_files[:10]):
    print(f"{i+1}. {f['copy_count']} copies - {f['path']} ({f['repo_name']})")
    print(f"   ID: {f['id']}")
    print(f"   Desc: {f['original_desc'][:100]}...")
    print()

# Find the file with maximum copy count
if non_binary_files:
    max_file = non_binary_files[0]
    print(f"Most copied file:")
    print(f"  Repository: {max_file['repo_name']}")
    print(f"  File ID: {max_file['id']}")
    print(f"  Path: {max_file['path']}")
    print(f"  Copy count: {max_file['copy_count']}")
    
    result = {
        'repository': max_file['repo_name'],
        'file_id': max_file['id'],
        'file_path': max_file['path'],
        'copy_count': max_file['copy_count']
    }
else:
    result = {'error': 'No non-binary Swift files found with copy information'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'repository': 'uacaps/PageMenu', 'max_copy_count': 38, 'file_id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'file_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift'}, 'var_functions.query_db:12': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}]}

exec(code, env_args)
