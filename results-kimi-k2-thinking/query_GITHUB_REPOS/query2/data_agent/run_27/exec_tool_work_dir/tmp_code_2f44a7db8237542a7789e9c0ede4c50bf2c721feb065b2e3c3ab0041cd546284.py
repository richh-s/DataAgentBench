code = """import json
import re

# Read the Swift files data
swift_files_file = locals()['var_functions.query_db:26']
swift_files = []

if isinstance(swift_files_file, str) and swift_files_file.endswith('.json'):
    with open(swift_files_file, 'r') as f:
        swift_files = json.load(f)
else:
    swift_files = swift_files_file

print(f"Number of Swift files found: {len(swift_files)}")

# Parse repo_data_description to extract copy counts
file_copy_counts = []

for file_info in swift_files:
    desc = file_info.get('repo_data_description', '')
    file_id = file_info.get('id')
    repo_name = file_info.get('sample_repo_name')
    file_path = file_info.get('sample_path')
    
    # Extract copy count from description
    # Patterns like "appears 8 times", "duplicated 10 times", "copied 12 times"
    copy_match = re.search(r'(appears|duplicated|repeated|copied)\s+(\d+)\s+times?', desc)
    if copy_match:
        copy_count = int(copy_match.group(2))
        file_copy_counts.append({
            'id': file_id,
            'repo_name': repo_name,
            'file_path': file_path,
            'copy_count': copy_count,
            'description': desc
        })

# Sort by copy count descending
file_copy_counts.sort(key=lambda x: x['copy_count'], reverse=True)

print(f"Found {len(file_copy_counts)} Swift files with copy count info")
if file_copy_counts:
    print("Top 10 most copied Swift files:")
    for i, file_info in enumerate(file_copy_counts[:10]):
        print(f"{i+1}. Copies: {file_info['copy_count']}, Repo: {file_info['repo_name']}, Path: {file_info['file_path']}")

# Store results
result = {
    'total_files': len(file_copy_counts),
    'top_files': file_copy_counts[:20]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'swift_repo_count': 27429, 'swift_repos': [{'repo_name': 'e-Sixt/Swen', 'swift_bytes': 16364, 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'swift_bytes': 109540, 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'swift_bytes': 18238, 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'swift_bytes': 1723695, 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'swift_bytes': 585714, 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}, {'repo_name': 'Apemb/Compass', 'swift_bytes': 33632, 'language_description': 'The codebase includes: Swift (33,632 bytes), Shell (711 bytes), Ruby (434 bytes).'}, {'repo_name': 'toggl/superday', 'swift_bytes': 747765, 'language_description': 'The majority of the code is in Swift (747,765 bytes), followed by Ruby (3,949 bytes), Shell (393 bytes).'}, {'repo_name': 'malcommac/SwiftDate', 'swift_bytes': 419579, 'language_description': 'While most of the project is built in Swift (419,579 bytes), it also incorporates Ruby (767 bytes), Shell (169 bytes).'}, {'repo_name': 'chronotruck/CTKFlagPhoneNumber', 'swift_bytes': 87439, 'language_description': 'While most of the project is built in Swift (87,439 bytes), it also incorporates Ruby (2,165 bytes), Shell (65 bytes).'}, {'repo_name': 'zendobk/SwiftUtils', 'swift_bytes': 71711, 'language_description': 'While most of the project is built in Swift (71,711 bytes), it also incorporates Shell (3,156 bytes), Ruby (3,009 bytes).'}]}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'total_rows': '105'}], 'var_functions.query_db:16': [{'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.', 'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f'}, {'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.', 'id': '2808cc7dad1e963456a33387816a60edcd14e3c2'}, {'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.', 'id': '9ba1cd853975d7412462af7426bfff682bf12171'}, {'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.', 'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67'}, {'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.', 'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75'}, {'sample_path': 'notes/2.3.1.markdown', 'repo_data_description': 'With a file size of 865 bytes and sample mode 33188, this non-binary file is duplicated 8 times.', 'id': 'f25ac53133823982d0d8449be27871abdbd4a494'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/hana/monadic_fold_right.hpp', 'repo_data_description': 'It is a non-binary file of 4802 bytes, repeated 8 times in the dataset under mode 33188.', 'id': '814343a33660c53403791055ac5f502cee0644bd'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/metaparse/v1/iterate_c.hpp', 'repo_data_description': 'This file has a size of 588 bytes, is non-binary, and appears 8 times with sample mode 33188.', 'id': 'bb50f15deb162b39542ee69056036a8d659d5fc6'}, {'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java', 'repo_data_description': 'Non-binary content file (3675 bytes) seen 8 times, using sample mode 33188.', 'id': 'e8b52ec203d330ee3fbf0403a4dbe4383d14b450'}, {'sample_path': 'src/program/lwaftr/doc/benchmarks-v1.0/transient-self-test-gbps.png', 'repo_data_description': 'This file has a size of 26140 bytes, is binary, and appears 8 times with sample mode 33188.', 'id': 'b01f05a2533b4fbfc58b4f0987e99211afdc9678'}, {'sample_path': 'Samples/NET/cs/SimpleNTier/WpfUI/App.config', 'repo_data_description': 'With a file size of 336 bytes and sample mode 33188, this non-binary file is duplicated 8 times.', 'id': '13e40b4143150944245cf5bd02600567905e77e5'}, {'sample_path': 'config/services/pmwebapis.xml', 'repo_data_description': 'With a file size of 544 bytes and sample mode 33188, this non-binary file is duplicated 8 times.', 'id': 'e210013f3d2cf0decdd6aff2960e34194232b9bf'}, {'sample_path': '3rdparty/dyncall/doc/manual/dyncall_logo.svg', 'repo_data_description': 'Non-binary content file (21851 bytes) seen 8 times, using sample mode 33188.', 'id': '26992250b2176770379cd6c7ba84ed51ce422090'}, {'sample_path': 'browser/kango-1.7.6/samples/InternationalizationDemo/src/common/extension_info.json', 'repo_data_description': 'A 397-byte non-binary file appearing 8 times, with sample mode code 33188.', 'id': '6555b1a2f3b5fa0064c6336fc878a7995bd4fe4c'}, {'sample_path': 'src/TKXSDRAW/PACKAGES', 'repo_data_description': 'Non-binary content file (43 bytes) seen 8 times, using sample mode 33188.', 'id': 'da48d7c48ca7f6c4c734487af0f288a1bb9926a2'}, {'sample_path': 'examples/aes-cmac/aes-cmac.cpp', 'repo_data_description': 'The dataset includes this non-binary file, 9000 bytes in size and copied 8 times (mode: 33188).', 'id': '105b24078f81dbc0cc3fa255a83c2ec8789272d0'}, {'sample_path': 'app/src/main/java/com/github/baoti/pioneer/ui/news/list/INewsListView.java', 'repo_data_description': 'The dataset includes this non-binary file, 979 bytes in size and copied 8 times (mode: 33188).', 'id': '0698e877472abb2aaa3a9896c05a1cdeca1747ea'}, {'sample_path': 'aikau/src/main/resources/alfresco/services/i18n/ContentService_ja.properties', 'repo_data_description': 'The dataset includes this non-binary file, 2524 bytes in size and copied 8 times (mode: 33188).', 'id': '6982ea63025c042ddf8c58eebb1add752e614761'}, {'sample_path': 'aclImdb/train/pos/8062_8.txt', 'repo_data_description': 'The dataset includes this non-binary file, 3451 bytes in size and copied 8 times (mode: 33188).', 'id': 'b09dfb007c3beec5ec0bcb2c113a826849a6d68b'}, {'sample_path': 'serial.pub', 'repo_data_description': 'A 247-byte non-binary file appearing 8 times, with sample mode code 33188.', 'id': '1409a2c49c7e19c876e0e3d4344652888a5702c5'}], 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [], 'var_functions.query_db:30': []}

exec(code, env_args)
