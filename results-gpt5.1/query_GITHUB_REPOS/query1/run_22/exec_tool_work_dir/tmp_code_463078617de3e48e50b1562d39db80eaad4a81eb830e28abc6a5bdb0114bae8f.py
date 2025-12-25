code = """import json, pandas as pd
from pathlib import Path

# Load full results
contents_path = Path(var_call_MVTDlJO3aYqiCMTSpVZTdXl6)
languages_path = Path(var_call_YnvhR3PuFiERoOLpGr9EQcFV)

with contents_path.open() as f:
    contents = json.load(f)
with languages_path.open() as f:
    languages = json.load(f)

contents_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

# Filter README.md files and drop rows without content
readme_df = contents_df[contents_df['content'].notna()].copy()

# Determine repos that do NOT use Python based on language_description not containing 'Python'
no_py_lang = languages_df[~languages_df['language_description'].str.contains('Python', case=False, na=False)].copy()

# Restrict READMEs to repos that appear in languages table and do not use Python
readme_no_py = readme_df.merge(no_py_lang, left_on='sample_repo_name', right_on='repo_name', how='inner')

# Define a simple heuristic for detecting copyright info in README content
copyright_patterns = ['copyright', '©', 'copr.', 'all rights reserved']

content_lower = readme_no_py['content'].str.lower().fillna('')
mask = False
for pat in copyright_patterns:
    mask = mask | content_lower.str.contains(pat)

with_copyright = mask.sum()

total = len(readme_no_py)

proportion = float(with_copyright) / total if total > 0 else None

result = {
    'total_readmes_no_python': int(total),
    'readmes_with_copyright_info': int(with_copyright),
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MVTDlJO3aYqiCMTSpVZTdXl6': 'file_storage/call_MVTDlJO3aYqiCMTSpVZTdXl6.json', 'var_call_YnvhR3PuFiERoOLpGr9EQcFV': 'file_storage/call_YnvhR3PuFiERoOLpGr9EQcFV.json'}

exec(code, env_args)
