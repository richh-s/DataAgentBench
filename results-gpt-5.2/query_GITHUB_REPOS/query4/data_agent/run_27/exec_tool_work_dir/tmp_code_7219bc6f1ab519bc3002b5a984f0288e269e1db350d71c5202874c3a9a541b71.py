code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_3zqDhwSAP8G2AHyVZLPZH1JR)
commits['commit_count'] = commits['commit_count'].astype(int)

# load languages full
path = var_call_QeJwMbgJ10njsSoUBdwYqKbE
with open(path, 'r', encoding='utf-8') as f:
    languages_raw = json.load(f)
langs = pd.DataFrame(languages_raw)

# parse main language as the one with max bytes mentioned in description
pat = re.compile(r"([A-Za-z0-9_+\-#.]+)\s*\((\d[\d,]*)\s*bytes\)")

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
            best_lang, best_bytes = lang, n
    return best_lang

langs['main_language'] = langs['language_description'].map(main_lang)

# join and filter main language != Python
merged = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')]

top5 = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_3zqDhwSAP8G2AHyVZLPZH1JR': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_QeJwMbgJ10njsSoUBdwYqKbE': 'file_storage/call_QeJwMbgJ10njsSoUBdwYqKbE.json'}

exec(code, env_args)
