code = """import json, pandas as pd

commits_df = pd.DataFrame(var_call_Zlv094z1a5OiqAqlbCNsSM3v)

with open(var_call_YUyzE2RXY9nYRvZMvUVlSVA5, 'r') as f:
    languages_data = json.load(f)

langs_df = pd.DataFrame(languages_data)

# Determine main language as the one with the highest bytes in the description
import re

main_langs = []
for _, row in langs_df.iterrows():
    desc = row['language_description']
    # find all "Language (number bytes)"
    matches = re.findall(r'([A-Za-z+#]+) \((\d[\d,]*) bytes\)', desc)
    if not matches:
        main_langs.append({'repo_name': row['repo_name'], 'main_language': None})
        continue
    # pick max bytes
    best_lang = None
    best_bytes = -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > best_bytes:
            best_bytes = b
            best_lang = lang
    main_langs.append({'repo_name': row['repo_name'], 'main_language': best_lang})

main_langs_df = pd.DataFrame(main_langs)

merged = commits_df.merge(main_langs_df, on='repo_name', how='left')

filtered = merged[merged['main_language'].str.lower() != 'python']

top5 = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Zlv094z1a5OiqAqlbCNsSM3v': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_YUyzE2RXY9nYRvZMvUVlSVA5': 'file_storage/call_YUyzE2RXY9nYRvZMvUVlSVA5.json'}

exec(code, env_args)
