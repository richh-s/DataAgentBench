code = """import json, re
import pandas as pd

commit_counts = pd.DataFrame(var_call_pWLb9E89WjTNZ83vL3xkhZ4x)
commit_counts['commit_count'] = pd.to_numeric(commit_counts['commit_count'], errors='coerce')

# load languages (may be file path)
lang_data = var_call_ySJvxhrev7AzeLs6KQBEBMDE
if isinstance(lang_data, str):
    with open(lang_data, 'r', encoding='utf-8') as f:
        lang_records = json.load(f)
else:
    lang_records = lang_data
languages = pd.DataFrame(lang_records)

# compute main language by max bytes parsed from description
pat = re.compile(r'([A-Za-z0-9+.#-]+) \(([0-9,]+) bytes\)')

def main_lang(desc):
    if desc is None:
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best = None
    best_bytes = -1
    for lang, b in matches:
        nb = int(b.replace(',', ''))
        if nb > best_bytes:
            best_bytes = nb
            best = lang
    return best

languages['main_language'] = languages['language_description'].map(main_lang)

df = commit_counts.merge(languages[['repo_name','main_language']], on='repo_name', how='left')

# filter main language not Python
out = df[(df['main_language'].notna()) & (df['main_language'].str.lower() != 'python')].sort_values('commit_count', ascending=False).head(5)
result = out['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_pWLb9E89WjTNZ83vL3xkhZ4x': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_ySJvxhrev7AzeLs6KQBEBMDE': 'file_storage/call_ySJvxhrev7AzeLs6KQBEBMDE.json'}

exec(code, env_args)
