code = """import json, pandas as pd, re

commits_df = pd.DataFrame(var_call_QtcPfHhLDBs98frSfY9pZeJq)

# Load only needed language rows for the top 100 repos to avoid heavy processing
with open(var_call_CCMPZFQJjdKsHWTgkNBFoiIL, 'r') as f:
    languages_data = json.load(f)

languages_df = pd.DataFrame(languages_data)

top_repos = set(commits_df['repo_name'].tolist())
lang_subset = languages_df[languages_df['repo_name'].isin(top_repos)].copy()

main_langs = []
for _, row in lang_subset.iterrows():
    desc = row['language_description']
    matches = re.findall(r"([A-Za-z+#]+) \(([0-9,]+) bytes\)", desc)
    if not matches:
        main_langs.append((row['repo_name'], None))
        continue
    max_lang = None
    max_bytes = -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > max_bytes:
            max_bytes = b
            max_lang = lang
    main_langs.append((row['repo_name'], max_lang))

main_langs_df = pd.DataFrame(main_langs, columns=['repo_name', 'main_language'])

merged = commits_df.merge(main_langs_df, on='repo_name', how='left')

filtered = merged[merged['main_language'].str.lower() != 'python']

# commit_count is currently string from SQL; convert to int for correct sorting
filtered['commit_count'] = filtered['commit_count'].astype(int)

top5 = filtered.sort_values('commit_count', ascending=False).head(5)

result = top5['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QtcPfHhLDBs98frSfY9pZeJq': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_CCMPZFQJjdKsHWTgkNBFoiIL': 'file_storage/call_CCMPZFQJjdKsHWTgkNBFoiIL.json'}

exec(code, env_args)
