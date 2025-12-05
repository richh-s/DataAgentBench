code = """import json, re, pandas as pd
from pathlib import Path

# Load languages data from file
path = Path(var_call_yDToxgFZpBYTsIUyn2sNZuMJ)
with path.open() as f:
    languages_data = json.load(f)

# Create DataFrames
commits_df = pd.DataFrame(var_call_9FKSoSN1qwxMPSvsDdRPGAZG)
languages_df = pd.DataFrame(languages_data)

# Function to extract main language from description
lang_pattern = re.compile(r"mainly written in ([^(,]+)|majority of the code is in ([^(,]+)|While most of the project is built in ([^(,]+)|The codebase includes: ([^(,]+)")

def extract_main_language(desc):
    m = lang_pattern.search(desc)
    if not m:
        return None
    for g in m.groups():
        if g:
            return g.strip()
    return None

languages_df['main_language'] = languages_df['language_description'].apply(extract_main_language)

# Filter out Python main language
non_python_langs = languages_df[languages_df['main_language'].str.lower() != 'python']

# Join commits with languages
merged = commits_df.merge(non_python_langs[['repo_name']], on='repo_name', how='inner')

# Sort by commit_count (cast to int) desc and get top 5
merged['commit_count'] = merged['commit_count'].astype(int)
Top5 = merged.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

result = json.dumps(Top5)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_9FKSoSN1qwxMPSvsDdRPGAZG': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_yDToxgFZpBYTsIUyn2sNZuMJ': 'file_storage/call_yDToxgFZpBYTsIUyn2sNZuMJ.json'}

exec(code, env_args)
