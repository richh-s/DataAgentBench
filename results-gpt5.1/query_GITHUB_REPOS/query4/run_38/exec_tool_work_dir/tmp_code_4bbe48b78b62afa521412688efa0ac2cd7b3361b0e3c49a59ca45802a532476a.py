code = """import json, re, pandas as pd

# languages large file path
languages_data = var_call_9ymPzDJaKsmHespRPDLYJBmR
with open(languages_data, 'r') as f:
    languages = json.load(f)

langs_df = pd.DataFrame(languages)

# function to extract main language: assume first language mentioned with highest bytes is main
pattern = re.compile(r"([A-Za-z+#]+) \((\d+,?\d*) bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if not matches:
        return None
    # bytes may have comma
    parsed = [(lang, int(bytes_str.replace(',', ''))) for lang, bytes_str in matches]
    parsed.sort(key=lambda x: x[1], reverse=True)
    return parsed[0][0]

langs_df['main_language'] = langs_df['language_description'].apply(main_lang)

commits = pd.DataFrame(var_call_ltHqBlCKQ3ubnyY1UC3AZbHs)
commits['commit_count'] = commits['commit_count'].astype(int)

merged = commits.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')

# filter out main_language == 'Python'
filtered = merged[merged['main_language'].ne('Python')]

result_names = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result_names)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9ymPzDJaKsmHespRPDLYJBmR': 'file_storage/call_9ymPzDJaKsmHespRPDLYJBmR.json', 'var_call_ltHqBlCKQ3ubnyY1UC3AZbHs': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
