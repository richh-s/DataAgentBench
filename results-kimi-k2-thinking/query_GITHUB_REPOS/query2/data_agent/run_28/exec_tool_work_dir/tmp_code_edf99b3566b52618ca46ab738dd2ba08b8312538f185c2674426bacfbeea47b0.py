code = """import json
import re

# Load the Swift files data from the previous query
storage_key = 'var_functions.query_db:22'
result_data = locals()[storage_key]

# Load the data
if isinstance(result_data, str):
    with open(result_data, 'r') as f:
        swift_files = json.load(f)
else:
    swift_files = result_data

print('Total Swift files found:', len(swift_files))
print('Sample file:', swift_files[0])

# Function to extract copy count from repo_data_description
def extract_copy_count(description):
    # Look for patterns like "duplicated X times", "copied X times", "appearing X times"
    patterns = [
        r'duplicated\s+(\d+)\s+times',
        r'copied\s+(\d+)\s+times',
        r'appearing\s+(\d+)\s+times',
        r'appears\s+(\d+)\s+times'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            return int(match.group(1))
    
    # If no pattern matches, return 1 (file appears at least once)
    return 1

# Test the function
test_desc = swift_files[0]['repo_data_description']
print('Test description:', test_desc)
print('Extracted count:', extract_copy_count(test_desc))

# Find file with maximum copy count
max_copies = 0
max_file = None

for file in swift_files:
    copies = extract_copy_count(file['repo_data_description'])
    if copies > max_copies:
        max_copies = copies
        max_file = file

print('\nMost copied file:', max_file)
print('Copy count:', max_copies)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.execute_python:18': {'total_swift_repos': 42605, 'first_repo_sample': {'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, 'unique_repo_names': 42605}, 'var_functions.query_db:20': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
