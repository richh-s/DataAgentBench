code = """import json
import re

# Read the results from the file
swift_files = []
with open('/tmp/tmp7b1o8oqc.json', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                row = json.loads(line)
                swift_files.append(row)
            except:
                pass

print('Total Swift files found: ' + str(len(swift_files)))

# Extract copy counts from repo_data_description
def extract_copy_count(description):
    patterns = [
        r'duplicated\s+(\d+)\s+times?',
        r'appearing\s+(\d+)\s+times?',
        r'copied\s+(\d+)\s+times?',
        r'repeated\s+(\d+)\s+times?',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return 1

# Process each file
file_stats = []
for file_info in swift_files:
    copy_count = extract_copy_count(file_info['repo_data_description'])
    file_stats.append({
        'id': file_info['id'],
        'path': file_info['sample_path'],
        'repo': file_info['sample_repo_name'],
        'count': copy_count,
        'desc': file_info['repo_data_description']
    })

# Sort by copy count
def sort_key(x):
    return x['count']

sorted_files = sorted(file_stats, key=sort_key, reverse=True)

# Find max
top_file = sorted_files[0]
max_count = top_file['count']
top_files = [f for f in sorted_files if f['count'] == max_count]

print('Max copies: ' + str(max_count))
print('Files with max copies:')
for f in top_files:
    print('ID: ' + f['id'])
    print('Path: ' + f['path'])
    print('Repo: ' + f['repo'])
    print()

# Get unique repos
repos = list(set(f['repo'] for f in top_files))
print('Repos to check: ' + str(repos))

result = {
    'max_count': max_count,
    'top_files': top_files,
    'repos': repos
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}, {'repo_name': 'Apemb/Compass', 'language_description': 'The codebase includes: Swift (33,632 bytes), Shell (711 bytes), Ruby (434 bytes).'}, {'repo_name': 'toggl/superday', 'language_description': 'The majority of the code is in Swift (747,765 bytes), followed by Ruby (3,949 bytes), Shell (393 bytes).'}, {'repo_name': 'malcommac/SwiftDate', 'language_description': 'While most of the project is built in Swift (419,579 bytes), it also incorporates Ruby (767 bytes), Shell (169 bytes).'}, {'repo_name': 'chronotruck/CTKFlagPhoneNumber', 'language_description': 'While most of the project is built in Swift (87,439 bytes), it also incorporates Ruby (2,165 bytes), Shell (65 bytes).'}, {'repo_name': 'zendobk/SwiftUtils', 'language_description': 'While most of the project is built in Swift (71,711 bytes), it also incorporates Shell (3,156 bytes), Ruby (3,009 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'repo_name': 'practicalswift/swift-compiler-crashes'}, {'repo_name': 'artsy/eidolon'}, {'repo_name': 'wxxsw/GSPhotos'}, {'repo_name': 'goktugyil/EZSwiftExtensions'}, {'repo_name': 'macoscope/GrandCentralBoard'}, {'repo_name': 'nodes-ios/user-manager-type'}, {'repo_name': 'rlopezdiez/RLDNavigationSwift'}, {'repo_name': 'stormpath/stormpath-sdk-swift'}, {'repo_name': 'domenicosolazzo/practice-swift'}, {'repo_name': 'wordpress-mobile/WordPress-iOS'}], 'var_functions.query_db:10': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.', 'sample_repo_name': 'kostiakoval/WatchKit-Apps'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.', 'sample_repo_name': 'slavapestov/swift'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.', 'sample_repo_name': 'gmertk/BusyNavigationBar'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.', 'sample_repo_name': 'firebase/quickstart-ios'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).', 'sample_repo_name': 'MakeZL/MLSwiftBasic'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'c86b30ad42a5299ccb8907a949ad9248eadc0204', 'sample_path': 'fixed/01682-swift-parser-parsedecl.swift', 'repo_data_description': 'The dataset includes this non-binary file, 211 bytes in size and copied 15 times (mode: 33188).', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '30b20e2d80706fd2381dc51eec2f1c22e71ecacf', 'sample_path': 'crashes-duplicates/15025-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'A 221-byte non-binary file appearing 15 times, with sample mode code 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'b350eee519227d356704648c868c896ff3a93048', 'sample_path': 'crashes-duplicates/18368-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'The dataset includes this non-binary file, 226 bytes in size and copied 15 times (mode: 33188).', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '1ad86cf8e815fce652aa101d654485fea8033954', 'sample_path': 'fixed/01847-std-function-func-swift-type-subst.swift', 'repo_data_description': 'Non-binary content file (215 bytes) seen 15 times, using sample mode 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '3c92bfc55f392146da4902bc252fd216cd3f2efd', 'sample_path': 'crashes-duplicates/08505-swift-typechecker-conformstoprotocol.swift', 'repo_data_description': 'With a file size of 247 bytes and sample mode 33188, this non-binary file is duplicated 15 times.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': '3d42ac2c0fad831225f80a9355a196027e6ccc3e', 'sample_path': 'fixed/00118-swift-dependentgenerictyperesolver-resolvegenerictypeparamtype.swift', 'repo_data_description': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'be6be234f9d404b0251c9a3626d644104cfe359b', 'sample_path': 'crashes-duplicates/15704-no-stacktrace.swift', 'repo_data_description': 'It is a non-binary file of 243 bytes, repeated 15 times in the dataset under mode 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'b8223ce270293582721ad59ebe08f0ca2c068ed8', 'sample_path': 'crashes-duplicates/04574-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'This file has a size of 241 bytes, is non-binary, and appears 15 times with sample mode 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'id': 'cc4de346f66613edef22d12b73c44fc2c8834acd', 'sample_path': 'crashes-duplicates/02484-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 226 bytes and sample mode 33188, this non-binary file is duplicated 15 times.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
