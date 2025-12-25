code = """import json
import pandas as pd

non_python_repos = json.load(open(locals()['var_function-call-7191682063390418889']))
commit_counts_data = locals()['var_function-call-14369657370896645146']
df_commits = pd.DataFrame(commit_counts_data)
df_commits['commit_count'] = pd.to_numeric(df_commits['commit_count'])

df_filtered_commits = df_commits[df_commits['repo_name'].isin(non_python_repos)]
top_5_repos = df_filtered_commits.sort_values(by='commit_count', ascending=False).head(5)

print("__RESULT__:")
print(json.dumps(top_5_repos['repo_name'].tolist()))"""

env_args = {'var_function-call-4786600211105115112': [{'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-11167423624507883408': 'file_storage/function-call-11167423624507883408.json', 'var_function-call-7191682063390418889': 'file_storage/function-call-7191682063390418889.json', 'var_function-call-14369657370896645146': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
