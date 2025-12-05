code = """import json, re, pandas as pd

# languages large result path
languages_path = var_call_OB6z8tyDQP8SzisyAig7SeLa
with open(languages_path, 'r') as f:
    languages_data = json.load(f)

langs_df = pd.DataFrame(languages_data)

# function to extract main language
pattern = re.compile(r"(mainly written in|majority of the code is in|most of the project is built in|codebase includes:|The primary language is) ([A-Za-z+#]+)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    if m:
        return m.group(2)
    return None

langs_df['main_language'] = langs_df['language_description'].apply(main_lang)

commits_df = pd.DataFrame(var_call_50oio0d5H3ENWvxrvsEGSX4G)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

merged = commits_df.merge(langs_df[['repo_name', 'main_language']], on='repo_name', how='left')

filtered = merged[merged['main_language'].str.lower() != 'python']

result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OB6z8tyDQP8SzisyAig7SeLa': 'file_storage/call_OB6z8tyDQP8SzisyAig7SeLa.json', 'var_call_50oio0d5H3ENWvxrvsEGSX4G': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
