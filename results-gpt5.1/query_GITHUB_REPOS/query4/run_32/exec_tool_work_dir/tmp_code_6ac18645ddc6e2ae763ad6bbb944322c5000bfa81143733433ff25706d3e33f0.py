code = """import json, pandas as pd

commits = pd.DataFrame(var_call_z39g2hjkVyPuybZxarGCtM2h)

with open(var_call_b4WL6QLZt5fTKc3Gy6G8JXsX, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# Determine main language as the one with the highest bytes mentioned in language_description
# We'll parse patterns like "Language (123 bytes)" and pick the max per repo.
import re

lang_rows = []
for _, row in languages.iterrows():
    desc = row['language_description']
    matches = re.findall(r"([A-Za-z+#]+) \((\d+) bytes\)", desc)
    if not matches:
        continue
    # pick language with max bytes
    main_lang, _ = max(matches, key=lambda x: int(x[1]))
    lang_rows.append({'repo_name': row['repo_name'], 'main_language': main_lang})

main_lang_df = pd.DataFrame(lang_rows)

# Filter out repos whose main language is Python
non_python = main_lang_df[main_lang_df['main_language'].str.lower() != 'python']

# Join with commits
merged = pd.merge(commits, non_python, on='repo_name')

# Get top five by commit_count (convert to int)
merged['commit_count'] = merged['commit_count'].astype(int)
result = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_z39g2hjkVyPuybZxarGCtM2h': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_b4WL6QLZt5fTKc3Gy6G8JXsX': 'file_storage/call_b4WL6QLZt5fTKc3Gy6G8JXsX.json'}

exec(code, env_args)
