code = """import json, re, pandas as pd

# load languages (may be file path)
langs = var_call_0Ekigk35kfdrR50QrFY0mgO9
if isinstance(langs, str):
    with open(langs, 'r', encoding='utf-8') as f:
        langs = json.load(f)

commits = var_call_PghkdTjMdRxN1u6Qt5pwqECl

df_lang = pd.DataFrame(langs)
df_comm = pd.DataFrame(commits)

# parse main language from language_description by extracting all "Lang (bytes)" pairs and taking max bytes
pat = re.compile(r"([A-Za-z0-9+#.-]+)\s*\(([,0-9]+)\s*bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    pairs = pat.findall(desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_lang, best_bytes = lang, n
    return best_lang

df_lang['main_language'] = df_lang['language_description'].map(main_lang)

# join commit counts with main language
# commit_count is string in tool output; convert
if 'commit_count' in df_comm.columns:
    df_comm['commit_count'] = pd.to_numeric(df_comm['commit_count'], errors='coerce')

merged = df_comm.merge(df_lang[['repo_name','main_language']], on='repo_name', how='left')

# filter not Python
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

# order by commit_count desc, take top 5
out = filtered.sort_values('commit_count', ascending=False).head(5)
answer_list = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_0Ekigk35kfdrR50QrFY0mgO9': 'file_storage/call_0Ekigk35kfdrR50QrFY0mgO9.json', 'var_call_PghkdTjMdRxN1u6Qt5pwqECl': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
