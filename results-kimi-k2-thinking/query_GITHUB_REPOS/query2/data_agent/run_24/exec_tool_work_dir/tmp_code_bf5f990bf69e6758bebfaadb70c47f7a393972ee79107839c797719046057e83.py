code = """import json
import re

# Get the result file path from storage
result_file_key = 'var_functions.query_db:8'
result_file = locals()[result_file_key]

print(f"Loading data from file: {result_file}")

# Load the full result from the file
with open(result_file, 'r') as f:
    swift_files = json.load(f)

print(f"Total Swift files retrieved: {len(swift_files)}")

# Analyze the data to find the most frequently copied non-binary Swift file
file_copy_counts = []

for file in swift_files:
    repo_data_desc = file.get('repo_data_description', '')
    
    # Check if it's non-binary and extract copy count
    if 'non-binary' in repo_data_desc.lower():
        # Extract copy count using regex
        copy_match = re.search(r'(duplicated|appearing|copied|repeated|appears) (\d+) times', repo_data_desc.lower())
        if copy_match:
            copy_count = int(copy_match.group(2))
            file_copy_counts.append({
                'id': file['id'],
                'repo_name': file['sample_repo_name'],
                'path': file['sample_path'],
                'copy_count': copy_count,
                'description': repo_data_desc
            })

# Sort by copy count in descending order
file_copy_counts.sort(key=lambda x: x['copy_count'], reverse=True)

print(f"Found {len(file_copy_counts)} non-binary Swift files with copy information")

if file_copy_counts:
    top_file = file_copy_counts[0]
    print(f"Top file: {top_file['path']} from {top_file['repo_name']}")
    print(f"Copy count: {top_file['copy_count']}")
    print(f"File ID: {top_file['id']}")

# Group by repository to find which repo has the most frequently copied file
repo_stats = {}
for file in file_copy_counts:
    repo = file['repo_name']
    if repo not in repo_stats:
        repo_stats[repo] = {
            'max_copies': 0,
            'file_with_max_copies': None
        }
    
    if file['copy_count'] > repo_stats[repo]['max_copies']:
        repo_stats[repo]['max_copies'] = file['copy_count']
        repo_stats[repo]['file_with_max_copies'] = file

# Find the repository with the highest copy count
max_copies = 0
best_repo = None
best_file = None

for repo, stats in repo_stats.items():
    if stats['max_copies'] > max_copies:
        max_copies = stats['max_copies']
        best_repo = repo
        best_file = stats['file_with_max_copies']

result = {
    'repository': best_repo,
    'max_copy_count': max_copies,
    'file_id': best_file['id'] if best_file else None,
    'file_path': best_file['path'] if best_file else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:1': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
