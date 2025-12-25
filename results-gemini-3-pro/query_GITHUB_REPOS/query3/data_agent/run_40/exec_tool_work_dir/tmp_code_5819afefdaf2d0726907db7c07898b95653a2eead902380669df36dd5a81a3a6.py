code = """import json

eligible_repos_file = locals()['var_function-call-4798822454506213376']
with open(eligible_repos_file, 'r') as f:
    eligible_repos = set(json.load(f))

commit_counts_data = locals()['var_function-call-5085005762312642924']

matching_repos = []
total = 0
for entry in commit_counts_data:
    if entry['repo_name'] in eligible_repos:
        matching_repos.append(entry['repo_name'])
        total += int(entry['cnt'])

print("__RESULT__:")
print(json.dumps({"matching_repos": matching_repos, "total": total}))"""

env_args = {'var_function-call-14340486422377598958': ['languages', 'repos', 'licenses'], 'var_function-call-10382311092339761028': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-2892584306306574223': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-7163643810791682287': 'file_storage/function-call-7163643810791682287.json', 'var_function-call-4798822454506213376': 'file_storage/function-call-4798822454506213376.json', 'var_function-call-10279647565570137680': 114972, 'var_function-call-5085005762312642924': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}], 'var_function-call-16045234870210927499': 'done', 'var_function-call-10310074430254351297': {'type': "<class 'list'>", 'length': 6}, 'var_function-call-15892018443893018677': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'Microsoft/vscode'}], 'var_function-call-10361935564838782939': 1077}

exec(code, env_args)
