code = """import json, re, pandas as pd

# Load full results from JSON files
with open(var_call_0EyrMrinBn7tWERAOmWO9llw, 'r') as f:
    readmes = json.load(f)
with open(var_call_TK0gjKabgQ2chx3zSWpJOgcw, 'r') as f:
    langs = json.load(f)

# Build DataFrames
readmes_df = pd.DataFrame(readmes)[['sample_repo_name', 'content']].rename(columns={'sample_repo_name': 'repo_name'})
langs_df = pd.DataFrame(langs)[['repo_name', 'language_description']]

# Identify repos that use Python (language_description contains 'Python (' case-insensitive)
python_mask = langs_df['language_description'].str.contains(r'Python \(', flags=re.IGNORECASE, na=False)
non_python_langs = langs_df[~python_mask]

# Join with READMEs: only repos that have a README.md content row
merged = pd.merge(readmes_df, non_python_langs, on='repo_name', how='inner')

# Function to detect copyright info in README content
copyright_pattern = re.compile(r"copyright|©|copr\.\b|\b(c)\b", re.IGNORECASE)

merged['has_copyright'] = merged['content'].fillna('').apply(lambda txt: bool(copyright_pattern.search(txt)))

# Compute proportion
if len(merged) == 0:
    proportion = None
else:
    proportion = merged['copyright'].mean()

result = {
    'total_non_python_repos_with_readme': int(len(merged)),
    'count_with_copyright': int(merged['has_copyright'].sum()) if len(merged) > 0 else 0,
    'proportion': float(merged['has_copyright'].mean()) if len(merged) > 0 else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0EyrMrinBn7tWERAOmWO9llw': 'file_storage/call_0EyrMrinBn7tWERAOmWO9llw.json', 'var_call_TK0gjKabgQ2chx3zSWpJOgcw': 'file_storage/call_TK0gjKabgQ2chx3zSWpJOgcw.json'}

exec(code, env_args)
