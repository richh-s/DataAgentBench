code = """import json, pandas as pd

commits_df = pd.DataFrame(var_call_T5OdqwnbwAwAub2n9fUwUIW7)

with open(var_call_g37hxpc4C8uE9DfgYMUS33Vz, 'r') as f:
    languages_data = json.load(f)

languages_df = pd.DataFrame(languages_data)

merged = commits_df.merge(languages_df, on='repo_name', how='left')

mask = ~merged['language_description'].str.contains('Python', case=False, na=False)
filtered = merged[mask]

result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_T5OdqwnbwAwAub2n9fUwUIW7': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_g37hxpc4C8uE9DfgYMUS33Vz': 'file_storage/call_g37hxpc4C8uE9DfgYMUS33Vz.json'}

exec(code, env_args)
