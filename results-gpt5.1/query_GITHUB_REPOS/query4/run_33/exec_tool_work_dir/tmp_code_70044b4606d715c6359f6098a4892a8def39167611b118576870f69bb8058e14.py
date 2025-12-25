code = """import json
import pandas as pd

langs = var_call_dJMrcMQE1LEeYJHluyMtizrN
commits = var_call_bqDhRef7FlB2BF21LUQbMK9L

# langs may be a file path if large
if isinstance(langs, str):
    with open(langs, 'r') as f:
        langs = json.load(f)

langs_df = pd.DataFrame(langs)
non_py_repos = set(langs_df['repo_name'].tolist())

commits_df = pd.DataFrame(commits)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

filtered = commits_df[commits_df['repo_name'].isin(non_py_repos)]
filtered = filtered.sort_values('commit_count', ascending=False).head(5)

result = filtered['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dJMrcMQE1LEeYJHluyMtizrN': 'file_storage/call_dJMrcMQE1LEeYJHluyMtizrN.json', 'var_call_bqDhRef7FlB2BF21LUQbMK9L': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
