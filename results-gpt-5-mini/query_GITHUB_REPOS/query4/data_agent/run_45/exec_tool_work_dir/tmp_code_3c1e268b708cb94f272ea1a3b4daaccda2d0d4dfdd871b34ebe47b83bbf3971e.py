code = """import json
import re
import pandas as pd

# Load the large languages result which may be a file path
langs_data = None
if isinstance(var_call_4Fev3etafn5hekfOyLYcIiIG, str) and var_call_4Fev3etafn5hekfOyLYcIiIG.endswith('.json'):
    with open(var_call_4Fev3etafn5hekfOyLYcIiIG, 'r', encoding='utf-8') as f:
        langs_data = json.load(f)
else:
    langs_data = var_call_4Fev3etafn5hekfOyLYcIiIG

commits_data = var_call_l4EROdf30XeHOw3Xs8D0TfwH

# Convert to DataFrames
df_langs = pd.DataFrame(langs_data)
df_commits = pd.DataFrame(commits_data)

# Normalize commit_count to int
if 'commit_count' in df_commits.columns:
    df_commits['commit_count'] = df_commits['commit_count'].astype(int)

# Keep only languages for repos present in commits list to limit processing
commit_repos = set(df_commits['repo_name'].tolist())
df_langs = df_langs[df_langs['repo_name'].isin(commit_repos)].copy()

# Function to parse main language
pattern = re.compile(r"([^,()]+?)\s*\(\s*([\d,]+)\s*bytes", re.IGNORECASE)

def parse_main_language(desc):
    if not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if matches:
        best = None
        best_bytes = -1
        for name, num in matches:
            try:
                n = int(num.replace(',', ''))
            except:
                n = 0
            name = name.strip()
            if n > best_bytes:
                best = name
                best_bytes = n
        return best
    # fallback: simple contains
    if 'python' in desc.lower():
        return 'Python'
    return None

# Apply parser
df_langs['main_language'] = df_langs['language_description'].apply(parse_main_language)

# Merge with commits
df_merged = pd.merge(df_commits, df_langs[['repo_name','main_language']], on='repo_name', how='left')

# Filter out Python main language
filtered = df_merged[~df_merged['main_language'].str.lower().eq('python')]
# For rows where main_language is NaN/None, treat as not Python (keep them)
filtered = df_merged[~(df_merged['main_language'].fillna('').str.lower() == 'python')]

# Sort by commit_count desc and take top 5
top5 = filtered.sort_values('commit_count', ascending=False).head(5)
result_list = top5['repo_name'].tolist()

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_4Fev3etafn5hekfOyLYcIiIG': 'file_storage/call_4Fev3etafn5hekfOyLYcIiIG.json', 'var_call_l4EROdf30XeHOw3Xs8D0TfwH': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
