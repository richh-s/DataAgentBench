code = """import json, re, pandas as pd

commits_df = pd.DataFrame(var_call_glI54GjJhROHpkbKi4YlXYFK)

with open(var_call_A9yrR7h3HcWrIvw5QUCt8WHT, 'r') as f:
    languages_data = json.load(f)

langs_df = pd.DataFrame(languages_data)

pattern_main = re.compile(r"mainly written in ([A-Za-z+#]+)|majority of the code is in ([A-Za-z+#]+)|While most of the project is built in ([A-Za-z+#]+)|The codebase includes: ([A-Za-z+#]+) \(", re.IGNORECASE)

def extract_main_language(desc):
    m = pattern_main.search(desc)
    if not m:
        return None
    for g in m.groups():
        if g:
            return g.strip().title()
    return None

langs_df['main_language'] = langs_df['language_description'].apply(extract_main_language)

merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')

filtered = merged[merged['main_language'].str.lower() != 'python']

top5 = filtered.sort_values('commit_count', ascending=False).head(5)

result = top5['repo_name'].tolist()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_glI54GjJhROHpkbKi4YlXYFK': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_A9yrR7h3HcWrIvw5QUCt8WHT': 'file_storage/call_A9yrR7h3HcWrIvw5QUCt8WHT.json'}

exec(code, env_args)
