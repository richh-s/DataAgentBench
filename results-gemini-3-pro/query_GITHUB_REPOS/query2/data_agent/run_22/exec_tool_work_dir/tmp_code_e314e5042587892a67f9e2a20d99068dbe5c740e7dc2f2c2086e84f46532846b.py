code = """import json
import re

with open(locals()['var_function-call-13308710563610632099'], 'r') as f:
    records = json.load(f)

max_copies = -1
candidates = []

pattern = re.compile(r'([\d,]+)\s+times')

for rec in records:
    desc = rec.get('repo_data_description', '')
    match = pattern.search(desc)
    if match:
        count_str = match.group(1).replace(',', '')
        count = int(count_str)
        if count > max_copies:
            max_copies = count
            candidates = [rec]
        elif count == max_copies:
            candidates.append(rec)

print("__RESULT__:")
print(json.dumps({"max_copies": max_copies, "candidates": candidates}))"""

env_args = {'var_function-call-6760782311447027470': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-6760782311447025991': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-12172347712947698703': [{'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copy_count': '1'}, {'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copy_count': '1'}], 'var_function-call-8396033359940187752': [{'id': 'a6fb31fa1e4b1647e8862580703add8c6205c6d1', 'cnt': '4'}, {'id': 'f64ee245678dcb26d658600708e2996a7608fc6e', 'cnt': '2'}, {'id': 'a1615a71d1bdbb036d1dde0a94b8285fa8fca084', 'cnt': '2'}, {'id': '53496cde05c660feb3ab3335e825b363aa68a51a', 'cnt': '2'}, {'id': '8af9111216436874eecfaa475d5c2f3ac650e3bc', 'cnt': '2'}], 'var_function-call-14498965116600895182': [], 'var_function-call-916819524649565680': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copy_count': '1'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copy_count': '1'}], 'var_function-call-13308710563610632099': 'file_storage/function-call-13308710563610632099.json', 'var_function-call-10680247206382184202': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'max_copies': 38, 'sample_repo': 'uacaps/PageMenu'}, 'var_function-call-10016013425642523852': [], 'var_function-call-11182386557603600349': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_function-call-3008030937835516359': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'max_copies': 38, 'sample_repo': 'uacaps/PageMenu', 'desc': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}, 'var_function-call-10094172368846169917': [{'repo_name': 'uacaps/PageMenu', 'watch_count': '487'}]}

exec(code, env_args)
