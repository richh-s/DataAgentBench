code = """import json, re
import pandas as pd

# Load languages (may be large)
lang_src = var_call_Ytkprb6KSdpUYX6YWK1GSbmE
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = lang_src

commits = var_call_nxAM8SpJ0l1Z7QYigvL1CRCw

lang_df = pd.DataFrame(langs)
comm_df = pd.DataFrame(commits)

# Parse main language from language_description by extracting (Language (bytes)) pairs
pattern = re.compile(r'([A-Za-z0-9+.#-]+)\s*\(([-0-9,]+)\s*bytes\)', re.IGNORECASE)

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    pairs = pattern.findall(desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        try:
            n = int(b.replace(',', '').replace('+',''))
        except Exception:
            continue
        if n > best_bytes:
            best_lang, best_bytes = lang, n
    return best_lang

lang_df['main_language'] = lang_df['language_description'].map(main_lang)

comm_df['commit_count'] = pd.to_numeric(comm_df['commit_count'], errors='coerce')

merged = comm_df.merge(lang_df[['repo_name','main_language']], on='repo_name', how='left')
# Exclude Python main language (case-insensitive)
filtered = merged[merged['main_language'].fillna('').str.lower() != 'python']
# Order by commit_count desc and take top 5
result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Ytkprb6KSdpUYX6YWK1GSbmE': 'file_storage/call_Ytkprb6KSdpUYX6YWK1GSbmE.json', 'var_call_nxAM8SpJ0l1Z7QYigvL1CRCw': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
