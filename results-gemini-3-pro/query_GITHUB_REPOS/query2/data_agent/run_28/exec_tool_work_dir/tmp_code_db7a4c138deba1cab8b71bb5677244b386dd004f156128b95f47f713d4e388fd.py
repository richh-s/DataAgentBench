code = """import json
import re

# Load the result from the previous query
with open('var_function-call-3272185907144915276.json', 'r') as f:
    data = json.load(f)

max_copies = -1
max_id = None

# Regex to capture the number of copies
# Patterns seen: "seen X times", "duplicated X times", "repeated X times", "copied X times", "appears X times"
pattern = re.compile(r"(?:seen|duplicated|repeated|copied|appears)\s+(\d+)\s+times")

for entry in data:
    desc = entry.get('repo_data_description', '')
    match = pattern.search(desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            max_id = entry['id']

print("__RESULT__:")
print(json.dumps({"max_id": max_id, "max_copies": max_copies}))"""

env_args = {'var_function-call-435749997997257662': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-435749997997259331': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-9274331157922824869': [{'count_star()': '105'}], 'var_function-call-3272185907144915276': 'file_storage/function-call-3272185907144915276.json'}

exec(code, env_args)
