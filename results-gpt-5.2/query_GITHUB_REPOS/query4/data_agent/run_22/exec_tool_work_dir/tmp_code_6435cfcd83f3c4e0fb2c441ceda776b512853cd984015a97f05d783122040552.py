code = """import json, re
import pandas as pd

# load languages
path = var_call_C5XJkgC9ZDLUuCzAUun5wqOo
with open(path, 'r', encoding='utf-8') as f:
    langs = json.load(f)

df_lang = pd.DataFrame(langs)
df_commits = pd.DataFrame(var_call_hfYn9LqrGRUnvGYKc6ZxcLcn)

# parse main language as language with max bytes mentioned
pat = re.compile(r"([A-Za-z0-9_+#\-\. ]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if desc is None:
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best_lang = lang.strip()
    return best_lang

df_lang['main_language'] = df_lang['language_description'].map(main_lang)

# join with commit counts
# commit_count comes as string; cast
if 'commit_count' in df_commits.columns:
    df_commits['commit_count'] = pd.to_numeric(df_commits['commit_count'], errors='coerce')

merged = pd.merge(df_commits, df_lang[['repo_name','main_language']], on='repo_name', how='left')

# filter main language not Python
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

# top 5 by commit_count desc
out = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = '\n'.join(out['repo_name'].tolist())

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_C5XJkgC9ZDLUuCzAUun5wqOo': 'file_storage/call_C5XJkgC9ZDLUuCzAUun5wqOo.json', 'var_call_hfYn9LqrGRUnvGYKc6ZxcLcn': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
