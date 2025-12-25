code = """import json

# Load valid repos
repo_file_path = locals()['var_function-call-6355967325981832149']
with open(repo_file_path, 'r') as f:
    valid_repos_list = json.load(f)
valid_repos = set(r['repo_name'] for r in valid_repos_list)

# Load commit counts
# The previous result was printed directly, so it's a list in the variable
commit_counts = locals()['var_function-call-734777088940472174']

# Sum counts for valid repos
total_commits = 0
matched_repos_count = 0

for record in commit_counts:
    repo = record['repo_name']
    count = int(record['cnt']) # Ensure it's int
    if repo in valid_repos:
        total_commits += count
        matched_repos_count += 1

print("__RESULT__:")
print(json.dumps({"total_commits": total_commits, "matched_repos": matched_repos_count}))"""

env_args = {'var_function-call-9828543375877277366': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-9828543375877275901': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-6355967325981832149': 'file_storage/function-call-6355967325981832149.json', 'var_function-call-14303692993939420586': 114972, 'var_function-call-734777088940472174': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'apple/swift', 'cnt': '963'}], 'var_function-call-13068245804339342754': [{'count_star()': '17976'}]}

exec(code, env_args)
