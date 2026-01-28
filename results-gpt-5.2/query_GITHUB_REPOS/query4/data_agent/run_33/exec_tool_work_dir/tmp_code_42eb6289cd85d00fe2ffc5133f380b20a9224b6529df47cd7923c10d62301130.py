code = """import json, re
import pandas as pd

commits = pd.DataFrame(var_call_SzMmPRBoyAMIwoMSaMcBAmWj)
commits['commit_count'] = commits['commit_count'].astype(int)

# Load languages (may be file path)
lang_data = var_call_T3s2q2B7kwyiypzrQ8a8zxrQ
if isinstance(lang_data, str):
    with open(lang_data, 'r', encoding='utf-8') as f:
        lang_rows = json.load(f)
else:
    lang_rows = lang_data
langs = pd.DataFrame(lang_rows)

# Parse main language as the one with max bytes
pat = re.compile(r"([A-Za-z0-9_+.#-]+) \((\d[\d,]*) bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    pairs = pat.findall(desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        val = int(b.replace(',', ''))
        if val > best_bytes:
            best_lang, best_bytes = lang, val
    return best_lang

langs['main_language'] = langs['language_description'].map(main_lang)

merged = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

# Order by commit_count desc and take top 5
out = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SzMmPRBoyAMIwoMSaMcBAmWj': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_T3s2q2B7kwyiypzrQ8a8zxrQ': 'file_storage/call_T3s2q2B7kwyiypzrQ8a8zxrQ.json'}

exec(code, env_args)
