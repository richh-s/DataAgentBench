code = """import json, pandas as pd
from pathlib import Path

# Load large results
contents_path = Path(var_call_v73IcjQD38OGejT5hOSirchi)
languages_path = Path(var_call_TjIkhhXpejrX6gvUJ8ahzGxo)

contents = json.loads(contents_path.read_text())
languages = json.loads(languages_path.read_text())

contents_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

# Identify repos that do NOT use Python (language_description without 'Python')
no_python_lang = languages_df[~languages_df['language_description'].str.contains('Python', case=False, na=False)]
no_python_repos = set(no_python_lang['repo_name'])

# README.md files
readmes = contents_df[contents_df['sample_path'].str.lower() == 'readme.md']

# Filter to repos without Python
readmes_no_python = readmes[readmes['sample_repo_name'].isin(no_python_repos)].copy()

# Define a simple heuristic for copyright info
patterns = ['copyright', '©', '(c)']
mask = readmes_no_python['content'].str.contains('|'.join(patterns), case=False, na=False)

num_repos = len(readmes_no_python)
num_with_copyright = int(mask.sum())
proportion = float(num_with_copyright) / num_repos if num_repos > 0 else None

result = {
    'num_readmes_non_python': int(num_repos),
    'num_with_copyright': num_with_copyright,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_v73IcjQD38OGejT5hOSirchi': 'file_storage/call_v73IcjQD38OGejT5hOSirchi.json', 'var_call_TjIkhhXpejrX6gvUJ8ahzGxo': 'file_storage/call_TjIkhhXpejrX6gvUJ8ahzGxo.json'}

exec(code, env_args)
