code = """import json
import re

# Get the file path from the variable
file_path = locals()['var_function-call-8178203267907188823']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Regex to find copy count
# Patterns seen: "seen X times", "appearing X times", "duplicated X times", "copied X times", "repeated X times"
regex = re.compile(r'(?:seen|appearing|duplicated|copied|repeated)\s+(\d+)\s+times')

candidates = []

for item in data:
    desc = item.get('repo_data_description', '')
    # Check for non-binary
    if 'non-binary' in desc.lower():
        match = regex.search(desc)
        if match:
            count = int(match.group(1))
            candidates.append({
                'id': item['id'],
                'sample_repo_name': item['sample_repo_name'],
                'count': count,
                'path': item.get('sample_path', '')
            })

# Sort by count descending
candidates.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps(candidates[:5]))"""

env_args = {'var_function-call-14403404163765122327': ['commits', 'contents', 'files'], 'var_function-call-13071292822670688676': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-16106151830741967884': [{'repo_data_description': 'Binary content file (462 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'Binary content file (593 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'Binary content file (456 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'Binary content file (596 bytes) seen 8 times, using sample mode 33188.'}, {'repo_data_description': 'Binary content file (31184 bytes) seen 8 times, using sample mode 33188.'}], 'var_function-call-11393151851164692853': [{'count_star()': '105'}], 'var_function-call-8178203267907188823': 'file_storage/function-call-8178203267907188823.json'}

exec(code, env_args)
