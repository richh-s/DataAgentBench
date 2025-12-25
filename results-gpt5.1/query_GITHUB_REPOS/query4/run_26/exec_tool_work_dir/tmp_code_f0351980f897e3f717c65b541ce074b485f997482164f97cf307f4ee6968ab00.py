code = """import json, pandas as pd

# load full languages table
with open(var_call_1Fp4MCOc2V8ukxUloFuuQKji, 'r') as f:
    languages_data = json.load(f)

df_lang = pd.DataFrame(languages_data)

# determine main language by parsing the description; it's the first language mentioned
# extract the token before the first ' ('
main_lang = df_lang['language_description'].str.extract(r'The (?:repository is mainly written in|majority of the code is in|codebase includes:|codebase is primarily|project is mainly|project is primarily|project is built in|codebase is mostly|main language is) ([^()]+?) \(' , expand=False)

# fallback: word before first ' (' if regex failed
main_lang = main_lang.fillna(df_lang['language_description'].str.extract(r'([A-Za-z\+#]+) \(', expand=False))

df_lang['main_language'] = main_lang.str.strip()

# commits summary from var_call_CCgyZILzz6v7cLlAk1zfzTJB
df_commits = pd.DataFrame(var_call_CCgyZILzz6v7cLlAk1zfzTJB)

# commit_count might be string; convert
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

# join on repo_name
merged = pd.merge(df_commits, df_lang, on='repo_name', how='left')

# filter where main_language is not Python
filtered = merged[merged['main_language'].str.lower() != 'python']

# sort by commit_count desc and take top 5
result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_CCgyZILzz6v7cLlAk1zfzTJB': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_1Fp4MCOc2V8ukxUloFuuQKji': 'file_storage/call_1Fp4MCOc2V8ukxUloFuuQKji.json'}

exec(code, env_args)
