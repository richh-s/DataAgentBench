code = """import json, re
import pandas as pd

# load languages full result (may be a file path)
lang_src = var_call_BuA4drlvcqDGakNJEMJC32SQ
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        languages = json.load(f)
else:
    languages = lang_src

commits = var_call_XSf0jheQdERIuYXjNevQl9hg

df_lang = pd.DataFrame(languages)
df_comm = pd.DataFrame(commits)

# parse main language as the one with max bytes in language_description
pat = re.compile(r'([A-Za-z0-9+#\-\. ]+)\s*\((\d[\d,]*)\s*bytes\)')

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        b_int = int(b.replace(',', ''))
        if b_int > best_bytes:
            best_bytes = b_int
            best_lang = lang.strip()
    return best_lang

df_lang['main_language'] = df_lang['language_description'].map(main_lang)

# Join commits with language
merged = pd.merge(df_comm, df_lang[['repo_name','main_language']], on='repo_name', how='left')
merged['commit_count'] = merged['commit_count'].astype(int)

# filter main_language != Python
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

# top 5 by commits
out = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BuA4drlvcqDGakNJEMJC32SQ': 'file_storage/call_BuA4drlvcqDGakNJEMJC32SQ.json', 'var_call_XSf0jheQdERIuYXjNevQl9hg': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
