code = """import json
import pandas as pd

non_python_repos = json.load(open(locals()['var_function-call-13759270199249380712'], 'r'))
commit_counts = locals()['var_function-call-13666020597353028308']

df_commits = pd.DataFrame(commit_counts)
df_commits["commit_count"] = df_commits["commit_count"].astype(int)

filtered_df = df_commits[df_commits["repo_name"].isin(non_python_repos)]

sorted_df = filtered_df.sort_values(by="commit_count", ascending=False)

top_5_repos = sorted_df.head(5)["repo_name"].tolist()

print("__RESULT__:")
print(json.dumps(top_5_repos))"""

env_args = {'var_function-call-13215391144481791493': 'file_storage/function-call-13215391144481791493.json', 'var_function-call-13759270199249380712': 'file_storage/function-call-13759270199249380712.json', 'var_function-call-13666020597353028308': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}]}

exec(code, env_args)
