code = """import json, re
import pandas as pd

# languages data file path
path = var_call_VzY2zunXuFTsSQ7xjSu9UZi5
with open(path, 'r') as f:
    languages = json.load(f)

lang_df = pd.DataFrame(languages)

# heuristic: main language is the one with highest byte count in the natural language string

def extract_main_language(desc):
    if not isinstance(desc, str):
        return None
    # find all "Language (number bytes)" patterns
    matches = re.findall(r"([A-Za-z+#]+) \((\d[\d,]*) bytes\)", desc)
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

lang_df['main_language'] = lang_df['language_description'].apply(extract_main_language)

# commits data
commits = var_call_PFMue7XH1oYvHU54YJlVAJtj
commits_df = pd.DataFrame(commits)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# join on repo_name
merged = commits_df.merge(lang_df[['repo_name', 'main_language']], on='repo_name', how='left')

# filter where main_language is not Python
filtered = merged[merged['main_language'].str.lower() != 'python']

# sort by commit_count desc and take top 5
result_df = filtered.sort_values('commit_count', ascending=False).head(5)

result = result_df['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_PFMue7XH1oYvHU54YJlVAJtj': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_VzY2zunXuFTsSQ7xjSu9UZi5': 'file_storage/call_VzY2zunXuFTsSQ7xjSu9UZi5.json'}

exec(code, env_args)
