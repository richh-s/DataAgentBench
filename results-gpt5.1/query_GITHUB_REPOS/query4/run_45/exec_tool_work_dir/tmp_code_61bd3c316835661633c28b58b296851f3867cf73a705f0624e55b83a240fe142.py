code = """import json, pandas as pd

commits_df = pd.DataFrame(var_call_SC95swM5Bg8jqqGTSUkSGOz3)

path = var_call_yTS1FK2jvpsd6nhCAVgumPqa
with open(path, 'r') as f:
    languages = json.load(f)
lang_df = pd.DataFrame(languages)

lang_df['main_lang'] = lang_df['language_description'].str.extract(r"mainly written in ([^(,]+)|majority of the code is in ([^(,]+)|built in ([^(,]+)|includes: ([^(,]+)")[0]
lang_df['main_lang'] = lang_df['main_lang'].str.strip()

merged = commits_df.merge(lang_df[['repo_name','main_lang']], on='repo_name', how='left')

filtered = merged[merged['main_lang'].str.lower() != 'python']

top5 = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_SC95swM5Bg8jqqGTSUkSGOz3': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_yTS1FK2jvpsd6nhCAVgumPqa': 'file_storage/call_yTS1FK2jvpsd6nhCAVgumPqa.json'}

exec(code, env_args)
