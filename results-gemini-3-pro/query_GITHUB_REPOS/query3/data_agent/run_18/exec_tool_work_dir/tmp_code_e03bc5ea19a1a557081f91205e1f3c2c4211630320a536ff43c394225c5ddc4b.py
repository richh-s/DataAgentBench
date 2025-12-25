code = """import json

# Load the list of valid repos (Shell + Apache-2.0)
file_path = locals()['var_function-call-14530052145036912762']
with open(file_path, 'r') as f:
    valid_repos_data = json.load(f)
valid_repo_names = set(r['repo_name'] for r in valid_repos_data)

# The result from the commits query
commits_counts = [
    {"repo_name": "facebook/react", "cnt": 104},
    {"repo_name": "tensorflow/tensorflow", "cnt": 114},
    {"repo_name": "twbs/bootstrap", "cnt": 251},
    {"repo_name": "Microsoft/vscode", "cnt": 171},
    {"repo_name": "apple/swift", "cnt": 963},
    {"repo_name": "torvalds/linux", "cnt": 13413}
]

total_commits = 0
matched_repos = []

for item in commits_counts:
    if item['repo_name'] in valid_repo_names:
        total_commits += int(item['cnt'])
        matched_repos.append(item['repo_name'])

print(f"Matched Repos: {matched_repos}")
print(f"Total Commits: {total_commits}")
print("__RESULT__:")
print(json.dumps(total_commits))"""

env_args = {'var_function-call-4210186772458490092': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-4210186772458489379': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-14530052145036912762': 'file_storage/function-call-14530052145036912762.json', 'var_function-call-18424538311467733003': 114972, 'var_function-call-16479859295058736099': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}], 'var_function-call-10499853064878351601': [{'count(DISTINCT repo_name)': '6'}]}

exec(code, env_args)
