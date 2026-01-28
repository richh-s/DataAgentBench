code = """import json, re
import pandas as pd

# Load languages (may be file path)
langs_src = var_call_nHhhU9lmMtXl7RPl8V6HmtMK
if isinstance(langs_src, str):
    with open(langs_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_src

commits = var_call_MEefoDMSjre68gfGUEQ3mqQh

def main_language(desc: str):
    if desc is None:
        return None
    # Extract "Language (number bytes)" pairs
    pairs = re.findall(r'([A-Za-z0-9_+#\.\- ]+)\s*\((\d[\d,]*)\s*bytes\)', desc)
    if not pairs:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in pairs:
        b_int = int(b.replace(',', ''))
        lang_clean = lang.strip().rstrip(':')
        if b_int > best_bytes:
            best_bytes = b_int
            best_lang = lang_clean
    return best_lang

lang_map = {r['repo_name']: main_language(r.get('language_description')) for r in langs}

# Determine top five by commits whose main language != Python
rows = []
for r in commits:
    rn = r['repo_name']
    ml = lang_map.get(rn)
    cc = int(r['commit_count']) if isinstance(r['commit_count'], str) else r['commit_count']
    rows.append({'repo_name': rn, 'commit_count': cc, 'main_language': ml})

df = pd.DataFrame(rows)
# Exclude Python main language
out = df[df['main_language'].notna() & (df['main_language'].str.lower() != 'python')].sort_values('commit_count', ascending=False).head(5)
answer_list = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_nHhhU9lmMtXl7RPl8V6HmtMK': 'file_storage/call_nHhhU9lmMtXl7RPl8V6HmtMK.json', 'var_call_MEefoDMSjre68gfGUEQ3mqQh': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
