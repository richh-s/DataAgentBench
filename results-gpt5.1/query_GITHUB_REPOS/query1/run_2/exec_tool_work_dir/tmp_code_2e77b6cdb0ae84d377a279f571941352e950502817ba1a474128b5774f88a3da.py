code = """import json, pandas as pd
from pathlib import Path

# Load full results from JSON files
contents_path = Path(var_call_06v0B3d8GHEMTTGnyrcgxsHG)
languages_path = Path(var_call_pOC75Yb2eeLk4eBe0zuFIi4g)

contents = json.loads(contents_path.read_text())
languages = json.loads(languages_path.read_text())

contents_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

# Determine repos that use Python (language_description contains 'Python (')
python_repos = set(languages_df[languages_df['language_description'].str.contains('Python (', case=False, na=False)]['repo_name'])

# Filter README.md files for repos that do NOT use Python
readme_df = contents_df[contents_df['sample_path'] == 'README.md']
non_python_readme_df = readme_df[~readme_df['sample_repo_name'].isin(python_repos)]

# Define a simple heuristic for copyright info: look for 'copyright' or '©'
pattern = r'(?i)copyright|\u00a9'

has_copyright = non_python_readme_df['content'].fillna('').str.contains(pattern, regex=True)

num_non_python_readmes = len(non_python_readme_df)
num_with_copyright = int(copyright.sum()) if (copyright := has_copyright) is not None else 0

proportion = float(num_with_copyright) / num_non_python_readmes if num_non_python_readmes > 0 else None

result = {
    'num_non_python_readmes': int(num_non_python_readmes),
    'num_with_copyright': int(num_with_copyright),
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_06v0B3d8GHEMTTGnyrcgxsHG': 'file_storage/call_06v0B3d8GHEMTTGnyrcgxsHG.json', 'var_call_pOC75Yb2eeLk4eBe0zuFIi4g': 'file_storage/call_pOC75Yb2eeLk4eBe0zuFIi4g.json'}

exec(code, env_args)
