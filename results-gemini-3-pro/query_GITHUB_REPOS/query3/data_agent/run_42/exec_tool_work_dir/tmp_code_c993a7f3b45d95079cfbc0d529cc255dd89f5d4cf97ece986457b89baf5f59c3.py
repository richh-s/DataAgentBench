code = """import json

# Load repo_names (metadata list)
with open(locals()['var_function-call-4035135090983698954'], 'r') as f:
    repo_data = json.load(f)
target_repos = set(item['repo_name'] for item in repo_data)

# Load commit_repos (artifacts list)
with open(locals()['var_function-call-16940984546907389411'], 'r') as f:
    commit_data = json.load(f)

# Count matches
count = 0
for item in commit_data:
    if item['repo_name'] in target_repos:
        count += 1

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-14235957637636619780': ['languages', 'repos', 'licenses'], 'var_function-call-3478505751337707721': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11281467589420128098': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-4035135090983698954': 'file_storage/function-call-4035135090983698954.json', 'var_function-call-9797831017971668472': 114972, 'var_function-call-7341050634147536112': [{'count_star()': '15016'}], 'var_function-call-15598791954333738087': [{'count_star()': '17976'}], 'var_function-call-16940984546907389411': 'file_storage/function-call-16940984546907389411.json'}

exec(code, env_args)
