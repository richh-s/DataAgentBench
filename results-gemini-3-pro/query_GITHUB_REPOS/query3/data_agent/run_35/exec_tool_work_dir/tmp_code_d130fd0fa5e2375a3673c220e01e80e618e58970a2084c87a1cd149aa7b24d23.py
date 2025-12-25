code = """import json

# Load the list of target repos (Shell + Apache-2.0)
repo_list_path = locals()['var_function-call-17329779136183549997']
with open(repo_list_path, 'r') as f:
    target_repos_data = json.load(f)

# Extract repo names into a set for fast lookup
target_repos = set(item['repo_name'] for item in target_repos_data)

# Load the commit counts
commit_counts_data = locals()['var_function-call-9867576631341269237']
# commit_counts_data is a list of dicts like [{"repo_name": "...", "cnt": "..."}]

total_commits = 0
matching_repos_count = 0

for item in commit_counts_data:
    r_name = item['repo_name']
    count = int(item['cnt'])
    
    if r_name in target_repos:
        total_commits += count
        matching_repos_count += 1

result = {
    "total_commits": total_commits,
    "matching_repos_count": matching_repos_count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3684319644010918398': ['languages', 'repos', 'licenses'], 'var_function-call-7791759768468631723': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-7791759768468632870': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-13600441682523570255': [{'license': 'apache-2.0'}], 'var_function-call-17329779136183549997': 'file_storage/function-call-17329779136183549997.json', 'var_function-call-14647605362113562932': 114972, 'var_function-call-9867576631341269237': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}], 'var_function-call-5506385497158210977': ['commits', 'contents', 'files'], 'var_function-call-4194248624772242420': [{'count_star()': '17976'}]}

exec(code, env_args)
