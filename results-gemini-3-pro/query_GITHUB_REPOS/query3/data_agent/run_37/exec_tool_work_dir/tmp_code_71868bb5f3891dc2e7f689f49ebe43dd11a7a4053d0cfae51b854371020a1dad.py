code = """import json

# Load the target repositories (Shell + Apache-2.0)
target_repos_file = locals()['var_function-call-1212352130297387460']
with open(target_repos_file, 'r') as f:
    target_repos_data = json.load(f)
target_repos_set = set(item['repo_name'] for item in target_repos_data)

commit_counts_data = locals()['var_function-call-4176930137089753944']

matched_repos = []
filtered_commit_count = 0

for entry in commit_counts_data:
    repo = entry['repo_name']
    count = int(entry['commit_count'])
    if repo in target_repos_set:
        matched_repos.append(repo)
        filtered_commit_count += count

print(f"Matched Repos: {matched_repos}")
print("__RESULT__:")
print(filtered_commit_count)"""

env_args = {'var_function-call-14250136166159752164': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-14250136166159751413': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-1212352130297387460': 'file_storage/function-call-1212352130297387460.json', 'var_function-call-10944148881803535860': 114972, 'var_function-call-4176930137089753944': [{'repo_name': 'facebook/react', 'commit_count': '104'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '114'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '171'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '251'}, {'repo_name': 'torvalds/linux', 'commit_count': '13413'}, {'repo_name': 'apple/swift', 'commit_count': '963'}], 'var_function-call-17866080246014176532': [{'count_star()': '17976'}], 'var_function-call-11268121399493719062': [{'count(DISTINCT repo_name)': '6'}], 'var_function-call-14282501555189304878': 1077}

exec(code, env_args)
