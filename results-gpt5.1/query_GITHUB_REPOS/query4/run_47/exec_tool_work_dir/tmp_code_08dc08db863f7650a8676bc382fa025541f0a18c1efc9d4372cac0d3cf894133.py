code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_1swqgMsqZpTdczmVvMLJBIcG)
languages_path = var_call_fL9wICMqCLhpadivGLKT4EfK
with open(languages_path, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# determine main language from natural language description by picking language with max bytes
pattern = re.compile(r"([A-Za-z+#]+) \((\d[\d,]*) bytes\)")

main_langs = []
for _, row in languages.iterrows():
    desc = row['language_description'] or ''
    matches = pattern.findall(desc)
    main = None
    max_bytes = -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > max_bytes:
            max_bytes = b
            main = lang
    main_langs.append(main)

languages['main_language'] = main_langs

# join with commits
merged = commits.merge(languages, on='repo_name', how='left')

# filter main language not Python
filtered = merged[merged['main_language'].str.lower() != 'python']

top5 = filtered.sort_values('commit_count', ascending=False).head(5)
result = top5['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1swqgMsqZpTdczmVvMLJBIcG': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_fL9wICMqCLhpadivGLKT4EfK': 'file_storage/call_fL9wICMqCLhpadivGLKT4EfK.json'}

exec(code, env_args)
