code = """import json
import re

commits_data = locals()['var_function-call-507962262134349788']
languages_file_path = locals()['var_function-call-507962262134348277']

with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

languages_map = {item['repo_name']: item['language_description'] for item in languages_data}

target_repos = ["torvalds/linux", "tensorflow/tensorflow"]

def get_main_language_debug(description):
    print(f"DEBUG: Processing description: {description}")
    matches = re.findall(r'([a-zA-Z\+\#\.]+(?: [a-zA-Z\+\#\.]+)*) \(([\d,]+) bytes\)', description)
    print(f"DEBUG: Matches found: {matches}")
    
    if not matches:
        return None
    
    max_bytes = -1
    main_lang = None
    
    for lang, bytes_str in matches:
        bytes_count = int(bytes_str.replace(',', ''))
        if bytes_count > max_bytes:
            max_bytes = bytes_count
            main_lang = lang.strip()
            
    return main_lang

results = {}
for name in target_repos:
    desc = languages_map.get(name)
    if desc:
        main = get_main_language_debug(desc)
        results[name] = main
    else:
        results[name] = "NOT FOUND"

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13619765481203691763': ['commits', 'contents', 'files'], 'var_function-call-13619765481203693066': ['languages', 'repos', 'licenses'], 'var_function-call-507962262134349788': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-507962262134348277': 'file_storage/function-call-507962262134348277.json', 'var_function-call-7988308145770392283': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react', 'tensorflow/tensorflow']}

exec(code, env_args)
