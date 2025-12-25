code = """import json, re, pandas as pd

# languages result is in a JSON file path
path = var_call_DLpTdS4ZDHHoRvNY1jqI5skE
with open(path, 'r') as f:
    languages_data = json.load(f)

langs_df = pd.DataFrame(languages_data)
commits_df = pd.DataFrame(var_call_BGYv24m21D7gZTWkqS0FZQ9M)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# determine main language from language_description
pattern = re.compile(r"([A-Za-z+#]+) \((\d[\d,]*) bytes\)")

def main_lang(desc):
    matches = pattern.findall(desc or '')
    if not matches:
        return None
    # pick language with max bytes
    max_lang = None
    max_bytes = -1
    for lang, bytes_str in matches:
        b = int(bytes_str.replace(',', ''))
        if b > max_bytes:
            max_bytes = b
            max_lang = lang
    return max_lang

langs_df['main_language'] = langs_df['language_description'].apply(main_lang)

# merge commits with languages
merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')

# filter out Python main language
filtered = merged[merged['main_language'].str.lower() != 'python']

# sort by commit_count desc and take top 5
top5 = filtered.sort_values('commit_count', ascending=False).head(5)

result = top5['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_DLpTdS4ZDHHoRvNY1jqI5skE': 'file_storage/call_DLpTdS4ZDHHoRvNY1jqI5skE.json', 'var_call_BGYv24m21D7gZTWkqS0FZQ9M': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
