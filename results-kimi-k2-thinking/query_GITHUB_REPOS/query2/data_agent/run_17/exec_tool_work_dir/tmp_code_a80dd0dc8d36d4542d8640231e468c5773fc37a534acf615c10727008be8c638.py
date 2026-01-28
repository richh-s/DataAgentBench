code = """import json
import re

# Get the file path from storage
file_path = locals()['var_functions.query_db:30']

# Read the Swift files data
with open(file_path, 'r') as f:
    swift_files = json.load(f)

# Function to extract copy count from description - look for the pattern specifically
# Looking for words like "duplicated", "copied", "appearing", "repeated" followed by a number
# and the word "times"
def get_copy_count(desc):
    if not desc:
        return 0
    # Look for pattern: word (duplicated/copied/appearing/repeated) [number] times
    match = re.search(r'(?:duplicated|copied|appearing|repeated).*?(\d+).*?times', desc, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 0

# Find file with maximum copies
max_copies = 0
max_file = None

for file_data in swift_files:
    copies = get_copy_count(file_data['repo_data_description'])
    if copies > max_copies:
        max_copies = copies
        max_file = file_data

result = {
    'max_actual_copies': max_copies,
    'file_info': max_file,
    'total_files': len(swift_files),
    'examples': swift_files[:3]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}, {'id': 'f25ac53133823982d0d8449be27871abdbd4a494', 'sample_repo_name': 'scalatra/scalatra', 'sample_path': 'notes/2.3.1.markdown', 'repo_data_description': 'With a file size of 865 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '814343a33660c53403791055ac5f502cee0644bd', 'sample_repo_name': 'arangodb/arangodb', 'sample_path': '3rdParty/boost/1.61.0b1/boost/hana/monadic_fold_right.hpp', 'repo_data_description': 'It is a non-binary file of 4802 bytes, repeated 8 times in the dataset under mode 33188.'}, {'id': 'bb50f15deb162b39542ee69056036a8d659d5fc6', 'sample_repo_name': 'arangodb/arangodb', 'sample_path': '3rdParty/boost/1.61.0b1/boost/metaparse/v1/iterate_c.hpp', 'repo_data_description': 'This file has a size of 588 bytes, is non-binary, and appears 8 times with sample mode 33188.'}, {'id': 'e8b52ec203d330ee3fbf0403a4dbe4383d14b450', 'sample_repo_name': 'apache/derby', 'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java', 'repo_data_description': 'Non-binary content file (3675 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'b01f05a2533b4fbfc58b4f0987e99211afdc9678', 'sample_repo_name': 'Igalia/snabb', 'sample_path': 'src/program/lwaftr/doc/benchmarks-v1.0/transient-self-test-gbps.png', 'repo_data_description': 'This file has a size of 26140 bytes, is binary, and appears 8 times with sample mode 33188.'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:22': [{'repo_name': '007HelloWorld/DouYuZhiBo'}, {'repo_name': '00aney/Briefinsta'}, {'repo_name': '00buggy00/SwiftOpenGLTutorials'}, {'repo_name': '0111b/JSONDecoder-Keypath'}, {'repo_name': '0111b/adventofcode.2016'}, {'repo_name': '01miru/HomeSense'}, {'repo_name': '031240302/DouYuZB'}, {'repo_name': '0359xiaodong/GoogleWearAlert'}, {'repo_name': '0416354917/FeedMeIOS'}, {'repo_name': '07cs07/Design-Patterns-In-Swift'}], 'var_functions.query_db:26': [], 'var_functions.query_db:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'max_copies': 53633, 'file_info': {'id': 'ed6d246019341c2a92b56578ddf49576577cc36b', 'sample_repo_name': 'watson-developer-cloud/ios-sdk', 'sample_path': 'Source/VisualRecognitionV3/Tests/VisualRecognitionTests.swift', 'repo_data_description': 'With a file size of 53633 bytes and sample mode 33188, this non-binary file is duplicated 1 times.'}, 'total_files': 69}, 'var_functions.execute_python:38': {'max_copies': 53633, 'file_info': {'id': 'ed6d246019341c2a92b56578ddf49576577cc36b', 'sample_repo_name': 'watson-developer-cloud/ios-sdk', 'sample_path': 'Source/VisualRecognitionV3/Tests/VisualRecognitionTests.swift', 'repo_data_description': 'With a file size of 53633 bytes and sample mode 33188, this non-binary file is duplicated 1 times.'}, 'total_files': 69}}

exec(code, env_args)
