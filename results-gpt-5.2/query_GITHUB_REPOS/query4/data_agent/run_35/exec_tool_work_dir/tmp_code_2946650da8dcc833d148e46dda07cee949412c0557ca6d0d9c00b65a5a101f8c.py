code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_fK0s9TU8y7eW78zgRStsIQct)
commits['commit_count'] = commits['commit_count'].astype(int)

# load languages (may be a json file path)
lang_data = var_call_yFo5XwH8IvPrawkmVTeA4wBT
if isinstance(lang_data, str) and lang_data.endswith('.json'):
    with open(lang_data, 'r', encoding='utf-8') as f:
        lang_data = json.load(f)
langs = pd.DataFrame(lang_data)

# Parse main language as the one with the largest byte count in the description.
pat = re.compile(r"([A-Za-z0-9+#\-\. ]+)\s*\((\d[\d,]*)\s*bytes\)")

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
            best_bytes = n
            best_lang = lang.strip()
    return best_lang

langs['main_language'] = langs['language_description'].map(main_lang)

merged = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
non_python = merged[merged['main_language'].notna() & (merged['main_language'].str.lower() != 'python')]
non_python = non_python.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
result = non_python['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fK0s9TU8y7eW78zgRStsIQct': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_yFo5XwH8IvPrawkmVTeA4wBT': 'file_storage/call_yFo5XwH8IvPrawkmVTeA4wBT.json'}

exec(code, env_args)
