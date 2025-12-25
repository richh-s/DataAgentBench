code = """import json
import re

# Get the file path from the variable
file_path = locals()['var_function-call-6796978219201560832']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Regex to extract count
# Patterns seen: "seen X times", "duplicated X times", "appears X times", "repeated X times", "copied X times"
pattern = re.compile(r'(?:seen|duplicated|appears|repeated|copied)\s+(\d+)\s+times')

max_count = -1
best_file = None

for item in data:
    desc = item.get('repo_data_description', '')
    match = pattern.search(desc)
    if match:
        count = int(match.group(1))
        if count > max_count:
            max_count = count
            best_file = item

print("__RESULT__:")
print(json.dumps(best_file))"""

env_args = {'var_function-call-436327041952697564': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.', 'sample_path': 'device/nfc/nfc.mojom'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.', 'sample_path': 'lib/cUnix.mli'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.', 'sample_path': 'json4s/src/main/ls/0.6.5.json'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg'}], 'var_function-call-436327041952697885': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-12290941396940329571': [{'count_star()': '89'}], 'var_function-call-6796978219201560832': 'file_storage/function-call-6796978219201560832.json'}

exec(code, env_args)
