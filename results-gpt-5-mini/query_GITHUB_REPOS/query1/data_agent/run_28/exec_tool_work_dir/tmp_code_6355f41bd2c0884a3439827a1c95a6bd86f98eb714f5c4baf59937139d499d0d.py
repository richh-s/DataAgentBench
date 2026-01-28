code = """import json
import pandas as pd

# Load the query results from the stored JSON files
with open(var_call_5oMrppJJaUfs7TklL4wzTD8x, 'r') as f:
    non_python_repos = json.load(f)  # list of dicts with 'repo_name'

with open(var_call_tQ5FkNNWffxBzFol5iVkWKmK, 'r') as f:
    readmes = json.load(f)  # list of dicts with 'sample_repo_name', 'content', 'sample_path'

# Create sets and DataFrames
non_python_set = set(r['repo_name'] for r in non_python_repos)
readmes_df = pd.DataFrame(readmes)

# Filter readmes to those belonging to non-python repos
rp = readmes_df[readmes_df['sample_repo_name'].isin(non_python_set)].copy()

# Define function to detect copyright-like text
import re
pattern = re.compile(r"copyright|\u00A9|\(c\)|all rights reserved", flags=re.IGNORECASE)

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

rp['has_copyright'] = rp['content'].apply(has_copyright)

# File-level statistics
total_readme_files_non_python = int(len(rp))
readme_files_with_copyright = int(rp['has_copyright'].sum())
file_level_proportion = None
if total_readme_files_non_python > 0:
    file_level_proportion = readme_files_with_copyright / total_readme_files_non_python

# Repo-level statistics (consider repos that have at least one README in contents)
repos_with_readme = set(rp['sample_repo_name'].unique())
repos_with_copyright = set(rp[rp['has_copyright']]['sample_repo_name'].unique())

total_non_python_repos_with_readme = int(len(repos_with_readme))
repos_with_copyright_in_readme = int(len(repos_with_copyright))
repo_level_proportion = None
if total_non_python_repos_with_readme > 0:
    repo_level_proportion = repos_with_copyright_in_readme / total_non_python_repos_with_readme

# Prepare result dict
result = {
    'total_readme_files_non_python': total_readme_files_non_python,
    'readme_files_with_copyright': readme_files_with_copyright,
    'file_level_proportion': file_level_proportion,
    'total_non_python_repos_with_readme': total_non_python_repos_with_readme,
    'repos_with_copyright_in_readme': repos_with_copyright_in_readme,
    'repo_level_proportion': repo_level_proportion
}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_5oMrppJJaUfs7TklL4wzTD8x': 'file_storage/call_5oMrppJJaUfs7TklL4wzTD8x.json', 'var_call_tQ5FkNNWffxBzFol5iVkWKmK': 'file_storage/call_tQ5FkNNWffxBzFol5iVkWKmK.json'}

exec(code, env_args)
