code = """import json, pandas as pd
from pathlib import Path

contents_path = Path(var_call_uKO1zIZxUy9IGGQrSqLpU896)
languages_path = Path(var_call_TjIkhhXpejrX6gvUJ8ahzGxo)

contents = json.loads(contents_path.read_text())
languages = json.loads(languages_path.read_text())

readmes_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

# Repos that do NOT use Python
no_python_lang = languages_df[~languages_df['language_description'].str.contains('Python', case=False, na=False)]
no_python_repos = set(no_python_lang['repo_name'])

# Filter README.md files to those repos
readmes_no_python = readmes_df[readmes_df['sample_repo_name'].isin(no_python_repos)].copy()

patterns = ['copyright', '©', '(c)']
mask = readmes_no_python['content'].str.contains('|'.join(patterns), case=False, na=False)

num_readmes = int(len(readmes_no_python))
num_with = int(mask.sum())
prop = float(num_with) / num_readmes if num_readmes > 0 else None

result = {"num_readmes_non_python": num_readmes, "num_with_copyright": num_with, "proportion": prop}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_v73IcjQD38OGejT5hOSirchi': 'file_storage/call_v73IcjQD38OGejT5hOSirchi.json', 'var_call_TjIkhhXpejrX6gvUJ8ahzGxo': 'file_storage/call_TjIkhhXpejrX6gvUJ8ahzGxo.json', 'var_call_uKO1zIZxUy9IGGQrSqLpU896': 'file_storage/call_uKO1zIZxUy9IGGQrSqLpU896.json'}

exec(code, env_args)
