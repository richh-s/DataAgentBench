code = """import pandas as pd
import json

non_python_repos = json.loads(locals()['var_function-call-9574990026442089051'])
commit_counts_data = locals()['var_function-call-10439745556900294206']

df_commits = pd.DataFrame(commit_counts_data)
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

df_filtered_commits = df_commits[df_commits['repo_name'].isin(non_python_repos)]
sorted_repos = df_filtered_commits.sort_values(by='commit_count', ascending=False)
top_five_repos = sorted_repos.head(5)['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(top_five_repos))"""

env_args = {'var_function-call-17345825887054219745': 'file_storage/function-call-17345825887054219745.json', 'var_function-call-9574990026442089051': 'file_storage/function-call-9574990026442089051.json', 'var_function-call-10439745556900294206': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
