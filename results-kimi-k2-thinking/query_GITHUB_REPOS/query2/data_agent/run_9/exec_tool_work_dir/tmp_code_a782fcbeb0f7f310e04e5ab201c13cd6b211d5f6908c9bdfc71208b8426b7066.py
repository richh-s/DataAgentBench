code = """import json

# Get Swift repositories from metadata database
swift_repos_result = locals()['var_functions.query_db:24']

if isinstance(swift_repos_result, str) and swift_repos_result.endswith('.json'):
    with open(swift_repos_result, 'r') as f:
        swift_repos_data = json.load(f)
else:
    swift_repos_data = swift_repos_result

# Extract repository names into a set for fast lookup
swift_repo_names = set([repo['repo_name'] for repo in swift_repos_data])

# Check if the repository with max copies is in Swift repos
max_copies_file = {
    "id": "6f4cdb70f044b0486a24a07403600cb964a02672",
    "sample_repo_name": "uacaps/PageMenu",
    "sample_path": "Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift",
    "repo_data_description": "It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188."
}

is_swift_repo = max_copies_file['sample_repo_name'] in swift_repo_names

# Also check if there might be other files with similar high copy counts
swift_files_result = locals()['var_functions.query_db:40']
if isinstance(swift_files_result, str) and swift_files_result.endswith('.json'):
    with open(swift_files_result, 'r') as f:
        swift_files_data = json.load(f)
else:
    swift_files_data = swift_files_result

# Double check for any file with 38+ copies
import re
copy_pattern = r'(?:duplicated|copied|appears|repeated) (\d+) times?'

max_copies = 0
best_file = None

for file_info in swift_files_data:
    description = file_info.get('repo_data_description', '')
    match = re.search(copy_pattern, description, re.IGNORECASE)
    if match:
        copies = int(match.group(1))
        repo_name = file_info.get('sample_repo_name')
        if copies > max_copies and repo_name in swift_repo_names:
            max_copies = copies
            best_file = file_info

print('__RESULT__:')
print(json.dumps({
    'is_max_file_in_swift_repo': is_swift_repo,
    'max_copies_confirmed': max_copies,
    'best_file': best_file,
    'target_repo_in_swift_list': "uacaps/PageMenu" in swift_repo_names
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'e-Sixt/Swen'}, {'repo_name': 'ApplauseOSS/Swifjection'}, {'repo_name': 'vizifit/GenericPasswordRow'}, {'repo_name': 'cxy921126/SoftSwift'}, {'repo_name': 'cwwise/CWWeChat'}, {'repo_name': 'Apemb/Compass'}, {'repo_name': 'toggl/superday'}, {'repo_name': 'malcommac/SwiftDate'}, {'repo_name': 'chronotruck/CTKFlagPhoneNumber'}, {'repo_name': 'zendobk/SwiftUtils'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}, {'id': 'f25ac53133823982d0d8449be27871abdbd4a494', 'sample_repo_name': 'scalatra/scalatra', 'sample_path': 'notes/2.3.1.markdown', 'repo_data_description': 'With a file size of 865 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '814343a33660c53403791055ac5f502cee0644bd', 'sample_repo_name': 'arangodb/arangodb', 'sample_path': '3rdParty/boost/1.61.0b1/boost/hana/monadic_fold_right.hpp', 'repo_data_description': 'It is a non-binary file of 4802 bytes, repeated 8 times in the dataset under mode 33188.'}, {'id': 'bb50f15deb162b39542ee69056036a8d659d5fc6', 'sample_repo_name': 'arangodb/arangodb', 'sample_path': '3rdParty/boost/1.61.0b1/boost/metaparse/v1/iterate_c.hpp', 'repo_data_description': 'This file has a size of 588 bytes, is non-binary, and appears 8 times with sample mode 33188.'}, {'id': 'e8b52ec203d330ee3fbf0403a4dbe4383d14b450', 'sample_repo_name': 'apache/derby', 'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java', 'repo_data_description': 'Non-binary content file (3675 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'b01f05a2533b4fbfc58b4f0987e99211afdc9678', 'sample_repo_name': 'Igalia/snabb', 'sample_path': 'src/program/lwaftr/doc/benchmarks-v1.0/transient-self-test-gbps.png', 'repo_data_description': 'This file has a size of 26140 bytes, is binary, and appears 8 times with sample mode 33188.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': 'file_', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'count': 42605, 'first_few': [{'repo_name': 'e-Sixt/Swen'}, {'repo_name': 'ApplauseOSS/Swifjection'}, {'repo_name': 'vizifit/GenericPasswordRow'}, {'repo_name': 'cxy921126/SoftSwift'}, {'repo_name': 'cwwise/CWWeChat'}]}, 'var_functions.query_db:30': [{'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}, {'repo_data_description': 'With a file size of 865 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'repo_data_description': 'It is a non-binary file of 4802 bytes, repeated 8 times in the dataset under mode 33188.'}, {'repo_data_description': 'This file has a size of 588 bytes, is non-binary, and appears 8 times with sample mode 33188.'}, {'repo_data_description': 'Non-binary content file (3675 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'This file has a size of 26140 bytes, is binary, and appears 8 times with sample mode 33188.'}, {'repo_data_description': 'With a file size of 336 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'repo_data_description': 'With a file size of 544 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'repo_data_description': 'Non-binary content file (21851 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'A 397-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'repo_data_description': 'Non-binary content file (43 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'The dataset includes this non-binary file, 9000 bytes in size and copied 8 times (mode: 33188).'}, {'repo_data_description': 'The dataset includes this non-binary file, 979 bytes in size and copied 8 times (mode: 33188).'}, {'repo_data_description': 'The dataset includes this non-binary file, 2524 bytes in size and copied 8 times (mode: 33188).'}, {'repo_data_description': 'The dataset includes this non-binary file, 3451 bytes in size and copied 8 times (mode: 33188).'}, {'repo_data_description': 'A 247-byte non-binary file appearing 8 times, with sample mode code 33188.'}], 'var_functions.execute_python:32': {'swift_repo_count': 42605, 'sample_sql_conditions': "sample_repo_name = 'e-Sixt/Swen' OR sample_repo_name = 'ApplauseOSS/Swifjection' OR sample_repo_name = 'vizifit/GenericPasswordRow' OR sample_repo_name = 'cxy921126/SoftSwift' OR sample_repo_name = 'cwwise/CWWeChat' OR sample_repo_name = 'Apemb/Compass' OR sample_repo_name = 'toggl/superday' OR samp"}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'max_copies': 38, 'file_info': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}}}

exec(code, env_args)
