code = """import json
import re
from collections import defaultdict

# Load the complete Swift files query result
swift_files_file = locals()['var_functions.query_db:12']

# Read the full results from the file
with open(swift_files_file, 'r') as f:
    all_swift_files = json.load(f)

print(f"Total Swift files found: {len(all_swift_files)}")

# Pattern to extract copy count from repo_data_description
copy_pattern = re.compile(r'(copied|appearing|duplicated|appears|repeated|seen)\s+(\d+)\s+times')

# Process each file
max_copy_count = 0
max_copy_files = []

# Track copy counts by file ID to ensure uniqueness
file_copy_counts = {}

for file_data in all_swift_files:
    desc = file_data.get('repo_data_description', '')
    
    # Check if it's non-binary
    is_non_binary = 'non-binary' in desc
    
    if not is_non_binary:
        continue
    
    # Extract copy count
    copy_count = 1
    match = copy_pattern.search(desc)
    if match:
        copy_count = int(match.group(2))
    
    file_id = file_data['id']
    repo = file_data['sample_repo_name']
    
    # Store by file ID to ensure uniqueness
    if file_id not in file_copy_counts or copy_count > file_copy_counts[file_id]['copy_count']:
        file_copy_counts[file_id] = {
            'id': file_id,
            'repo': repo,
            'path': file_data['sample_path'],
            'copy_count': copy_count,
            'description': desc
        }
    
    # Update max
    if copy_count > max_copy_count:
        max_copy_count = copy_count
        max_copy_files = [file_copy_counts[file_id]]
    elif copy_count == max_copy_count:
        max_copy_files.append(file_copy_counts[file_id])

print(f"\nNon-binary Swift files: {len(file_copy_counts)}")
print(f"Max copy count: {max_copy_count}")
print(f"Number of files with max copies: {len(max_copy_files)}")

if max_copy_files:
    print(f"\nFiles with maximum copy count:")
    repos_with_max_files = defaultdict(list)
    for f in max_copy_files:
        repos_with_max_files[f['repo']].append(f)
        print(f"  ID: {f['id']}")
        print(f"  Repo: {f['repo']}")
        print(f"  Path: {f['path']}")
        print(f"  Copies: {f['copy_count']}")
        print()
    
    # Identify unique repositories
    unique_repos = list(repos_with_max_files.keys())
    print(f"Repositories containing files with {max_copy_count} copies:")
    for repo in unique_repos:
        print(f"  - {repo} ({len(repos_with_max_files[repo])} file(s))")
    
    # Prepare result
    result = {
        'max_copy_count': max_copy_count,
        'repositories': unique_repos,
        'file_count': len(max_copy_files),
        'sample_files': max_copy_files[:3]
    }
    
    print('\n__RESULT__:')
    print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_functions.execute_python:10': {'max_copy_count': 15, 'top_files': [{'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'repo': 'practicalswift/swift-compiler-crashes', 'path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'copy_count': 15, 'is_non_binary': True}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'repo': 'practicalswift/swift-compiler-crashes', 'path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'copy_count': 15, 'is_non_binary': True}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
