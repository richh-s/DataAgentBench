code = """import json, re
import pandas as pd

commits = pd.DataFrame(var_call_PTmGazx1Cvy0z4xAqQMr6iQD)
commits['commit_count'] = commits['commit_count'].astype(int)

# Load full languages table
path = var_call_6YfsJJUL5AFjNfzqDRInFzBm
with open(path, 'r', encoding='utf-8') as f:
    langs_records = json.load(f)
langs = pd.DataFrame(langs_records)

# Parse main language as the one with max bytes in language_description
pat = re.compile(r"([A-Za-z0-9+.#-]+)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc: str):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        n = int(b.replace(',', ''))
        if n > best_bytes:
            best_lang, best_bytes = lang, n
    return best_lang

langs['main_language'] = langs['language_description'].map(main_lang)

df = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
# keep non-Python main language
out = df[df['main_language'].notna() & (df['main_language'].str.lower() != 'python')].sort_values('commit_count', ascending=False).head(5)
result = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PTmGazx1Cvy0z4xAqQMr6iQD': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_6YfsJJUL5AFjNfzqDRInFzBm': 'file_storage/call_6YfsJJUL5AFjNfzqDRInFzBm.json'}

exec(code, env_args)
