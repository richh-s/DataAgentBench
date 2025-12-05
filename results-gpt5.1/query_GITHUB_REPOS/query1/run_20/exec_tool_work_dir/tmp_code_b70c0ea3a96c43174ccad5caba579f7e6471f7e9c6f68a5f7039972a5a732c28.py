code = """import json, pandas as pd
from pathlib import Path

# Load full results from files
contents_path = Path(var_call_cFX5rRZSKX4Gr8qHzzvU3iKA)
languages_path = Path(var_call_iIjkoFlKBrOw692UN9alKEke)

with contents_path.open() as f:
    contents = json.load(f)
with languages_path.open() as f:
    languages = json.load(f)

contents_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

# Determine repos that do NOT use Python
mask_no_python = ~languages_df['language_description'].str.contains('Python', case=False, na=False)
no_python_repos = languages_df[mask_no_python]['repo_name'].unique()

# Filter README.md files for those repos
readmes_df = contents_df[contents_df['sample_path'].str.lower() == 'readme.md']
readmes_no_python = readmes_df[readmes_df['sample_repo_name'].isin(no_python_repos)].copy()

# Define a simple heuristic for copyright info
patterns = ['copyright', '©', 'copr.']
content_lower = readmes_no_python['content'].str.lower().fillna('')
mask_copyright = content_lower.apply(lambda txt: any(pat in txt for pat in patterns))

num_repos_no_python = len(no_python_repos)
num_readmes_no_python = len(readmes_no_python)
num_with_copyright = int(mask_copyright.sum())

# Proportion among README.md files for non-Python repos
prop = float(num_with_copyright / num_readmes_no_python) if num_readmes_no_python > 0 else None

result = {
    'num_repos_no_python': int(num_repos_no_python),
    'num_readmes_no_python': int(num_readmes_no_python),
    'num_readmes_with_copyright': int(num_with_copyright),
    'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cFX5rRZSKX4Gr8qHzzvU3iKA': 'file_storage/call_cFX5rRZSKX4Gr8qHzzvU3iKA.json', 'var_call_iIjkoFlKBrOw692UN9alKEke': 'file_storage/call_iIjkoFlKBrOw692UN9alKEke.json'}

exec(code, env_args)
