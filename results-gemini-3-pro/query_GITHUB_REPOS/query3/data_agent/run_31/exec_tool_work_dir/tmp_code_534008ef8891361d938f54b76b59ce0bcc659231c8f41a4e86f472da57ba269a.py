code = """import json

# Load the list of valid repos (Shell + Apache-2.0)
with open(locals()['var_function-call-17085759733731587748'], 'r') as f:
    valid_repos_data = json.load(f)

valid_repo_names = set([r['repo_name'] for r in valid_repos_data])

# Load the commit counts
commit_counts_data = locals()['var_function-call-12632532552433494395']
# It is a list of dicts: [{"repo_name": "...", "commit_count": "..."}]

total_commits = 0
matched_repos = []

for entry in commit_counts_data:
    r_name = entry['repo_name']
    count = int(entry['commit_count'])
    
    if r_name in valid_repo_names:
        total_commits += count
        matched_repos.append(r_name)

print("__RESULT__:")
print(json.dumps({"total_commits": total_commits, "matched_repos": matched_repos}))"""

env_args = {'var_function-call-13922844926968821357': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-13922844926968820806': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-17085759733731587748': 'file_storage/function-call-17085759733731587748.json', 'var_function-call-4166200339729823572': 114972, 'var_function-call-12632532552433494395': [{'repo_name': 'facebook/react', 'commit_count': '104'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '114'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '251'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '171'}, {'repo_name': 'apple/swift', 'commit_count': '963'}, {'repo_name': 'torvalds/linux', 'commit_count': '13413'}], 'var_function-call-2161426638598006439': [{'count_star()': '17976'}], 'var_function-call-2161426638598007698': 'file_storage/function-call-2161426638598007698.json'}

exec(code, env_args)
