code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_gilJbdMSemceMB7AafCyYhBI)

with open(var_call_KxJojcPYDr3Yh0sDzsdMDWEJ, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# Extract main language as the one with the largest byte count from the natural language description
pattern = re.compile(r"([A-Za-z+#]+) \((\d,[\d,]*|\d+) bytes\)")

main_langs = []
for _, row in languages.iterrows():
    text = row['language_description']
    matches = pattern.findall(text)
    if not matches:
        main_langs.append({'repo_name': row['repo_name'], 'main_language': None})
        continue
    # Normalize and pick max bytes
    best_lang, best_bytes = None, -1
    for lang, bytes_str in matches:
        n = int(bytes_str.replace(',', ''))
        if n > best_bytes:
            best_bytes = n
            best_lang = lang
    main_langs.append({'repo_name': row['repo_name'], 'main_language': best_lang})

main_df = pd.DataFrame(main_langs)

merged = commits.merge(main_df, on='repo_name', how='left')

# filter out main_language == 'Python'
filtered = merged[merged['main_language'].ne('Python')]

# sort by commit_count desc, ensure numeric
filtered['commit_count'] = filtered['commit_count'].astype(int)
filtered = filtered.sort_values('commit_count', ascending=False).head(5)

result = filtered['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gilJbdMSemceMB7AafCyYhBI': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_KxJojcPYDr3Yh0sDzsdMDWEJ': 'file_storage/call_KxJojcPYDr3Yh0sDzsdMDWEJ.json', 'var_call_BtBhCgfySz1nEyKQKB19LGNK': [{'name': 'languages'}, {'name': 'repos'}, {'name': 'licenses'}]}

exec(code, env_args)
