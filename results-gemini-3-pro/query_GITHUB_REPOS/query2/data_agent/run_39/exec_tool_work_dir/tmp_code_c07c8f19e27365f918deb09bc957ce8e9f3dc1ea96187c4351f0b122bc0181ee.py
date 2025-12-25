code = """import json

with open(locals()['var_function-call-4082122974327051000'], 'r') as f:
    data = json.load(f)

target_id = "6f4cdb70f044b0486a24a07403600cb964a02672"
for item in data:
    if item['id'] == target_id:
        print("__RESULT__:")
        print(json.dumps(item))
        break"""

env_args = {'var_function-call-4610002158733760041': ['commits', 'contents', 'files'], 'var_function-call-13233484506308516938': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli', 'repo_data_description': 'A 2526-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg', 'repo_data_description': 'This file has a size of 2954 bytes, is non-binary, and appears 8 times with sample mode 33188.'}], 'var_function-call-14273510091529888919': [{'count_star()': '105'}], 'var_function-call-4082122974327051000': 'file_storage/function-call-4082122974327051000.json', 'var_function-call-14690061221934093139': {'repo': 'uacaps/PageMenu', 'copies': 38, 'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'desc': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}}

exec(code, env_args)
