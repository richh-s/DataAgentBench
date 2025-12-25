code = """import json, re, pandas as pd

commits = pd.DataFrame(var_call_C4YwSzQ7lqNZfP4dLYFQrrgi)

with open(var_call_7jrXeVFaODB54cuEevBL1bXs, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# extract main language as the one with 'mainly written in X' or 'majority of the code is in X' or first in list
pattern_main = re.compile(r"mainly written in ([A-Za-z+#]+)|majority of the code is in ([A-Za-z+#]+)|built in ([A-Za-z+#]+)|includes: ([A-Za-z+#]+)")

def get_main(lang_desc):
    m = pattern_main.search(lang_desc)
    if not m:
        return None
    for g in m.groups():
        if g:
            return g
    return None

languages['main_language'] = languages['language_description'].apply(get_main)

merged = commits.merge(languages[['repo_name','main_language']], on='repo_name', how='left')

filtered = merged[merged['main_language'].str.lower() != 'python']

filtered['commit_count'] = filtered['commit_count'].astype(int)

top5 = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_C4YwSzQ7lqNZfP4dLYFQrrgi': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_7jrXeVFaODB54cuEevBL1bXs': 'file_storage/call_7jrXeVFaODB54cuEevBL1bXs.json', 'var_call_HyHfsBjLyJBnvu6PNY79aLul': [{'name': 'languages'}, {'name': 'repos'}, {'name': 'licenses'}]}

exec(code, env_args)
