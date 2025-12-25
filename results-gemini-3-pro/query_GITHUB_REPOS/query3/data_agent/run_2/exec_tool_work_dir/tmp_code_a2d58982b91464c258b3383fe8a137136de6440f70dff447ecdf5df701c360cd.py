code = """import json
import os

# Load the counts
# Check if it is a list or a file path
counts_data = locals()['var_function-call-16745568738797511383']
if isinstance(counts_data, str) and os.path.exists(counts_data):
    with open(counts_data, 'r') as f:
        repo_counts = json.load(f)
else:
    repo_counts = counts_data

# Load the valid repos list
valid_repos_path = locals()['var_function-call-16205692850786819155']
with open(valid_repos_path, 'r') as f:
    valid_repos_list = json.load(f)

# Convert list to set for O(1) lookup
valid_repos_set = set(valid_repos_list)

total_commits = 0
matched_repos = []

for entry in repo_counts:
    # entry is {"repo_name": "...", "cnt": "..."}
    # Note: cnt might be string or int depending on DB driver.
    r_name = entry['repo_name']
    cnt = int(entry['cnt'])
    
    if r_name in valid_repos_set:
        total_commits += cnt
        matched_repos.append(r_name)

print(f"Matched repos: {matched_repos}")
print(f"Total commits: {total_commits}")

print("__RESULT__:")
print(json.dumps(total_commits))"""

env_args = {'var_function-call-4123773394754128272': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-4123773394754129877': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-17526777643317543344': 'file_storage/function-call-17526777643317543344.json', 'var_function-call-16205692850786819155': 'file_storage/function-call-16205692850786819155.json', 'var_function-call-598181883990585523': 'file_storage/function-call-598181883990585523.json', 'var_function-call-13779345076968794009': 3021893, 'var_function-call-3678787294981550227': 'Done', 'var_function-call-4193700092434364678': {'count': 114972, 'first': 'jitsi/jipopro', 'avg_len': 22.281903419963122, 'str_len': 3021681}, 'var_function-call-9755489189922434271': 'file_storage/function-call-9755489189922434271.json', 'var_function-call-16745568738797511383': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}], 'var_function-call-184060528676464587': [{'total_commits': '17976', 'total_repos': '6'}]}

exec(code, env_args)
