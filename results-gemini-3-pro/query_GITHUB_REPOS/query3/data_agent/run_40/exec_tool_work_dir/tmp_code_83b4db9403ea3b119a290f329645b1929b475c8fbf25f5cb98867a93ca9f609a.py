code = """import json

# eligible repos file
eligible_repos_file = locals()['var_function-call-4798822454506213376']
with open(eligible_repos_file, 'r') as f:
    eligible_repos_data = json.load(f)
    # create a set for faster lookup
    eligible_repos = set(r['repo_name'] for r in eligible_repos_data)

# commit counts from artifacts_database
commit_counts_data = locals()['var_function-call-5085005762312642924']
# commit_counts_data is a list of dicts: [{'repo_name': '...', 'cnt': '...'}]

total_commits = 0
matching_repos = []

for entry in commit_counts_data:
    repo = entry['repo_name']
    cnt = int(entry['cnt'])
    
    if repo in eligible_repos:
        total_commits += cnt
        matching_repos.append(repo)

print(f"Eligible Repos Count: {len(eligible_repos)}")
print(f"Artifact Repos Count: {len(commit_counts_data)}")
print(f"Matching Repos: {matching_repos}")
print(f"Total Commits: {total_commits}")

print("__RESULT__:")
print(json.dumps(total_commits))"""

env_args = {'var_function-call-14340486422377598958': ['languages', 'repos', 'licenses'], 'var_function-call-10382311092339761028': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-2892584306306574223': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-7163643810791682287': 'file_storage/function-call-7163643810791682287.json', 'var_function-call-4798822454506213376': 'file_storage/function-call-4798822454506213376.json', 'var_function-call-10279647565570137680': 114972, 'var_function-call-5085005762312642924': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}], 'var_function-call-16045234870210927499': 'done', 'var_function-call-10310074430254351297': {'type': "<class 'list'>", 'length': 6}, 'var_function-call-15892018443893018677': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'Microsoft/vscode'}]}

exec(code, env_args)
