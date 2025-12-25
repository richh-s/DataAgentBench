code = """import json
import re

# Load the result from the previous query
file_path = locals()['var_function-call-17591085962227246708']
with open(file_path, 'r') as f:
    data = json.load(f)

max_copies = -1
best_id = None
regex = re.compile(r'(?:seen|duplicated|repeated|appears|copied)\s+(\d+)\s+times', re.IGNORECASE)

for item in data:
    desc = item.get('repo_data_description', '')
    match = regex.search(desc)
    if match:
        count = int(match.group(1))
        if count > max_copies:
            max_copies = count
            best_id = item['id']

print("__RESULT__:")
print(json.dumps({"id": best_id, "max_copies": max_copies}))"""

env_args = {'var_function-call-11869439743162173103': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11869439743162173488': 'file_storage/function-call-11869439743162173488.json', 'var_function-call-13103241597973200793': [{'id': '1ad86cf8e815fce652aa101d654485fea8033954', 'repo_data_description': 'Non-binary content file (215 bytes) seen 15 times, using sample mode 33188.'}, {'id': '1c6815216db5b95a45adef969aa7bf81e99b36c2', 'repo_data_description': 'Non-binary content file (398 bytes) seen 21 times, using sample mode 33188.'}, {'id': '760f115984630b588b915a6bed1e73894425d524', 'repo_data_description': 'Non-binary content file (271 bytes) seen 22 times, using sample mode 33188.'}, {'id': '5cfc8fe3f8c6c07e7bc11d632be5034d9cc19c62', 'repo_data_description': 'Non-binary content file (863 bytes) seen 1 times, using sample mode 33188.'}, {'id': 'c489dfee601c57ab8286c344b65b8d8d60a1df18', 'repo_data_description': 'Non-binary content file (1747 bytes) seen 1 times, using sample mode 33188.'}, {'id': '1e6441e8ff6c2dbbf44790b449820a80e9e54622', 'repo_data_description': 'Non-binary content file (4279 bytes) seen 1 times, using sample mode 33188.'}, {'id': '9ef2e30e948f45194e614aca0e7a18cef17836e1', 'repo_data_description': 'Non-binary content file (7360 bytes) seen 1 times, using sample mode 33261.'}, {'id': '162de135e92f4ae00ac81826c734ec1e5a44f182', 'repo_data_description': 'Non-binary content file (2987 bytes) seen 2 times, using sample mode 33188.'}, {'id': 'c236a42435aa5e367f87077c802b0a77e8047faa', 'repo_data_description': 'Non-binary content file (2535 bytes) seen 1 times, using sample mode 33188.'}, {'id': '41ce8772198f7ae1e283c21438cb0c6b3e941b19', 'repo_data_description': 'Non-binary content file (1729 bytes) seen 1 times, using sample mode 33188.'}, {'id': '997bf94818ee5a6b44790a9a634b855478205029', 'repo_data_description': 'Non-binary content file (1920 bytes) seen 1 times, using sample mode 33188.'}, {'id': '1f63b3ceb821ef39296b65b13366ccb7c8e363b6', 'repo_data_description': 'Non-binary content file (8942 bytes) seen 1 times, using sample mode 33188.'}, {'id': 'bf10fb7332af537f4430a4af4b05018265c382e3', 'repo_data_description': 'Non-binary content file (1857 bytes) seen 1 times, using sample mode 33188.'}, {'id': 'd092b9cc4cbe94df4ebb747187caffeefbbed0ab', 'repo_data_description': 'Non-binary content file (1268 bytes) seen 2 times, using sample mode 33188.'}, {'id': 'f6ec334d38084d8ff0ffa388e8550b01e245ea60', 'repo_data_description': 'Non-binary content file (20194 bytes) seen 7 times, using sample mode 33261.'}, {'id': '2406d0daa2ba71a23ccbabc6e5ce3bb45d64ca8f', 'repo_data_description': 'Non-binary content file (3872 bytes) seen 3 times, using sample mode 33188.'}], 'var_function-call-17591085962227246708': 'file_storage/function-call-17591085962227246708.json'}

exec(code, env_args)
