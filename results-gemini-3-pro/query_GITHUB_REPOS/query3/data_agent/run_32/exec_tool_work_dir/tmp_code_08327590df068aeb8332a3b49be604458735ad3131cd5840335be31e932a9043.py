code = """import json

# Load target repos (Shell + Apache-2.0)
with open(locals()['var_function-call-13909328388397089403'], 'r') as f:
    target_repos_list = json.load(f)

target_repo_names = set(r['repo_name'] for r in target_repos_list)

# Load commit counts
# This is a list of dicts, not a file path
commit_counts = locals()['var_function-call-3443328016762070568']

total_commits = 0
matched_repos = []

for entry in commit_counts:
    r_name = entry['repo_name']
    count = int(entry['cnt']) # Ensure it's int
    if r_name in target_repo_names:
        total_commits += count
        matched_repos.append(r_name)

print(f"Matched repos: {matched_repos}")
print(f"Total commits: {total_commits}")

print("__RESULT__:")
print(json.dumps(total_commits))"""

env_args = {'var_function-call-13909328388397089403': 'file_storage/function-call-13909328388397089403.json', 'var_function-call-14961582393071831973': 'file_storage/function-call-14961582393071831973.json', 'var_function-call-7912600663322304728': 'file_storage/function-call-7912600663322304728.json', 'var_function-call-3443328016762070568': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}]}

exec(code, env_args)
