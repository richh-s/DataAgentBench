code = """import json, re
import pandas as pd

# Load languages result (may be a filepath)
langs_src = var_call_ti6vfi9xdIMy21hQsb6RfLd2
if isinstance(langs_src, str):
    with open(langs_src, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = langs_src

commits = var_call_mirIF7HHAVXhz1XxHQj57Hbn

lang_df = pd.DataFrame(langs)
commit_df = pd.DataFrame(commits)

# Extract main language as the one with max bytes in language_description
pattern = re.compile(r'([A-Za-z0-9_+.#-]+)\s*\((\d[\d,]*)\s*bytes\)')

def main_lang(desc):
    if desc is None:
        return None
    matches = pattern.findall(desc)
    if not matches:
        return None
    best_lang = None
    best_bytes = -1
    for lang, b in matches:
        try:
            n = int(b.replace(',', ''))
        except Exception:
            continue
        if n > best_bytes:
            best_bytes = n
            best_lang = lang
    return best_lang

lang_df['main_language'] = lang_df['language_description'].map(main_lang)

merged = commit_df.merge(lang_df[['repo_name','main_language']], on='repo_name', how='left')
# Only those not Python
filtered = merged[(merged['main_language'].notna()) & (merged['main_language'].str.lower() != 'python')].copy()
filtered['commit_count'] = pd.to_numeric(filtered['commit_count'], errors='coerce')
filtered = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_list = filtered['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_ti6vfi9xdIMy21hQsb6RfLd2': 'file_storage/call_ti6vfi9xdIMy21hQsb6RfLd2.json', 'var_call_mirIF7HHAVXhz1XxHQj57Hbn': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
