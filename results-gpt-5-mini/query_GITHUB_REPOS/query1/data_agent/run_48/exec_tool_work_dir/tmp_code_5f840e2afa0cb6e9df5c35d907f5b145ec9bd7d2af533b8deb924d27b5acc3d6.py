code = """import json
import pandas as pd

# load data from previous tool calls stored in variables
# var_call_CfqGzu1TkUDUuj0ndSbJyJ1I is the result file path for the first query
# var_call_6LEjPsM3f4CAffs9vDaVI6cD is the result file path for the second query

with open(var_call_CfqGzu1TkUDUuj0ndSbJyJ1I, 'r') as f:
    data_no_python = json.load(f)

with open(var_call_6LEjPsM3f4CAffs9vDaVI6cD, 'r') as f:
    readmes = json.load(f)

# Create DataFrames
df_no_python = pd.DataFrame(data_no_python)
df_readmes = pd.DataFrame(readmes)

# Normalize repo name column names
# df_no_python has repo_name; df_readmes has sample_repo_name

# Filter readmes to markdown-like files and take content not None
# Consider files with 'readme' in path already queried; but filter content not null and non-binary via repo_data_description

# Keep only text readmes (non-binary) and content not None
mask_text = df_readmes['content'].notnull() & df_readmes['repo_data_description'].str.lower().str.contains('non-binary')
text_readmes = df_readmes[mask_text].copy()

# Lower repo names for safe matching
df_no_python['repo_name'] = df_no_python['repo_name'].str.lower()
text_readmes['sample_repo_name'] = text_readmes['sample_repo_name'].str.lower()

# Keep only readmes from repos that are in the non-python list
merged = text_readmes.merge(df_no_python, left_on='sample_repo_name', right_on='repo_name', how='inner')

# Define a function to detect copyright in content
import re

def has_copyright(text):
    if not isinstance(text, str):
        return False
    # common copyright symbols and patterns
    patterns = [r'\bcopyright\b', r'©', r'\ball rights reserved\b', r'\bcopyright \(c\)\b', r'\bcopyright \(c\)']
    txt = text.lower()
    for p in patterns:
        if re.search(p, txt):
            return True
    return False

merged['has_copyright'] = merged['content'].apply(copyright_text := lambda x: bool(re.search(r"\bcopyright\b|©|\ball rights reserved\b", x.lower()) if isinstance(x, str) else False))

# Now compute proportion among repositories (unique repos) that do not use python
# We need proportion of their README.md files include copyright info.
# Interpret as: among repos (from non-python set) that have at least one README text file in contents, what proportion of those README files include copyright info.

# Count unique repos with at least one readme found
repos_with_readme = merged['sample_repo_name'].nunique()

# Count repos where any README contains copyright
repos_with_copyright = merged.groupby('sample_repo_name')['has_copyright'].any().sum()

# Also compute proportion of README files (file-level) with copyright
total_readme_files = merged.shape[0]
readme_files_with_copyright = merged['has_copyright'].sum()

result = {
    'repos_with_readme': int(repos_with_readme),
    'repos_with_copyright': int(repos_with_copyright),
    'proportion_repos_with_copyright': repos_with_copyright / repos_with_readme if repos_with_readme>0 else None,
    'total_readme_files': int(total_readme_files),
    'readme_files_with_copyright': int(readme_files_with_copyright),
    'proportion_readme_files_with_copyright': readme_files_with_copyright / total_readme_files if total_readme_files>0 else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CfqGzu1TkUDUuj0ndSbJyJ1I': 'file_storage/call_CfqGzu1TkUDUuj0ndSbJyJ1I.json', 'var_call_6LEjPsM3f4CAffs9vDaVI6cD': 'file_storage/call_6LEjPsM3f4CAffs9vDaVI6cD.json'}

exec(code, env_args)
