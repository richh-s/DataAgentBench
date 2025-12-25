code = """import json

# Load the list of valid repos (Shell + Apache-2.0)
repo_file_path = locals()['var_function-call-15944842631924152285']
with open(repo_file_path, 'r') as f:
    target_repos_list = json.load(f)

# Create a set for faster lookup
target_repos = set(r['repo_name'] for r in target_repos_list)

# Load the commit counts from the query result
commit_counts_data = locals()['var_function-call-4519857414249323683']
# commit_counts_data is a list of dicts like [{'repo_name': '...', 'cnt': '...'}]

total_commits = 0
matched_repos = []

for entry in commit_counts_data:
    r_name = entry['repo_name']
    count = int(entry['cnt'])
    
    if r_name in target_repos:
        total_commits += count
        matched_repos.append(r_name)

print(f"Matched repos: {matched_repos}")
print("__RESULT__:")
print(total_commits)"""

env_args = {'var_function-call-14249347328310499430': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-14249347328310499441': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-15944842631924152285': 'file_storage/function-call-15944842631924152285.json', 'var_function-call-17540613410460020872': 114972, 'var_function-call-4519857414249323683': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}], 'var_function-call-13154877753547812944': [{'total_rows': '17976', 'distinct_repos': '6'}]}

exec(code, env_args)
