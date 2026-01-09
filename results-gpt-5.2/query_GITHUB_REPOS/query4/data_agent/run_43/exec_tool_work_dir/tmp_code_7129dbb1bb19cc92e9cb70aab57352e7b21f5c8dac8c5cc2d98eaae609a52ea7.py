code = """import json, re
import pandas as pd

commits = pd.DataFrame(var_call_sDZ6BIJQf2Kk7ojKMDoqr01M)
commits['commit_count'] = commits['commit_count'].astype(int)

# Load language data
lang_data = var_call_xHE5GqjXNv9RB2ehXe8d40CX
if isinstance(lang_data, str) and lang_data.endswith('.json'):
    with open(lang_data, 'r', encoding='utf-8') as f:
        all_lang = json.load(f)
else:
    all_lang = lang_data

# Reduce to repos present in commits to avoid heavy processing
commit_repos = set(commits['repo_name'].tolist())
langs = [r for r in all_lang if r.get('repo_name') in commit_repos]
lang_df = pd.DataFrame(langs)

pat = re.compile(r"([A-Za-z0-9+#\-\. ]+?)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if not desc:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pat.findall(desc):
        bi = int(b.replace(',', ''))
        if bi > best_bytes:
            best_lang, best_bytes = lang.strip(), bi
    return best_lang

lang_df['main_language'] = [main_lang(d) for d in lang_df['language_description'].tolist()]

merged = commits.merge(lang_df[['repo_name','main_language']], on='repo_name', how='inner')
filtered = merged[merged['main_language'] != 'Python']

top5 = filtered.sort_values('commit_count', ascending=False).head(5)

print('__RESULT__:')
print(json.dumps(top5['repo_name'].tolist()))"""

env_args = {'var_call_sDZ6BIJQf2Kk7ojKMDoqr01M': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_xHE5GqjXNv9RB2ehXe8d40CX': 'file_storage/call_xHE5GqjXNv9RB2ehXe8d40CX.json'}

exec(code, env_args)
