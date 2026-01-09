code = """import json, re
import pandas as pd

commits = pd.DataFrame(var_call_M0DkwzrwWY0SsQcyPwL02yiY)
commits['commit_count'] = commits['commit_count'].astype(int)

# load languages full
path = var_call_Z4H4d2W5Q6vqLi4ufyPTp35M
with open(path, 'r', encoding='utf-8') as f:
    langs = json.load(f)
langs_df = pd.DataFrame(langs)

# parse main language by max bytes in description
pat = re.compile(r"([A-Za-z0-9_+.#-]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best_lang = lang
    return best_lang

langs_df['main_language'] = langs_df['language_description'].map(main_lang)

merged = commits.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[merged['main_language'].notna() & (merged['main_language'].str.lower() != 'python')]

top5 = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_M0DkwzrwWY0SsQcyPwL02yiY': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_Z4H4d2W5Q6vqLi4ufyPTp35M': 'file_storage/call_Z4H4d2W5Q6vqLi4ufyPTp35M.json'}

exec(code, env_args)
