code = """import json

with open(locals()['var_function-call-13484576814427699800'], 'r') as f:
    languages_data = json.load(f)

repo_languages = {item['repo_name']: item['language_description'] for item in languages_data}
commits_data = locals()['var_function-call-13484576814427699867']

raw_descs = {}
for c in commits_data:
    raw_descs[c['repo_name']] = repo_languages.get(c['repo_name'])

print("__RESULT__:")
print(json.dumps(raw_descs))"""

env_args = {'var_function-call-11742302900551546422': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11742302900551545127': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}], 'var_function-call-13484576814427699800': 'file_storage/function-call-13484576814427699800.json', 'var_function-call-13484576814427699867': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'facebook/react', 'commit_count': '178'}], 'var_function-call-3914277259782831792': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react', 'tensorflow/tensorflow'], 'var_function-call-5777633598743109769': {'torvalds/linux_desc': None}, 'var_function-call-8815141744651366927': [], 'var_function-call-10485262413673137620': [{'repo_name': 'torvalds/linux', 'watch_count': '5332'}], 'var_function-call-11417626852124346638': [{'repo': 'tensorflow/tensorflow', 'count': '156', 'main_lang': 'While most of the project is built in C++'}, {'repo': 'Microsoft/vscode', 'count': '190', 'main_lang': 'The majority of the code is in TypeScript'}, {'repo': 'apple/swift', 'count': '1051', 'main_lang': 'C++'}, {'repo': 'torvalds/linux', 'count': '16061', 'main_lang': None}, {'repo': 'twbs/bootstrap', 'count': '340', 'main_lang': 'JavaScript'}, {'repo': 'facebook/react', 'count': '178', 'main_lang': 'While most of the project is built in JavaScript'}]}

exec(code, env_args)
