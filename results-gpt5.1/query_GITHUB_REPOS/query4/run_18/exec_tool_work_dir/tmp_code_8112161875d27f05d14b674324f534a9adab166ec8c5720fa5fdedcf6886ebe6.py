code = """import json, pandas as pd

commits = pd.DataFrame(var_call_Z62A14kYUSFKj1PiGPsFJcjo)

# load full languages file
import pathlib
with open(var_call_6NAQNLgM47OwnuLyHyZT3jdJ, 'r') as f:
    languages = json.load(f)
langs = pd.DataFrame(languages)

# infer main language as the first language mentioned before the first '('
# language_description examples mention 'Ruby (22,438 bytes), Shell ...'
# We'll parse by taking tokens before first '('

def main_lang(desc: str):
    if not isinstance(desc, str):
        return None
    # take substring before first '(' then last word in that substring
    before = desc.split('(')[0]
    parts = before.strip().split()
    return parts[-1] if parts else None

langs['main_language'] = langs['language_description'].apply(main_lang)

# merge with commits on repo_name
merged = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')

# filter out Python main language
filtered = merged[merged['main_language'].str.lower() != 'python']

# sort by commit_count desc (commit_count is str currently)
filtered['commit_count'] = filtered['commit_count'].astype(int)
filtered = filtered.sort_values('commit_count', ascending=False)

result = filtered.head(5)['repo_name'].tolist()

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Z62A14kYUSFKj1PiGPsFJcjo': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_6NAQNLgM47OwnuLyHyZT3jdJ': 'file_storage/call_6NAQNLgM47OwnuLyHyZT3jdJ.json'}

exec(code, env_args)
