code = """import json
import re

with open(locals()['var_function-call-11496198756874579014'], 'r') as f:
    data = json.load(f)

pattern = re.compile(r'(?:seen|duplicated|copied|repeated|appears|appearing)\s+(\d+)\s+times', re.IGNORECASE)

files_with_counts = []
for entry in data:
    desc = entry.get('repo_data_description', '')
    match = pattern.search(desc)
    if match:
        count = int(match.group(1))
        files_with_counts.append((count, entry))

# Sort by count descending
files_with_counts.sort(key=lambda x: x[0], reverse=True)

print("__RESULT__:")
print(json.dumps([f[1] for f in files_with_counts[:5]]))"""

env_args = {'var_function-call-15541582446204944311': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-11496198756874579014': 'file_storage/function-call-11496198756874579014.json', 'var_function-call-4975723978102769331': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift'}, 'var_function-call-414105683910853777': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_function-call-3944732475793156689': [], 'var_function-call-5889145276197690014': [{'id': '316ad972693d0355c3504729fff14287419e004d', 'repo_name': 'np/ling'}, {'id': 'daa40d563068ee94f01b1e87952d607a6588a589', 'repo_name': 'np/ling'}, {'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a', 'repo_name': 'np/ling'}, {'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969', 'repo_name': 'np/ling'}, {'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6', 'repo_name': 'np/ling'}]}

exec(code, env_args)
