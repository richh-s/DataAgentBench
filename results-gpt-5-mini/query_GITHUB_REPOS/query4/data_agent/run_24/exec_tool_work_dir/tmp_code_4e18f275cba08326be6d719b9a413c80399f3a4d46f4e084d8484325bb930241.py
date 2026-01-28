code = """import json
import re
import pandas as pd

# Load the large languages result from file path provided in var_call_QViaduQgNIQpZRUl3dJna4Hy
with open(var_call_QViaduQgNIQpZRUl3dJna4Hy, 'r', encoding='utf-8') as f:
    languages = json.load(f)

commits = var_call_YOdcze3V8ZxxfUP2N1PyFIbQ

# Parse language_description to extract language-byte pairs and determine the main language
lang_rows = []
pattern = re.compile(r"([A-Za-z0-9#\+\-\. ]+)\s*\(\s*([\d,]+)\s*bytes",
                     flags=re.IGNORECASE)
for r in languages:
    repo = r.get('repo_name')
    desc = r.get('language_description','')
    matches = pattern.findall(desc)
    if matches:
        # convert bytes and find max
        parsed = [(m[0].strip(), int(m[1].replace(',',''))) for m in matches]
        # pick language with max bytes
        main_lang = max(parsed, key=lambda x: x[1])[0]
    else:
        # fallback: try to take the first word of the description
        main_lang = desc.split()[0] if desc else None
    lang_rows.append({'repo_name': repo, 'main_language': main_lang})

df_lang = pd.DataFrame(lang_rows)

df_commits = pd.DataFrame(commits)
# ensure numeric commit_count
if 'commit_count' in df_commits.columns:
    df_commits['commit_count'] = df_commits['commit_count'].astype(int)

# Merge on repo_name
df_merged = pd.merge(df_commits, df_lang, on='repo_name', how='left')

# Filter out repositories whose main language is Python (case-insensitive)
def is_python(x):
    if not x or not isinstance(x, str):
        return False
    return x.strip().lower() == 'python'

filtered = df_merged[~df_merged['main_language'].apply(is_python)]

# Sort by commit_count desc and take top 5
top5 = filtered.sort_values('commit_count', ascending=False).head(5)

result_list = top5['repo_name'].tolist()

import json
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_QViaduQgNIQpZRUl3dJna4Hy': 'file_storage/call_QViaduQgNIQpZRUl3dJna4Hy.json', 'var_call_YOdcze3V8ZxxfUP2N1PyFIbQ': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
