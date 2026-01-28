code = """import json
import re
import sys

# Check what variables are available
available_vars = [name for name in dir() if name.startswith('var_')]
print('Available variables:', available_vars)
print('\n')

# We'll need to load the actual file data. Let me check what's available.
# Since previous attempts showed the data is stored in JSON files, let's load them properly.

# The paths should be in these variables
swift_repos_path = None
swift_files_path = None

for key in available_vars:
    if 'query_db:8' in key:
        swift_repos_path = globals()[key]
    elif 'query_db:10' in key:
        swift_files_path = globals()[key]

print('Paths found:')
print('  Swift repos:', swift_repos_path)
print('  Swift files:', swift_files_path)
print('\n')

# If paths exist, load them
swift_repos = []
swift_files = []

if swift_repos_path and isinstance(swift_repos_path, str):
    try:
        with open(swift_repos_path, 'r') as f:
            swift_repos = json.load(f)
        print(f'Loaded {len(swift_repos)} Swift repositories')
    except Exception as e:
        print(f'Error loading repos: {e}')

if swift_files_path and isinstance(swift_files_path, str):
    try:
        with open(swift_files_path, 'r') as f:
            swift_files = json.load(f)
        print(f'Loaded {len(swift_files)} Swift files')
    except Exception as e:
        print(f'Error loading files: {e}')

print('\n')

# If we have the data, process it
if swift_files:
    # Extract copy numbers from descriptions
    def extract_copies(desc):
        if not desc:
            return 0
        desc_lower = desc.lower()
        
        # Multiple patterns to match
        patterns = [
            r'duplicated (\d+) times',
            r'appearing (\d+) times', 
            r'copied (\d+) times',
            r'repeated (\d+) times',
            r'seen (\d+) times',
            r'appears (\d+) times'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, desc_lower)
            if match:
                return int(match.group(1))
        
        return 0
    
    # Process each file
    max_copies = 0
    max_file_info = None
    
    print('Analyzing files...')
    for idx, file_data in enumerate(swift_files):
        desc = file_data.get('repo_data_description', '')
        copies = extract_copies(desc)
        
        if copies > max_copies:
            max_copies = copies
            max_file_info = {
                'repository': file_data.get('sample_repo_name'),
                'file_id': file_data.get('id'),
                'copies': copies,
                'path': file_data.get('sample_path'),
                'description': desc
            }
        
        # Progress indicator
        if idx % 1000 == 0:
            print(f'  Processed {idx} files...')
    
    print('\n')
    print('='*60)
    print('MOST COPIED SWIFT FILE FOUND:')
    print('='*60)
    if max_file_info:
        print(f"Repository: {max_file_info['repository']}")
        print(f"File ID: {max_file_info['file_id']}")
        print(f"Copies: {max_file_info['copies']}")
        print(f"Path: {max_file_info['path']}")
        print(f"Description: {max_file_info['description']}")
        
        result = {
            'repository': max_file_info['repository'],
            'file_id': max_file_info['file_id'],
            'copies': max_file_info['copies'],
            'file_path': max_file_info['path']
        }
    else:
        print("No files with copy information found")
        result = {'error': 'No copied files found'}
else:
    print('No Swift files data available')
    result = {'error': 'No data loaded'}

print('\n')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}, {'repo_name': 'Apemb/Compass', 'language_description': 'The codebase includes: Swift (33,632 bytes), Shell (711 bytes), Ruby (434 bytes).'}, {'repo_name': 'toggl/superday', 'language_description': 'The majority of the code is in Swift (747,765 bytes), followed by Ruby (3,949 bytes), Shell (393 bytes).'}, {'repo_name': 'malcommac/SwiftDate', 'language_description': 'While most of the project is built in Swift (419,579 bytes), it also incorporates Ruby (767 bytes), Shell (169 bytes).'}, {'repo_name': 'chronotruck/CTKFlagPhoneNumber', 'language_description': 'While most of the project is built in Swift (87,439 bytes), it also incorporates Ruby (2,165 bytes), Shell (65 bytes).'}, {'repo_name': 'zendobk/SwiftUtils', 'language_description': 'While most of the project is built in Swift (71,711 bytes), it also incorporates Shell (3,156 bytes), Ruby (3,009 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'sample_repo_name': 'kostiakoval/WatchKit-Apps'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'sample_repo_name': 'slavapestov/swift'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'sample_repo_name': 'gmertk/BusyNavigationBar'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'sample_repo_name': 'firebase/quickstart-ios'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'sample_repo_name': 'MakeZL/MLSwiftBasic'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:28': [{'swift_repo_count': '42605'}]}

exec(code, env_args)
