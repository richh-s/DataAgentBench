code = """import json
import pandas as pd

langs = var_call_nYKJ5CgNuWchiNYqitWxpZJv
commits = var_call_4pn0d00m6RpwSXEGX2gdrU6c

if isinstance(langs, str) and langs.endswith('.json'):
    with open(langs, 'r') as f:
        langs = json.load(f)

langs_df = pd.DataFrame(langs)
commits_df = pd.DataFrame(commits)

merged = pd.merge(commits_df, langs_df, on='repo_name', how='inner')

merged['commit_count'] = merged['commit_count'].astype(int)

result_df = merged.sort_values('commit_count', ascending=False).head(5)

result = result_df['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nYKJ5CgNuWchiNYqitWxpZJv': 'file_storage/call_nYKJ5CgNuWchiNYqitWxpZJv.json', 'var_call_4pn0d00m6RpwSXEGX2gdrU6c': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}]}

exec(code, env_args)
