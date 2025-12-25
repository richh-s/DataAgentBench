code = """import json

# Load the list of valid repos (Shell + Apache-2.0)
valid_repos_file = locals()['var_function-call-5954355455731196388']
with open(valid_repos_file, 'r') as f:
    valid_repos_data = json.load(f)

# Create a set for faster lookup
valid_repo_names = set(r['repo_name'] for r in valid_repos_data)

# Load the commit counts
commit_counts_data = locals()['var_function-call-12640646627459413047']
# commit_counts_data is a list of dicts like {'repo_name': '...', 'cnt': ...}

total_commits = 0
matched_repos = []

for entry in commit_counts_data:
    repo = entry['repo_name']
    count = int(entry['cnt']) # Ensure it's an int
    
    if repo in valid_repo_names:
        total_commits += count
        matched_repos.append(repo)

print("__RESULT__:")
print(json.dumps({"total_commits": total_commits, "matched_repos": matched_repos}))"""

env_args = {'var_function-call-13281482937171668161': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-13281482937171668522': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-9031384466391263031': [{'license': 'apache-2.0'}], 'var_function-call-5954355455731196388': 'file_storage/function-call-5954355455731196388.json', 'var_function-call-14229973942719456216': 114972, 'var_function-call-12640646627459413047': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'facebook/react', 'cnt': '104'}], 'var_function-call-1048989578087882440': [{'count_star()': '17976'}], 'var_function-call-5023268032205048179': [{'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'facebook/react'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}]}

exec(code, env_args)
