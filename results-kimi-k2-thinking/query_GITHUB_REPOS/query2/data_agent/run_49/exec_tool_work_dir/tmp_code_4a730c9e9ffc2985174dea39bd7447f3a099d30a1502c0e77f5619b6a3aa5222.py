code = """# Load the full Swift files data
swift_files = locals()['var_functions.query_db:24']

# Check if it's a file path or direct data
import json
import os
import re

if isinstance(swift_files, str) and swift_files.endswith('.json'):
    with open(swift_files, 'r') as f:
        swift_files = json.load(f)

# Extract copy counts from repo_data_description
def extract_copy_count(description):
    # Patterns to match:
    # - "duplicated X times"
    # - "appears X times"
    # - "copied X times"
    # - "repeated X times"
    patterns = [
        r'duplicated\s+(\d+)\s+time',
        r'appears\s+(\d+)\s+time',
        r'copied\s+(\d+)\s+time',
        r'repeated\s+(\d+)\s+time'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return 1  # Default to 1 if no pattern found

# Process all Swift files
processed_files = []
for file_data in swift_files:
    copy_count = extract_copy_count(file_data['repo_data_description'])
    processed_files.append({
        'id': file_data['id'],
        'repo_name': file_data['sample_repo_name'],
        'path': file_data['sample_path'],
        'copy_count': copy_count,
        'description': file_data['repo_data_description']
    })

# Sort by copy count descending
processed_files.sort(key=lambda x: x['copy_count'], reverse=True)

# Group files by copy count to see distribution
copy_count_distribution = {}
for file in processed_files:
    count = file['copy_count']
    copy_count_distribution[count] = copy_count_distribution.get(count, 0) + 1

# Find the highest copy count
highest_copy_count = processed_files[0]['copy_count']
most_copied_files = [f for f in processed_files if f['copy_count'] == highest_copy_count]

print('__RESULT__:')
print(json.dumps({
    'highest_copy_count': highest_copy_count,
    'num_files_with_highest_count': len(most_copied_files),
    'most_copied_files': most_copied_files,
    'copy_count_distribution': copy_count_distribution,
    'total_swift_files': len(processed_files)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'num_swift_repos': 42605, 'first_few_repos': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}]}, 'var_functions.query_db:12': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_functions.query_db:14': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [], 'var_functions.query_db:20': [{'total_swift_files': '105'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'all_files_count': 105, 'files_with_copy_count': 105, 'first_few_all': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}], 'first_few_copy': [{'id': '061e1b677455b609b3725754014caf28d5775d42', 'sample_repo_name': 'onmyway133/Scale', 'sample_path': 'Example/Scale/AppDelegate.swift', 'repo_data_description': 'With a file size of 2140 bytes and sample mode 33188, this non-binary file is duplicated 1 times.'}, {'id': '0712bc9ab52f2682d220bb189f62d942ed11c7fa', 'sample_repo_name': '0xc010d/VFLToolbox', 'sample_path': 'VFLToolbox/Formula/Constraint.swift', 'repo_data_description': 'With a file size of 1948 bytes and sample mode 33188, this non-binary file is duplicated 3 times.'}, {'id': '0989d91c91a2ae2d15225e64b34ffbebe9b98db0', 'sample_repo_name': 'rugheid/Swift-MathEagle', 'sample_path': 'MathEagleTests/ComplexTests.swift', 'repo_data_description': 'This file has a size of 3924 bytes, is non-binary, and appears 1 times with sample mode 33188.'}]}}

exec(code, env_args)
