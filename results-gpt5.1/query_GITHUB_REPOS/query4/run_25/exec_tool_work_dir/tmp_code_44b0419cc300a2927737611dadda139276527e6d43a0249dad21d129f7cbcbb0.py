code = """import json, pandas as pd, os

# Load full languages data
with open(var_call_aoT8BhtRYrD8CFT2opLrEGIA, 'r') as f:
    languages_data = json.load(f)

df_lang = pd.DataFrame(languages_data)

# Determine main language from language_description text (largest bytes mentioned)
import re

main_langs = []
for desc in df_lang['language_description']:
    # find patterns like "Python (123,456 bytes)"
    matches = re.findall(r"([A-Za-z+#]+) \(([0-9,]+) bytes\)", desc)
    if not matches:
        main_langs.append(None)
        continue
    # pick language with max bytes
    max_lang = None
    max_bytes = -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > max_bytes:
            max_bytes = b
            max_lang = lang
    main_langs.append(max_lang)

df_lang['main_language'] = main_langs

# Commit counts
df_commits = pd.DataFrame(var_call_Vvrx4RdbyM2FRQDfoXUqi4FO)

# merge on repo_name
df = pd.merge(df_commits, df_lang[['repo_name','main_language']], on='repo_name', how='left')

# filter main_language != 'Python'
filtered = df[df['main_language'] != 'Python'].copy()

# sort by commit_count desc (ensure numeric) and take top 5
filtered['commit_count'] = filtered['commit_count'].astype(int)
filtered = filtered.sort_values('commit_count', ascending=False).head(5)

result = filtered['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Vvrx4RdbyM2FRQDfoXUqi4FO': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_aoT8BhtRYrD8CFT2opLrEGIA': 'file_storage/call_aoT8BhtRYrD8CFT2opLrEGIA.json'}

exec(code, env_args)
