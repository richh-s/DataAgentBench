code = """import json
import re

# Access the storage variables correctly
def get_storage_var(var_name):
    """Safely get a variable from storage"""
    if var_name in globals():
        return globals()[var_name]
    elif var_name in locals():
        return locals()[var_name]
    else:
        return None

# Get the data
swift_repos_data = get_storage_var('var_functions.query_db:8')
swift_files_data = get_storage_var('var_functions.query_db:10')

print('Data types:')
print(f'  swift_repos_data: {type(swift_repos_data)}')
print(f'  swift_files_data: {type(swift_files_data)}')

# Load JSON data if paths are provided
swift_repos = []
swift_files = []

if isinstance(swift_repos_data, str) and '.json' in swift_repos_data:
    with open(swift_repos_data, 'r') as f:
        swift_repos = json.load(f)
elif isinstance(swift_repos_data, list):
    swift_repos = swift_repos_data

if isinstance(swift_files_data, str) and '.json' in swift_files_data:
    with open(swift_files_data, 'r') as f:
        swift_files = json.load(f)
elif isinstance(swift_files_data, list):
    swift_files = swift_files_data

print(f'\nLoaded: {len(swift_repos)} repositories, {len(swift_files)} files')

if swift_files:
    print('\nSample file entries:')
    for i, f in enumerate(swift_files[:3]):
        print(f"  {i+1}. {f.get('id', 'N/A')}: {f.get('repo_data_description', 'N/A')[:80]}...")

# Function to extract copy count from description
def extract_copies(description):
    if not description:
        return 0
    desc_lower = description.lower()
    
    import re
    patterns = [
        r'duplicated (\d+) times',
        r'appearing (\d+) times',
        r'copied (\d+) times',
        r'repeated (\d+) times',
        r'seen (\d+) times',
        r'appears (\d+) times',
        r'appears (\d+) times'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, desc_lower)
        if match:
            return int(match.group(1))
    
    # Also check for patterns like "is duplicated <n> times"
    match = re.search(r'is duplicated (\d+) times', desc_lower)
    if match:
        return int(match.group(1))
    
    return 0

# Analyze files
max_copies = 0
max_file = None
files_with_copies = []

for file_info in swift_files:
    copies = extract_copies(file_info.get('repo_data_description', ''))
    if copies > 0:
        files_with_copies.append({
            'id': file_info.get('id'),
            'repo_name': file_info.get('sample_repo_name'),
            'path': file_info.get('sample_path'),
            'copies': copies,
            'description': file_info.get('repo_data_description', '')
        })
        
        if copies > max_copies:
            max_copies = copies
            max_file = files_with_copies[-1]

print(f'\nFiles with copy information: {len(files_with_copies)}')

if max_file:
    print(f'\nMost copied Swift file:')
    print(f"  ID: {max_file['id']}")
    print(f"  Repository: {max_file['repo_name']}")
    print(f"  Copies: {max_file['copies']}")
    print(f"  Path: {max_file['path']}")
    
    # Prepare result for JSON output
    result = {
        'repository': max_file['repo_name'],
        'file_id': max_file['id'],
        'copies': max_file['copies'],
        'file_path': max_file['path'],
        'description': max_file['description']
    }
else:
    result = {'error': 'No copied files found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}, {'repo_name': 'Apemb/Compass', 'language_description': 'The codebase includes: Swift (33,632 bytes), Shell (711 bytes), Ruby (434 bytes).'}, {'repo_name': 'toggl/superday', 'language_description': 'The majority of the code is in Swift (747,765 bytes), followed by Ruby (3,949 bytes), Shell (393 bytes).'}, {'repo_name': 'malcommac/SwiftDate', 'language_description': 'While most of the project is built in Swift (419,579 bytes), it also incorporates Ruby (767 bytes), Shell (169 bytes).'}, {'repo_name': 'chronotruck/CTKFlagPhoneNumber', 'language_description': 'While most of the project is built in Swift (87,439 bytes), it also incorporates Ruby (2,165 bytes), Shell (65 bytes).'}, {'repo_name': 'zendobk/SwiftUtils', 'language_description': 'While most of the project is built in Swift (71,711 bytes), it also incorporates Shell (3,156 bytes), Ruby (3,009 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'sample_repo_name': 'kostiakoval/WatchKit-Apps'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'sample_repo_name': 'slavapestov/swift'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'sample_repo_name': 'gmertk/BusyNavigationBar'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'sample_repo_name': 'firebase/quickstart-ios'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'sample_repo_name': 'MakeZL/MLSwiftBasic'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
