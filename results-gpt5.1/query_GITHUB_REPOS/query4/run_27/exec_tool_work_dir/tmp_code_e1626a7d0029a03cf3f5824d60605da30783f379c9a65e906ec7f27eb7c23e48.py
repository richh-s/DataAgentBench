code = """import json, pandas as pd

commits_df = pd.DataFrame(var_call_wHQ4HTlDXucxhKnyzIbsCV5G)

# load full languages data
import os, pandas as pd
with open(var_call_tbIt6mfGcFmHuMaIjPdqxUb2, 'r') as f:
    languages_data = json.load(f)
lang_df = pd.DataFrame(languages_data)

# Infer main language from description: take first 'X (n bytes)' occurrence
import re

def get_main_language(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r"([A-Za-z+#]+) \(\d+ bytes\)", desc)
    return m.group(1) if m else None

lang_df['main_language'] = lang_df['language_description'].apply(get_main_language)

# merge on repo_name, filter non-Python
merged = commits_df.merge(lang_df[['repo_name','main_language']], on='repo_name', how='left')
non_py = merged[merged['main_language'].str.lower() != 'python']

# sort by commit_count desc (ensure numeric) and take top 5
non_py['commit_count'] = non_py['commit_count'].astype(int)
result_names = non_py.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result_names)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_wHQ4HTlDXucxhKnyzIbsCV5G': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_tbIt6mfGcFmHuMaIjPdqxUb2': 'file_storage/call_tbIt6mfGcFmHuMaIjPdqxUb2.json'}

exec(code, env_args)
