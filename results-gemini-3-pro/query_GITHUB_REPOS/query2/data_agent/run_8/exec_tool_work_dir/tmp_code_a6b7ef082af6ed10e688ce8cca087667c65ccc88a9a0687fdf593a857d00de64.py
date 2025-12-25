code = """import json
import re

file_path = locals()['var_function-call-43427940192881032']
with open(file_path, 'r') as f:
    data = json.load(f)

max_copies = -1
candidates = []

patterns = [
    r"copied (\d+) times",
    r"repeated (\d+) times",
    r"appearing (\d+) times",
    r"appears (\d+) times",
    r"duplicated (\d+) times",
    r"seen (\d+) times"
]

# First pass to find max
for item in data:
    desc = item.get('repo_data_description', '')
    copies = 0
    for pat in patterns:
        match = re.search(pat, desc)
        if match:
            copies = int(match.group(1))
            break
    if copies > max_copies:
        max_copies = copies

# Second pass to collect all candidates
for item in data:
    desc = item.get('repo_data_description', '')
    copies = 0
    for pat in patterns:
        match = re.search(pat, desc)
        if match:
            copies = int(match.group(1))
            break
    if copies == max_copies:
        candidates.append(item)

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-6873153169641065013': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-8478554410488526240': [{'count_star()': '89'}], 'var_function-call-43427940192881032': 'file_storage/function-call-43427940192881032.json', 'var_function-call-12055316186000777544': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.', 'parsed_copies': 38}, 'var_function-call-9682194306002384355': [], 'var_function-call-17694614949631728834': [], 'var_function-call-13486632226811815128': [{'count_star()': '524077'}], 'var_function-call-3546330234111903142': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}]}

exec(code, env_args)
