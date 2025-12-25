code = """import json

# Load the large list of repos from the file
valid_repos_path = locals()['var_function-call-6490452699147991390']
with open(valid_repos_path, 'r') as f:
    valid_repos_list = json.load(f)

# Convert to a set for faster lookup
valid_repos = set(r['repo_name'] for r in valid_repos_list)

# Load the commit counts (this is a direct list variable)
commit_counts = locals()['var_function-call-18407094983301795778']

total_commits = 0
matched_repos = []

for entry in commit_counts:
    repo = entry['repo_name']
    cnt = int(entry['cnt'])
    if repo in valid_repos:
        total_commits += cnt
        matched_repos.append(repo)

print("__RESULT__:")
print(json.dumps({"total_commits": total_commits, "matched_repos": matched_repos}))"""

env_args = {'var_function-call-6490452699147991390': 'file_storage/function-call-6490452699147991390.json', 'var_function-call-15620731107733032422': 114972, 'var_function-call-18407094983301795778': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}], 'var_function-call-17336453436231985061': ['commits', 'contents', 'files'], 'var_function-call-15800272206324792857': [{'count(DISTINCT repo_name)': '6'}]}

exec(code, env_args)
