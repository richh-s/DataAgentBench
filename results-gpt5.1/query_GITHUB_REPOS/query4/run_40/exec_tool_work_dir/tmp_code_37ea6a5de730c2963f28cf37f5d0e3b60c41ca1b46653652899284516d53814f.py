code = """import json, pandas as pd

commits_top = pd.DataFrame(var_call_ZdN3P88yBxy1mk8X0zTamOtC)

with open(var_call_OeLfDMjPwJvYFWiXALrIL7mc, 'r') as f:
    langs = json.load(f)
langs_df = pd.DataFrame(langs)

langs_df['main_language'] = langs_df['language_description'].str.extract(r"mainly written in ([A-Za-z\+#]+)|majority of the code is in ([A-Za-z\+#]+)|built in ([A-Za-z\+#]+)|includes: ([A-Za-z\+#]+)", expand=True).bfill(axis=1).iloc[:,0]

merged = commits_top.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[(merged['main_language'].str.lower() != 'python')]
result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ZdN3P88yBxy1mk8X0zTamOtC': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_OeLfDMjPwJvYFWiXALrIL7mc': 'file_storage/call_OeLfDMjPwJvYFWiXALrIL7mc.json'}

exec(code, env_args)
