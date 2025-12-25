code = """import json

commits_data = locals()['var_function-call-993125701442150257']
# Sort
commits_sorted = sorted(commits_data, key=lambda x: int(x['commit_count']), reverse=True)
top_10 = commits_sorted[:10]

# Load languages to check existence
languages_file_path = locals()['var_function-call-17748333109832134525']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)
    
lang_repos = set(item['repo_name'] for item in languages_data)

result = []
for item in top_10:
    has_lang = item['repo_name'] in lang_repos
    item['has_lang'] = has_lang
    result.append(item)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14089913042029323930': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-993125701442150257': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-17748333109832134525': 'file_storage/function-call-17748333109832134525.json', 'var_function-call-7018712310867347699': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react', 'tensorflow/tensorflow'], 'var_function-call-13277353696404990849': {'linux_commits': {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, 'linux_lang': None}}

exec(code, env_args)
