code = """import json, re
import pandas as pd

commits = pd.DataFrame(var_call_vmv6nEv98rS5aedyFAYLIiGR)
commits['commit_count'] = commits['commit_count'].astype(int)

# load languages full
lang_src = var_call_GyZPgwf3he2wFU31LTGC1BjW
if isinstance(lang_src, str) and lang_src.endswith('.json'):
    with open(lang_src, 'r', encoding='utf-8') as f:
        languages_records = json.load(f)
else:
    languages_records = lang_src
languages = pd.DataFrame(languages_records)

# Parse main language as the one with max bytes in language_description
pat = re.compile(r"([A-Za-z0-9+#\-\. ]+?)\s*\((\d[\d,]*)\s*bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        try:
            n = int(b.replace(',', ''))
        except:
            continue
        lang = lang.strip()
        if n > best_bytes:
            best_lang, best_bytes = lang, n
    return best_lang

languages['main_language'] = languages['language_description'].map(main_lang)

df = commits.merge(languages[['repo_name','main_language']], on='repo_name', how='left')
# exclude repos whose main language is Python
filtered = df[df['main_language'].fillna('') != 'Python'].sort_values('commit_count', ascending=False)
result = filtered.head(5)['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vmv6nEv98rS5aedyFAYLIiGR': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_GyZPgwf3he2wFU31LTGC1BjW': 'file_storage/call_GyZPgwf3he2wFU31LTGC1BjW.json'}

exec(code, env_args)
