code = """import json
import re

# Get the file path from the variable
file_path = locals()['var_function-call-3046721292762974421']

# Load the result from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Regex to find copy count
copy_pattern = re.compile(r'(?:seen|appearing|appears|repeated|duplicated|copied)\s+(\d+)\s+times')

results = []

for entry in data:
    desc = entry.get('repo_data_description', '').lower()
    
    # Check if non-binary
    if 'non-binary' not in desc:
        continue
        
    # Extract copy count
    match = copy_pattern.search(desc)
    if match:
        copies = int(match.group(1))
        results.append({
            'id': entry['id'],
            'sample_repo_name': entry['sample_repo_name'],
            'sample_path': entry['sample_path'],
            'copies': copies
        })

# Sort by copies descending
results.sort(key=lambda x: x['copies'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:10]))"""

env_args = {'var_function-call-14741054177989663846': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-3046721292762974421': 'file_storage/function-call-3046721292762974421.json'}

exec(code, env_args)
