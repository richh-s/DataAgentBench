code = """import json
import re

# Read data from file
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    swift_files = json.load(f)

print('Total non-binary Swift files:', len(swift_files))

# Extract copy count from repo_data_description
def extract_copies(description):
    pattern = r'(\d+)\s+times'
    match = re.search(pattern, description)
    if match:
        return int(match.group(1))
    return 0

# Create list with copy counts enhanced
files_with_copies = []
for file in swift_files:
    copies = extract_copies(file['repo_data_description'])
    files_with_copies.append({
        'id': file['id'],
        'repo': file['sample_repo_name'],
        'copies': copies,
        'description': file['repo_data_description']
    })

# Sort by copy count descending
sorted_files = sorted(files_with_copies, key=lambda x: x['copies'], reverse=True)

print('Top 5 most copied Swift files:')
for i, file in enumerate(sorted_files[:5]):
    print(str(i+1) + '. ID: ' + file['id'][:20] + ', Repo: ' + file['repo'] + ', Copies: ' + str(file['copies']))

# Find the repository of the most copied file
most_copied_file = sorted_files[0]
print('\nMost copied file:')
print('Copy count:', most_copied_file['copies'])
print('Repository:', most_copied_file['repo'])
print('File ID:', most_copied_file['id'])
print('Description:', most_copied_file['description'])

result = {
    'repository': most_copied_file['repo'],
    'copy_count': most_copied_file['copies'],
    'file_id': most_copied_file['id']
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}, {'repo_data_description': 'With a file size of 865 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'repo_data_description': 'It is a non-binary file of 4802 bytes, repeated 8 times in the dataset under mode 33188.'}, {'repo_data_description': 'This file has a size of 588 bytes, is non-binary, and appears 8 times with sample mode 33188.'}, {'repo_data_description': 'Non-binary content file (3675 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'This file has a size of 26140 bytes, is binary, and appears 8 times with sample mode 33188.'}], 'var_functions.query_db:2': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'sample_repo_name': 'slavapestov/swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'sample_repo_name': 'firebase/quickstart-ios', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
