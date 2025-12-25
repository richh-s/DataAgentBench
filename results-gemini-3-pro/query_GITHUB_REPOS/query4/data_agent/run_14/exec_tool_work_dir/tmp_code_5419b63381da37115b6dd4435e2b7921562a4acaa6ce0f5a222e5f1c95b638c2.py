code = """import json

with open(locals()['var_function-call-4552926070102299372'], 'r') as f:
    languages_data = json.load(f)

repo_name = "torvalds/linux"
found_item = None
for item in languages_data:
    if item['repo_name'] == repo_name:
        found_item = item
        break
        
print("__RESULT__:")
print(json.dumps({"found_item": found_item}))"""

env_args = {'var_function-call-15579391546040287460': ['languages', 'repos', 'licenses'], 'var_function-call-15579391546040288403': ['commits', 'contents', 'files'], 'var_function-call-406465522556242917': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-1803186809871716056': 'file_storage/function-call-1803186809871716056.json', 'var_function-call-4552926070102299372': 'file_storage/function-call-4552926070102299372.json', 'var_function-call-4552926070102302235': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-13284210856608587587': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react', 'tensorflow/tensorflow']}

exec(code, env_args)
