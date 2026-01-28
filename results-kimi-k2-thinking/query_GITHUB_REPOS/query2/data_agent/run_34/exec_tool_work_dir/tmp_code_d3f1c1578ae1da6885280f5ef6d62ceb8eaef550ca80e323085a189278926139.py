code = """import json

# Read the file containing Swift files data
with open('/tmp/tmpq3w7h4i8.json', 'r') as f:
    swift_files = json.load(f)

print(f'Total Swift files with metadata: {len(swift_files)}')

# Extract copy count from repo_data_description
import re

file_copy_data = []
for file in swift_files:
    desc = file.get('repo_data_description', '')
    
    # Check if it's non-binary
    if 'non-binary' in desc:
        # Extract copy count
        copy_match = re.search(r'(?:duplicated|appearing|copied|repeated) (\d+) times', desc)
        if copy_match:
            copy_count = int(copy_match.group(1))
            file_copy_data.append({
                'id': file['id'],
                'repo_name': file['sample_repo_name'],
                'path': file['sample_path'],
                'copy_count': copy_count,
                'description': desc
            })

print(f'Total non-binary Swift files: {len(file_copy_data)}')

# Find the file with maximum copy count
if file_copy_data:
    max_copies = max(file_copy_data, key=lambda x: x['copy_count'])
    print(f'Max copies: {max_copies["copy_count"]}')
    
    # Group by repo_name to find which repo has the most copied files
    from collections import defaultdict
    repo_copy_stats = defaultdict(list)
    
    for file in file_copy_data:
        repo_copy_stats[file['repo_name']].append(file)
    
    # Find repo with highest copy count file
    best_repo = None
    best_file = None
    max_copies = 0
    
    for repo_name, files in repo_copy_stats.items():
        repo_max_file = max(files, key=lambda x: x['copy_count'])
        if repo_max_file['copy_count'] > max_copies:
            max_copies = repo_max_file['copy_count']
            best_repo = repo_name
            best_file = repo_max_file
    
    print('__RESULT__:')
    print(json.dumps({
        'repository': best_repo,
        'file_id': best_file['id'],
        'file_path': best_file['path'],
        'copy_count': best_file['copy_count']
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No non-binary Swift files found'}))"""

env_args = {'var_functions.list_db:0': ['commits', 'contents', 'files'], 'var_functions.query_db:2': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'c86b30ad42a5299ccb8907a949ad9248eadc0204', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/01682-swift-parser-parsedecl.swift', 'repo_data_description': 'The dataset includes this non-binary file, 211 bytes in size and copied 15 times (mode: 33188).'}, {'id': '30b20e2d80706fd2381dc51eec2f1c22e71ecacf', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/15025-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'A 221-byte non-binary file appearing 15 times, with sample mode code 33188.'}, {'id': 'b350eee519227d356704648c868c896ff3a93048', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/18368-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'The dataset includes this non-binary file, 226 bytes in size and copied 15 times (mode: 33188).'}, {'id': '1ad86cf8e815fce652aa101d654485fea8033954', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/01847-std-function-func-swift-type-subst.swift', 'repo_data_description': 'Non-binary content file (215 bytes) seen 15 times, using sample mode 33188.'}, {'id': '3c92bfc55f392146da4902bc252fd216cd3f2efd', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/08505-swift-typechecker-conformstoprotocol.swift', 'repo_data_description': 'With a file size of 247 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': '3d42ac2c0fad831225f80a9355a196027e6ccc3e', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/00118-swift-dependentgenerictyperesolver-resolvegenerictypeparamtype.swift', 'repo_data_description': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'id': 'be6be234f9d404b0251c9a3626d644104cfe359b', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/15704-no-stacktrace.swift', 'repo_data_description': 'It is a non-binary file of 243 bytes, repeated 15 times in the dataset under mode 33188.'}, {'id': 'b8223ce270293582721ad59ebe08f0ca2c068ed8', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/04574-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'This file has a size of 241 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'id': 'cc4de346f66613edef22d12b73c44fc2c8834acd', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/02484-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 226 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
