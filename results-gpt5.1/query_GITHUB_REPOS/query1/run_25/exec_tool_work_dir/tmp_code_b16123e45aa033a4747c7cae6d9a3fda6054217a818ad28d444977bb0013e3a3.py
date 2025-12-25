code = """import json, re, pandas as pd

# Load full results from JSON files
with open(var_call_suv0Hcf0wQt02gInh6vC2mGI, 'r') as f:
    readmes = json.load(f)
with open(var_call_E0K55TGmQKgXSRoVFRts9CQg, 'r') as f:
    langs = json.load(f)

# Create DataFrames
readmes_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

# Normalize columns
readmes_df.rename(columns={'sample_repo_name': 'repo_name'}, inplace=True)

# Identify repos that use Python based on language_description mentioning 'Python ('
# We'll treat any mention of 'Python (' as sign of Python usage.
langs_df['uses_python'] = langs_df['language_description'].str.contains(r'Python ', case=False, na=False)

# Get set of repos that use Python
python_repos = set(langs_df.loc[langs_df['uses_python'], 'repo_name'])

# Filter readmes to those where repo is known in langs_df (to know if it uses Python or not)
merged = readmes_df.merge(langs_df[['repo_name', 'uses_python']], on='repo_name', how='left')

# Consider repos that do NOT use Python (uses_python == False or NaN)
non_python_readmes = merged[(merged['uses_python'] == False) | (merged['uses_python'].isna())].copy()

# Define heuristic for copyright info in README
pattern = re.compile(r'copyright|\bcopyright \(c\)|\u00a9', re.IGNORECASE)
non_python_readmes['has_copyright'] = non_python_readmes['content'].fillna('').str.contains(pattern)

# Compute proportion
total_non_python = len(non_python_readmes)
with_copyright = int(non_python_readmes['has_copyright'].sum())
proportion = with_copyright / total_non_python if total_non_python > 0 else None

result = {
    'total_non_python_readmes': total_non_python,
    'non_python_readmes_with_copyright': with_copyright,
    'proportion': proportion
}

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_suv0Hcf0wQt02gInh6vC2mGI': 'file_storage/call_suv0Hcf0wQt02gInh6vC2mGI.json', 'var_call_E0K55TGmQKgXSRoVFRts9CQg': 'file_storage/call_E0K55TGmQKgXSRoVFRts9CQg.json', 'var_call_WeRTb5ICKujg7SP5T6gujFyB': 'file_storage/call_WeRTb5ICKujg7SP5T6gujFyB.json', 'var_call_bm5vbQ6kiAppzHJEymlQKMOg': 'file_storage/call_bm5vbQ6kiAppzHJEymlQKMOg.json', 'var_call_jMZjDYpob3jbCo7RyEhc8djj': 'file_storage/call_jMZjDYpob3jbCo7RyEhc8djj.json', 'var_call_JAinxuxT2MG38NvRtBXJERJT': 'file_storage/call_JAinxuxT2MG38NvRtBXJERJT.json'}

exec(code, env_args)
