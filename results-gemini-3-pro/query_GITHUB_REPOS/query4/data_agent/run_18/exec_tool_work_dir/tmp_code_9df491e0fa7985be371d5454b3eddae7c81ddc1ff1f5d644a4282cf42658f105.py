code = """import json

# Load commit counts
commits_data = locals()['var_function-call-993125701442150257']
linux_commits = next((item for item in commits_data if item['repo_name'] == 'torvalds/linux'), None)

# Load languages data
languages_file_path = locals()['var_function-call-17748333109832134525']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

linux_lang = next((item for item in languages_data if item['repo_name'] == 'torvalds/linux'), None)

res = {
    "linux_commits": linux_commits,
    "linux_lang": linux_lang
}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-14089913042029323930': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-993125701442150257': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-17748333109832134525': 'file_storage/function-call-17748333109832134525.json', 'var_function-call-7018712310867347699': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react', 'tensorflow/tensorflow']}

exec(code, env_args)
