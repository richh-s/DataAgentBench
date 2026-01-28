code = """import json, re
import pandas as pd

commits = pd.DataFrame(var_call_sDZ6BIJQf2Kk7ojKMDoqr01M)
commits['commit_count'] = commits['commit_count'].astype(int)

# load languages (may be file path)
lang_data = var_call_xHE5GqjXNv9RB2ehXe8d40CX
if isinstance(lang_data, str) and lang_data.endswith('.json'):
    with open(lang_data, 'r', encoding='utf-8') as f:
        languages = json.load(f)
else:
    languages = lang_data

lang_df = pd.DataFrame(languages)

# extract main language by largest byte count
pat = re.compile(r"([A-Za-z0-9+#\-\. ]+?)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if desc is None:
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        b_int = int(b.replace(',', ''))
        if b_int > best_bytes:
            best_lang, best_bytes = lang.strip(), b_int
    return best_lang

lang_df['main_language'] = lang_df['language_description'].map(main_lang)

merged = commits.merge(lang_df[['repo_name','main_language']], on='repo_name', how='inner')
filtered = merged[merged['main_language'].fillna('') != 'Python']

top5 = filtered.sort_values('commit_count', ascending=False).head(5)
result = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_sDZ6BIJQf2Kk7ojKMDoqr01M': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_xHE5GqjXNv9RB2ehXe8d40CX': 'file_storage/call_xHE5GqjXNv9RB2ehXe8d40CX.json'}

exec(code, env_args)
