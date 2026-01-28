code = """import json
import re
import pandas as pd

# Load previous tool results provided in storage
commits = var_call_VXmFE6G0oEtXGQoTGsztU6L7
languages_file = var_call_mw1hQptbH484kgjsXoSB0Sut

# Load the large languages result from the file path
with open(languages_file, 'r') as f:
    languages = json.load(f)

# Create DataFrames
df_commits = pd.DataFrame(commits)
# Ensure commit_count is an integer
if 'commit_count' in df_commits.columns:
    df_commits['commit_count'] = df_commits['commit_count'].astype(int)
else:
    df_commits['commit_count'] = 0

df_lang = pd.DataFrame(languages)

# Function to parse main language from language_description
pattern = re.compile(r'([A-Za-z0-9+#\-\.\s]+?) \(([\d,]+) bytes\)')

def get_main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if not matches:
        return None
    max_lang = None
    max_bytes = -1
    for lang, b in matches:
        try:
            bval = int(b.replace(',', ''))
        except:
            continue
        lang_clean = lang.strip()
        if bval > max_bytes:
            max_bytes = bval
            max_lang = lang_clean
    return max_lang

if 'language_description' in df_lang.columns:
    df_lang['main_language'] = df_lang['language_description'].apply(get_main_lang)
else:
    df_lang['main_language'] = None

# Merge commits and languages on repo_name
if 'repo_name' in df_commits.columns and 'repo_name' in df_lang.columns:
    df = pd.merge(df_commits, df_lang[['repo_name', 'main_language']], on='repo_name', how='left')
else:
    df = df_commits.copy()
    df['main_language'] = None

# Filter: main_language determined and not Python
df_filtered = df[df['main_language'].notnull() & (df['main_language'].str.lower() != 'python')]

# Sort by commit_count desc and get top 5 repo names
df_sorted = df_filtered.sort_values(by='commit_count', ascending=False)

top5 = df_sorted.head(5)['repo_name'].tolist()

# Prepare result as JSON-serializable string
result_json = json.dumps(top5)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_EPr8fDD1CqBP8v9O2KGjUIs9': ['languages', 'repos', 'licenses'], 'var_call_TeV08pl74Z4ir2dvKrm8mqhc': ['commits', 'contents', 'files'], 'var_call_VXmFE6G0oEtXGQoTGsztU6L7': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}], 'var_call_mw1hQptbH484kgjsXoSB0Sut': 'file_storage/call_mw1hQptbH484kgjsXoSB0Sut.json'}

exec(code, env_args)
