code = """import json
import re

# Load the query result
with open(locals()['var_function-call-11496198756874579014'], 'r') as f:
    data = json.load(f)

# Regex to find copy count
# Patterns seen: 
# "seen X times"
# "duplicated X times"
# "copied X times"
# "repeated X times"
# "appears X times"
# "appearing X times"

pattern = re.compile(r'(?:seen|duplicated|copied|repeated|appears|appearing)\s+(\d+)\s+times', re.IGNORECASE)

max_copies = -1
best_file = None

for entry in data:
    desc = entry.get('repo_data_description', '')
    match = pattern.search(desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            best_file = entry
    else:
        # If pattern not found, maybe look closer? 
        # But for now assume the patterns cover most cases.
        pass

print("__RESULT__:")
print(json.dumps(best_file))"""

env_args = {'var_function-call-15541582446204944311': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-11496198756874579014': 'file_storage/function-call-11496198756874579014.json'}

exec(code, env_args)
