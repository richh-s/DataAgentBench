code = """import json, pandas as pd
from pathlib import Path

commits_top = var_call_OAyPWarNOc5o9HVTq2KfJDlC
langs_path = Path(var_call_PGpw4wzVoT0DEsEHxoCk6wYV)
langs = json.loads(langs_path.read_text())

df_commits = pd.DataFrame(commits_top)
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

df_langs = pd.DataFrame(langs)

python_mask = df_langs['language_description'].str.contains('Python', case=False, na=False)
non_python_langs = df_langs[~python_mask]

merged = pd.merge(df_commits, non_python_langs, on='repo_name', how='inner')

merged_sorted = merged.sort_values('commit_count', ascending=False).head(5)

result = merged_sorted['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OAyPWarNOc5o9HVTq2KfJDlC': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_XCFj4WmdqC7rx2CuqDdr9DlA': ['languages', 'repos', 'licenses'], 'var_call_PGpw4wzVoT0DEsEHxoCk6wYV': 'file_storage/call_PGpw4wzVoT0DEsEHxoCk6wYV.json'}

exec(code, env_args)
