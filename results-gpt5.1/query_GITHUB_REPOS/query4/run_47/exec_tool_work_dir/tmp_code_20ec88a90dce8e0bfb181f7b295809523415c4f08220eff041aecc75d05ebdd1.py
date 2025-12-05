code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_1swqgMsqZpTdczmVvMLJBIcG)

# Lowercase repo_name for join key
commits['repo_name_l'] = commits['repo_name'].str.lower()

languages_path = var_call_fL9wICMqCLhpadivGLKT4EfK
with open(languages_path, 'r') as f:
    lang_data = json.load(f)

# Build mapping repo_name -> main_language without full DataFrame operations to speed up
pattern = re.compile(r"([A-Za-z+#]+) \((\d[\d,]*) bytes\)")
main_lang_map = {}
for rec in lang_data:
    desc = rec.get('language_description') or ''
    matches = pattern.findall(desc)
    main = None
    max_bytes = -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > max_bytes:
            max_bytes = b
            main = lang
    if rec.get('repo_name'):
        main_lang_map[rec['repo_name'].lower()] = main

# attach main language to commits rows
main_langs = [main_lang_map.get(rn, None) for rn in commits['repo_name_l']]
commits['main_language'] = main_langs

# filter not Python
mask = commits['main_language'].str.lower() != 'python'
filtered = commits[mask]

# top 5 by commit_count (cast to int)
filtered['commit_count'] = filtered['commit_count'].astype(int)
filtered = filtered.sort_values('commit_count', ascending=False).head(5)
result = filtered['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1swqgMsqZpTdczmVvMLJBIcG': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_fL9wICMqCLhpadivGLKT4EfK': 'file_storage/call_fL9wICMqCLhpadivGLKT4EfK.json'}

exec(code, env_args)
