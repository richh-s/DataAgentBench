code = """import json, re, pandas as pd

# languages large result path
path = var_call_NK0b55u4RcOxuqpANqMMwIfC
with open(path, 'r') as f:
    languages = json.load(f)

commits = var_call_Vt7F5qrIy2ED79HuEhSik9OT

# determine main language from language_description
pat = re.compile(r"([A-Za-z+#]+) \((\d+) bytes\)")

def main_lang(desc):
    matches = pat.findall(desc)
    if not matches:
        return None
    # pick language with max bytes
    lang, _ = max(matches, key=lambda x: int(x[1]))
    return lang

for row in languages:
    row['main_language'] = main_lang(row['language_description'])

# build dataframes
lang_df = pd.DataFrame(languages)[['repo_name', 'main_language']]
comm_df = pd.DataFrame(commits)
comm_df['commit_count'] = comm_df['commit_count'].astype(int)

# join
merged = comm_df.merge(lang_df, on='repo_name', how='left')

# filter main_language != 'Python'
filtered = merged[merged['main_language'].ne('Python')]

# sort by commit_count desc and take top 5
top5 = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_NK0b55u4RcOxuqpANqMMwIfC': 'file_storage/call_NK0b55u4RcOxuqpANqMMwIfC.json', 'var_call_Vt7F5qrIy2ED79HuEhSik9OT': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
