code = """import json, re, pandas as pd

# languages table is large; load from file
path = var_call_uydOJq6rKIVbJ6MaqOs16fYG
with open(path, 'r') as f:
    languages_data = json.load(f)

commits_data = var_call_l4HBl1dvA8g9uda7aIbGIjvH

langs_df = pd.DataFrame(languages_data)
commits_df = pd.DataFrame(commits_data)

# Extract primary language as the one with largest bytes from language_description
lang_pattern = re.compile(r"([A-Za-z+#]+) \((\d+,?\d*) bytes\)")

def get_main_language(desc):
    if not isinstance(desc, str):
        return None
    matches = lang_pattern.findall(desc)
    if not matches:
        return None
    # parse bytes and pick max
    best_lang, best_bytes = None, -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > best_bytes:
            best_lang, best_bytes = lang, b
    return best_lang

langs_df['main_language'] = langs_df['language_description'].apply(get_main_language)

# Merge commits with languages
merged = commits_df.merge(langs_df[['repo_name', 'main_language']], on='repo_name', how='left')

# filter out Python as main language
filtered = merged[merged['main_language'].str.lower() != 'python']

# order by commit_count desc (already ordered but ensure) and take top 5
filtered['commit_count'] = filtered['commit_count'].astype(int)
filtered = filtered.sort_values('commit_count', ascending=False).head(5)

result = filtered['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uydOJq6rKIVbJ6MaqOs16fYG': 'file_storage/call_uydOJq6rKIVbJ6MaqOs16fYG.json', 'var_call_l4HBl1dvA8g9uda7aIbGIjvH': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
