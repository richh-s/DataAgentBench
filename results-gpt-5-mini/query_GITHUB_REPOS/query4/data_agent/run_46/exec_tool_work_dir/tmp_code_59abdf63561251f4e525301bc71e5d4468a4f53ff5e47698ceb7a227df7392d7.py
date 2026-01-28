code = """import json
import re
import pandas as pd

# Load languages data from the stored JSON file path var_call_TjqKuvZN2LsBjy2FbJDTtq5Y
with open(var_call_TjqKuvZN2LsBjy2FbJDTtq5Y, 'r') as f:
    languages = json.load(f)

# commits data is available as var_call_8vMSvpbaqJRNkYfi3y05xHUi
commits = var_call_8vMSvpbaqJRNkYfi3y05xHUi

# Create DataFrames
df_lang = pd.DataFrame(languages)
df_commits = pd.DataFrame(commits)

# Ensure commit_count is int
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

# Function to extract primary language from language_description
pattern = re.compile(r"([A-Za-z0-9\+\#\.]+(?:[ \-\/][A-Za-z0-9\+\#\.]*)*)\s*\(\s*([\d,]+)\s*bytes", re.IGNORECASE)

def get_primary_language(desc):
    if not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if not matches:
        return None
    # Convert to (language, bytes)
    lst = []
    for lang, bytes_str in matches:
        try:
            num = int(bytes_str.replace(',', ''))
        except:
            num = 0
        lst.append((lang.strip(), num))
    # pick language with max bytes
    if not lst:
        return None
    primary = max(lst, key=lambda x: x[1])[0]
    # Normalize common names (e.g., Javascript -> JavaScript)
    return primary

# Apply to df_lang
df_lang['primary_language'] = df_lang['language_description'].apply(get_primary_language)

# Merge commits with primary language info
df_merged = pd.merge(df_commits, df_lang[['repo_name', 'primary_language']], on='repo_name', how='left')

# Filter where primary_language is not Python (case-insensitive) and not null
mask = df_merged['primary_language'].notnull() & (df_merged['primary_language'].str.lower() != 'python')
filtered = df_merged[mask].copy()

# Sort by commit_count descending and take top 5
top5 = filtered.sort_values('commit_count', ascending=False).head(5)

# Prepare result list of repo_name in order
result_list = top5['repo_name'].tolist()

# For transparency, if fewer than 5 results, still return what's available
output = json.dumps(result_list)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_TjqKuvZN2LsBjy2FbJDTtq5Y': 'file_storage/call_TjqKuvZN2LsBjy2FbJDTtq5Y.json', 'var_call_8vMSvpbaqJRNkYfi3y05xHUi': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
