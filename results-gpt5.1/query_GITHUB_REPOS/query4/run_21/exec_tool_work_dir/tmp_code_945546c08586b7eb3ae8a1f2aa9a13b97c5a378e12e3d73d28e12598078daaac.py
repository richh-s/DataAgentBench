code = """import json, pandas as pd

# commits with counts
commits = var_call_Cu1B7pb1tEfru9lfPoCrITwp
commits_df = pd.DataFrame(commits)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# non-Python main languages
path = var_call_Z6TFmWO94J5O1ZdXZIqwJqkV
with open(path, 'r') as f:
    non_python = json.load(f)
non_df = pd.DataFrame(non_python)

# keep only repos where main_language is not null and not Python (already filtered)
non_df = non_df[non_df['main_language'].notna()]

merged = commits_df.merge(non_df, left_on='repo_name', right_on='repo_name', how='inner')

# order by commit_count desc and take top 5
top5 = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_Cu1B7pb1tEfru9lfPoCrITwp': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_iHxTyeiUeQeID2U4JhcjQYnf': ['languages', 'repos', 'licenses'], 'var_call_wmAYh5PqEGXezR0HUTRV8Nnd': 'file_storage/call_wmAYh5PqEGXezR0HUTRV8Nnd.json', 'var_call_Z6TFmWO94J5O1ZdXZIqwJqkV': 'file_storage/call_Z6TFmWO94J5O1ZdXZIqwJqkV.json'}

exec(code, env_args)
