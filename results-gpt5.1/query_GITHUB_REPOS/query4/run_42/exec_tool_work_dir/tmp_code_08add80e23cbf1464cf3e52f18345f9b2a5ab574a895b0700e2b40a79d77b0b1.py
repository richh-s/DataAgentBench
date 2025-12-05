code = """import json, re
import pandas as pd

langs_path = var_call_zNFiGjzymO6GCUWnUUVV4JWX
with open(langs_path, 'r') as f:
    languages = json.load(f)

langs_df = pd.DataFrame(languages)

# Determine main language from language_description by taking the first "Language (N bytes)" entry
pattern = re.compile(r"([A-Za-z+#]+) \((\d+,?\d*) bytes\)")

def main_lang(desc):
    m = pattern.search(desc or '')
    return m.group(1) if m else None

langs_df['main_language'] = langs_df['language_description'].apply(main_lang)

commits_df = pd.DataFrame(var_call_wgd4T4sdTyqDOUKuh7HXQrRD)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')

# Filter out Python main language
non_py = merged[merged['main_language'].str.lower() != 'python']

# Sort by commit_count desc and take top 5
top5 = non_py.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_zNFiGjzymO6GCUWnUUVV4JWX': 'file_storage/call_zNFiGjzymO6GCUWnUUVV4JWX.json', 'var_call_wgd4T4sdTyqDOUKuh7HXQrRD': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
