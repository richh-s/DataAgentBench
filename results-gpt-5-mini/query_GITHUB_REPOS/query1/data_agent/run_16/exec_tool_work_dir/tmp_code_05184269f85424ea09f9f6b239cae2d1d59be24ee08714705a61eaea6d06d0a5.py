code = """import json, re
import pandas as pd

# Load the large JSON results from previous tool calls (file paths provided as variables)
with open(var_call_dLyvzASXin9iZpNgMEz0NoFO, 'r', encoding='utf-8') as f:
    languages = json.load(f)
with open(var_call_qih05ke9OfpE3LK9HUbDd8L3, 'r', encoding='utf-8') as f:
    readmes = json.load(f)

# DataFrames
lang_df = pd.DataFrame(languages)
readme_df = pd.DataFrame(readmes)

# Normalize column names
lang_df['language_description'] = lang_df['language_description'].fillna('').astype(str)

# Identify repos that do NOT use Python (case-insensitive search in language_description)
lang_df['has_python'] = lang_df['language_description'].str.lower().str.contains('python')
non_python_repos = set(lang_df.loc[~lang_df['has_python'], 'repo_name'].unique())

# Filter README files to those belonging to non-Python repos
readme_df['sample_repo_name'] = readme_df['sample_repo_name'].astype(str)
readme_df['content'] = readme_df['content'].fillna('').astype(str)

# Ensure we only consider README.md files (some paths may include READMEs in subdirs)
readme_df['path_lower'] = readme_df['sample_path'].astype(str).str.lower()
readme_mask = readme_df['path_lower'].str.endswith('readme.md')
readme_df = readme_df[readme_mask]

# Filter to non-Python repos
nonpy_readmes = readme_df[readme_df['sample_repo_name'].isin(non_python_repos)].copy()

# Define a function to detect copyright-like text
cpy_regex = re.compile(r"copyright|\u00A9|\(c\)|all rights reserved", re.IGNORECASE)
nonpy_readmes['has_copyright'] = nonpy_readmes['content'].apply(lambda c: bool(cpy_regex.search(c)))

# Compute counts
total_readme_files = int(len(nonpy_readmes))
readme_with_copyright = int(nonpy_readmes['has_copyright'].sum())

# Also compute distinct repos considered and how many of those repos have at least one README with copyright
distinct_repos = int(nonpy_readmes['sample_repo_name'].nunique())
repos_with_copyright = int(nonpy_readmes.groupby('sample_repo_name')['has_copyright'].any().sum())

proportion_files = None
if total_readme_files > 0:
    proportion_files = readme_with_copyright / total_readme_files

result = {
    'total_readme_files_in_non_python_repos': total_readme_files,
    'readme_files_with_copyright': readme_with_copyright,
    'proportion_of_readme_files_with_copyright': proportion_files,
    'distinct_non_python_repos_with_readme': distinct_repos,
    'distinct_non_python_repos_with_readme_and_copyright': repos_with_copyright
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dLyvzASXin9iZpNgMEz0NoFO': 'file_storage/call_dLyvzASXin9iZpNgMEz0NoFO.json', 'var_call_qih05ke9OfpE3LK9HUbDd8L3': 'file_storage/call_qih05ke9OfpE3LK9HUbDd8L3.json'}

exec(code, env_args)
