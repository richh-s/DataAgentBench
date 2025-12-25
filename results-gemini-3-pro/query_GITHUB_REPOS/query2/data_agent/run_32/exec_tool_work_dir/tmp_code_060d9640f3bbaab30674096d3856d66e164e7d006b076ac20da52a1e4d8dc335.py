code = """import json
import re

with open('var_function-call-3486998471131883368.json', 'r') as f:
    data = json.load(f)

result_list = []

for item in data:
    desc = item.get('repo_data_description', '')
    
    # Check if non-binary
    if 'non-binary' not in desc.lower():
        continue

    # Extract count
    # Patterns:
    # seen X times
    # repeated X times
    # copied X times
    # duplicated X times
    # appearing X times
    # appears X times
    
    match = re.search(r'(?:seen|repeated|copied|duplicated|appearing|appears)\s+(\d+)\s+times', desc)
    if match:
        count = int(match.group(1))
        result_list.append({
            'id': item['id'],
            'count': count,
            'sample_repo_name': item['sample_repo_name'],
            'sample_path': item.get('sample_path', '') # Not requested but useful
        })

# Sort by count descending
result_list.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps(result_list[:10]))"""

env_args = {'var_function-call-1642771150100073436': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.', 'sample_path': 'device/nfc/nfc.mojom'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.', 'sample_path': 'lib/cUnix.mli'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.', 'sample_path': 'json4s/src/main/ls/0.6.5.json'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg'}], 'var_function-call-3486998471131883368': 'file_storage/function-call-3486998471131883368.json'}

exec(code, env_args)
