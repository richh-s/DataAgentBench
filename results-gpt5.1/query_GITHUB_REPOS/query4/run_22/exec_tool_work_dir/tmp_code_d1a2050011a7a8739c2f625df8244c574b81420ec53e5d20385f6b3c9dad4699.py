code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_gilJbdMSemceMB7AafCyYhBI)

# Load only relevant language rows for these repos to avoid processing the entire file
repo_names = commits['repo_name'].unique().tolist()

selected_rows = []
with open(var_call_KxJojcPYDr3Yh0sDzsdMDWEJ, 'r') as f:
    data = json.load(f)
    repo_set = set(repo_names)
    for row in data:
        if row['repo_name'] in repo_set:
            selected_rows.append(row)

languages = pd.DataFrame(selected_rows)

pattern = re.compile(r"([A-Za-z+#]+) \(([\d,]+) bytes\)")

main_langs = []
for _, row in languages.iterrows():
    text = row['language_description']
    matches = pattern.findall(text)
    if not matches:
        main_langs.append({'repo_name': row['repo_name'], 'main_language': None})
        continue
    best_lang, best_bytes = None, -1
    for lang, bytes_str in matches:
        n = int(bytes_str.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best_lang = lang
    main_langs.append({'repo_name': row['repo_name'], 'main_language': best_lang})

main_df = pd.DataFrame(main_langs)

merged = commits.merge(main_df, on='repo_name', how='left')

filtered = merged[merged['main_language'].ne('Python')]

filtered['commit_count'] = filtered['commit_count'].astype(int)
filtered = filtered.sort_values('commit_count', ascending=False).head(5)

result = filtered['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gilJbdMSemceMB7AafCyYhBI': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_KxJojcPYDr3Yh0sDzsdMDWEJ': 'file_storage/call_KxJojcPYDr3Yh0sDzsdMDWEJ.json', 'var_call_BtBhCgfySz1nEyKQKB19LGNK': [{'name': 'languages'}, {'name': 'repos'}, {'name': 'licenses'}]}

exec(code, env_args)
