code = """import json

# Load valid repos (Shell + Apache-2.0)
path_repos = locals()['var_function-call-14528612285472370295']
with open(path_repos, 'r') as f:
    valid_repos_list = json.load(f)

# Create a set for faster lookup
valid_repos_set = set(item['repo_name'] for item in valid_repos_list)

# Load commit counts
commit_counts = locals()['var_function-call-6173420733157389623']
# commit_counts is a list of dicts: [{'repo_name': '...', 'cnt': ...}, ...]

total_commits = 0
matched_repos = []

for entry in commit_counts:
    r_name = entry['repo_name']
    count = int(entry['cnt']) # Ensure int
    
    if r_name in valid_repos_set:
        total_commits += count
        matched_repos.append(r_name)

print("__RESULT__:")
print(json.dumps({"total_commits": total_commits, "matched_repos": matched_repos}))"""

env_args = {'var_function-call-14516034867321177332': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-14516034867321176507': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-14528612285472370295': 'file_storage/function-call-14528612285472370295.json', 'var_function-call-15052329786741856997': 114972, 'var_function-call-6173420733157389623': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}], 'var_function-call-6586900986359374533': [{'count_star()': '17976'}], 'var_function-call-9110981939337221533': [{'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'facebook/react'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'apple/swift'}]}

exec(code, env_args)
