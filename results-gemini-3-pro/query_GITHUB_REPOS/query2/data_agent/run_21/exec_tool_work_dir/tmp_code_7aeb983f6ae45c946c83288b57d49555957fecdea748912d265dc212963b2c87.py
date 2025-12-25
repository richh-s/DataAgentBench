code = """import json
import re

with open(locals()['var_function-call-8678929752017260060'], 'r') as f:
    records = json.load(f)

pattern = re.compile(r'(?:seen|appearing|appears|duplicated|copied|repeated)\s+(\d+)\s+times', re.IGNORECASE)

max_copies = 38 # from previous finding
candidates = []

for rec in records:
    desc = rec['repo_data_description']
    if 'non-binary' not in desc.lower():
        continue
    match = pattern.search(desc)
    if match:
        copies = int(match.group(1))
        if copies == max_copies:
            candidates.append(rec)

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-2129303542318089801': ['commits', 'contents', 'files'], 'var_function-call-3598620817718079374': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-8791524838464828215': [{'count_star()': '105'}], 'var_function-call-8678929752017260060': 'file_storage/function-call-8678929752017260060.json', 'var_function-call-9893853558552638339': {'max_file': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}, 'max_copies': 38}, 'var_function-call-427441803666800052': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_function-call-12791259213936296375': [], 'var_function-call-8493045235778202479': [{'id': '316ad972693d0355c3504729fff14287419e004d'}], 'var_function-call-9614213769388339063': [], 'var_function-call-58327498718443368': [{'count_star()': '524077'}]}

exec(code, env_args)
