code = """import json, re
import pandas as pd

# Load data
contents_df = pd.read_json(var_call_jXLGcimimjStaVgBKEBluLpi)
languages_df = pd.read_json(var_call_OXxwVtwPkEAAMEMOUiyJtSAu)

# Determine repos that do NOT use Python
mask_no_python = ~languages_df['language_description'].str.contains('Python', case=False, na=False)
no_python_repos = set(languages_df.loc[mask_no_python, 'repo_name'])

# Filter README.md files to those repos
readme_df = contents_df[contents_df['sample_repo_name'].isin(no_python_repos)].copy()

# Define a simple copyright heuristic
pattern = re.compile(r'copyright|\b(c)\b|\u00a9', re.IGNORECASE)

readme_df['has_copyright'] = readme_df['content'].fillna('').apply(lambda x: bool(pattern.search(x)))

total = int(len(readme_df))
with_copyright = int(readme_df['has_copyright'].sum())
proportion = float(with_copyright / total) if total > 0 else None

result = {
    'total_readmes_non_python_repos': total,
    'readmes_with_copyright_info': with_copyright,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_jXLGcimimjStaVgBKEBluLpi': 'file_storage/call_jXLGcimimjStaVgBKEBluLpi.json', 'var_call_OXxwVtwPkEAAMEMOUiyJtSAu': 'file_storage/call_OXxwVtwPkEAAMEMOUiyJtSAu.json'}

exec(code, env_args)
