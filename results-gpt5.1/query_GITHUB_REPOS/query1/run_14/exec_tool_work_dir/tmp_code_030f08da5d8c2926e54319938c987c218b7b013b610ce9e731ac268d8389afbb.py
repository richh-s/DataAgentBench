code = """import json, pandas as pd

contents_readmes = var_call_neGRorwxUb0ndRHwV0JzoISe
languages = var_call_RFfVxCRkGoUeJLBYO8PMFlHr

# Load into DataFrames
df_readmes = pd.read_json(contents_readmes)
df_lang = pd.read_json(languages)

# Determine repos that do NOT use Python (language_description does not contain 'Python')
no_python_repos = df_lang[~df_lang['language_description'].str.contains('Python', case=False, na=False)]['repo_name'].unique()

# Filter README.md files for those repos
df_readmes_filtered = df_readmes[df_readmes['sample_repo_name'].isin(no_python_repos)].copy()

# Heuristic for copyright info: look for 'copyright' or '(c)' case-insensitive
pattern = r"copyright|\(c\)"
df_readmes_filtered['has_copyright'] = df_readmes_filtered['content'].str.contains(pattern, case=False, na=False)

num_total = len(df_readmes_filtered)
num_with = int(df_readmes_filtered['has_copyright'].sum())
prop = float(num_with / num_total) if num_total > 0 else None

result = {
  'num_total_non_python_readmes': int(num_total),
  'num_with_copyright': num_with,
  'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_neGRorwxUb0ndRHwV0JzoISe': 'file_storage/call_neGRorwxUb0ndRHwV0JzoISe.json', 'var_call_RFfVxCRkGoUeJLBYO8PMFlHr': 'file_storage/call_RFfVxCRkGoUeJLBYO8PMFlHr.json', 'var_call_9Fsq7P1vKbU2XzrRXE1ckOp5': 'file_storage/call_9Fsq7P1vKbU2XzrRXE1ckOp5.json', 'var_call_wMunXxPaIDfUmVzY42z6MER8': 'file_storage/call_wMunXxPaIDfUmVzY42z6MER8.json'}

exec(code, env_args)
