code = """import json

# Load metadata repo list
path_metadata = locals()['var_function-call-11464923006534604886']
with open(path_metadata, 'r') as f:
    meta_repos = json.load(f)

valid_repos = set(r['repo_name'] for r in meta_repos)

# Load artifacts commit repo list
path_commits = locals()['var_function-call-3685936756422862804']
with open(path_commits, 'r') as f:
    commit_repos = json.load(f)

# Count matching commits
count = 0
for entry in commit_repos:
    if entry['repo_name'] in valid_repos:
        count += 1

print(f"Matching commits: {count}")
print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-12604790790188677838': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-12604790790188675383': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-11464923006534604886': 'file_storage/function-call-11464923006534604886.json', 'var_function-call-16730583594283689202': 114972, 'var_function-call-7422575115173066213': [{'count_star()': '15016'}], 'var_function-call-6993118478984686210': [{'count_star()': '17976'}], 'var_function-call-3685936756422862804': 'file_storage/function-call-3685936756422862804.json'}

exec(code, env_args)
