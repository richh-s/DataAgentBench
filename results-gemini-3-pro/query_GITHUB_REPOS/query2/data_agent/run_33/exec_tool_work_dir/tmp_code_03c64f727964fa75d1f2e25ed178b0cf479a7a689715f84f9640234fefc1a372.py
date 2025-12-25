code = """import json
import re

# Load the result from the previous tool call
# var_function-call-10129500024059362760 contains the path to the JSON file
file_path = locals()['var_function-call-10129500024059362760']
with open(file_path, 'r') as f:
    data = json.load(f)

def extract_copies(desc):
    # Patterns for copy count
    # "seen 8 times"
    # "appearing 8 times"
    # "appears 9 times"
    # "duplicated 10 times"
    # "copied 12 times"
    # "repeated 15 times"
    
    # Combined regex
    match = re.search(r'(?:seen|appearing|appears|duplicated|copied|repeated)\s+(\d+)\s+times', desc)
    if match:
        return int(match.group(1))
    return 0

results = []
for item in data:
    copies = extract_copies(item['repo_data_description'])
    results.append({
        'id': item['id'],
        'repo': item['sample_repo_name'],
        'copies': copies
    })

# Sort by copies descending
results.sort(key=lambda x: x['copies'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:10]))"""

env_args = {'var_function-call-5227546589164281979': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-8086570677736900779': [{'count_star()': '89'}], 'var_function-call-10129500024059362760': 'file_storage/function-call-10129500024059362760.json'}

exec(code, env_args)
