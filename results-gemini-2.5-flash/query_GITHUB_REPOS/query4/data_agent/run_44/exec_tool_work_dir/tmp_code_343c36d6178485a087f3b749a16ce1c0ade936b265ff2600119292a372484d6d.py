code = """import pandas as pd
import json

non_python_repos_path = locals()['var_function-call-2792665969835822291']
with open(non_python_repos_path, 'r') as f:
    non_python_repos_data = json.load(f)

non_python_repos_df = pd.DataFrame(non_python_repos_data)
non_python_repo_names = non_python_repos_df['repo_name'].tolist()


commit_counts_data = locals()['var_function-call-9167090119458941622']
commit_counts_df = pd.DataFrame(commit_counts_data)

filtered_repos = commit_counts_df[commit_counts_df['repo_name'].isin(non_python_repo_names)]

sorted_repos = filtered_repos.sort_values(by='commit_count', ascending=False)

top_5_repos = sorted_repos.head(5)

result = top_5_repos['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-2792665969835822291': 'file_storage/function-call-2792665969835822291.json', 'var_function-call-16590410597530550681': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter'], 'var_function-call-9167090119458941622': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
