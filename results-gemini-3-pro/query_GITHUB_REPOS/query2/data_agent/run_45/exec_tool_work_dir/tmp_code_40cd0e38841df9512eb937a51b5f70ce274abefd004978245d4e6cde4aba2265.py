code = """import json
import re

file_path = locals()['var_function-call-12146207024763606278']
with open(file_path, 'r') as f:
    data = json.load(f)

max_copies = -1
ties = []

for item in data:
    desc = item['repo_data_description']
    match = re.search(r'(\d+)\s+times', desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            ties = [item]
        elif copies == max_copies:
            ties.append(item)

print("__RESULT__:")
print(json.dumps(ties))"""

env_args = {'var_function-call-8690036921960868837': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-8690036921960868172': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-14230385318039386849': [{'count_star()': '89'}], 'var_function-call-12146207024763606278': 'file_storage/function-call-12146207024763606278.json', 'var_function-call-1678352776284954031': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}, 'var_function-call-8827290552773009548': [], 'var_function-call-8827290552773011561': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_function-call-13800483334302068365': [], 'var_function-call-2961727954446671006': [{'count_star()': '524077'}], 'var_function-call-2961727954446670983': [{'repo_name': 'uacaps/PageMenu', 'watch_count': '487'}], 'var_function-call-14554599819442144125': [{'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift'}], 'var_function-call-745374599180643640': [], 'var_function-call-8247249704105754124': [{'repo_name': 'kostiakoval/Mirror', 'language_description': 'The codebase includes: Swift (28,389 bytes), Ruby (1,160 bytes), Objective-C (480 bytes).'}], 'var_function-call-5149243925605355263': [{'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}]}

exec(code, env_args)
