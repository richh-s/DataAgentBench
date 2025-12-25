code = """import json
import pandas as pd

non_python_repos_json = locals()['var_function-call-10930683387778801682']
commit_counts_json = locals()['var_function-call-17435252314679724535']

with open(non_python_repos_json, 'r') as f:
    non_python_repos = json.load(f)

commit_counts = commit_counts_json

df_non_python = pd.DataFrame(non_python_repos)
df_commits = pd.DataFrame(commit_counts)

df_commits['commit_count'] = df_commits['commit_count'].astype(int)

merged_df = pd.merge(df_non_python, df_commits, on='repo_name', how='inner')

result_df = merged_df.sort_values(by='commit_count', ascending=False).head(5)

final_repo_names = result_df['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(final_repo_names))"""

env_args = {'var_function-call-9475326180653849631': 'file_storage/function-call-9475326180653849631.json', 'var_function-call-10930683387778801682': 'file_storage/function-call-10930683387778801682.json', 'var_function-call-17435252314679724535': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}]}

exec(code, env_args)
