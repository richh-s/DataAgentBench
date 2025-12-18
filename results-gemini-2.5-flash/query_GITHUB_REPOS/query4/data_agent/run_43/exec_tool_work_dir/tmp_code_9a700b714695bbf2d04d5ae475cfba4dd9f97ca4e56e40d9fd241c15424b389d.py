code = """import json
import pandas as pd

non_python_repos = json.loads(open(locals()['var_function-call-6572228548991105208'], 'r').read())
commit_counts = locals()['var_function-call-4615113393884012113']

df_commits = pd.DataFrame(commit_counts)
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

df_non_python_commits = df_commits[df_commits['repo_name'].isin(non_python_repos)]

top_five_repos = df_non_python_commits.sort_values(by='commit_count', ascending=False).head(5)

print('__RESULT__:')
print(json.dumps(top_five_repos['repo_name'].tolist()))"""

env_args = {'var_function-call-15701927023968665033': 'file_storage/function-call-15701927023968665033.json', 'var_function-call-6572228548991105208': 'file_storage/function-call-6572228548991105208.json', 'var_function-call-4615113393884012113': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
