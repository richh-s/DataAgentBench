code = """import json, pandas as pd

commits_df = pd.DataFrame(var_call_SRE8sKqvGhhbgTaLOtqve2Ww)

with open(var_call_sb4JpmDYhW6FGUD0wOAxVPJy, 'r') as f:
    languages_data = json.load(f)
languages_df = pd.DataFrame(languages_data)

# infer main language as the first language mentioned before the first '('
# or by parsing patterns like 'mainly written in X' / 'majority of the code is in X'

def get_main_language(desc: str):
    if desc is None:
        return None
    lower = desc.lower()
    for key_phrase in ["mainly written in ", "majority of the code is in ", "while most of the project is built in ", "the codebase includes:", "this repository is ", "the codebase is primarily in "]:
        if key_phrase in lower:
            part = desc[lower.index(key_phrase) + len(key_phrase):]
            lang = part.split('(')[0].split(',')[0].split('.')[0].strip()
            return lang
    # fallback: first token before space and '('
    return desc.split('(')[0].split()[0].strip()

languages_df['main_language'] = languages_df['language_description'].apply(get_main_language)

# merge with commits on repo_name
merged = pd.merge(commits_df, languages_df[['repo_name', 'main_language']], on='repo_name', how='left')

# filter out Python main language (case-insensitive)
non_python = merged[merged['main_language'].str.lower() != 'python']

# order by commit_count desc (need numeric)
non_python['commit_count'] = non_python['commit_count'].astype(int)
non_python_sorted = non_python.sort_values('commit_count', ascending=False)

# pick top 5 repo_names
top5 = non_python_sorted.head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_SRE8sKqvGhhbgTaLOtqve2Ww': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_sb4JpmDYhW6FGUD0wOAxVPJy': 'file_storage/call_sb4JpmDYhW6FGUD0wOAxVPJy.json'}

exec(code, env_args)
