code = """import json, pandas as pd
from pathlib import Path

# Load full results
contents_path = Path(var_call_34HHhLcljg18vrjUFGxyzDJW)
languages_path = Path(var_call_EHN3wv6vZsbUSfJUEgkvef8J)

contents = json.loads(contents_path.read_text())
languages = json.loads(languages_path.read_text())

contents_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

# Repos without Python
mask_no_python = ~languages_df['language_description'].str.contains('Python', case=False, na=False)
no_python_repos = languages_df.loc[mask_no_python, 'repo_name'].unique()

readmes = contents_df[contents_df['sample_repo_name'].isin(no_python_repos)].copy()

# Heuristic: README contains copyright info if it has word 'copyright' or '©' or 'opyright (c)' etc.
pattern = r'(copyright\b|\(c\)|©)'
readmes['has_copyright'] = readmes['content'].str.contains(pattern, case=False, regex=True, na=False)

# Compute proportion
if len(readmes) == 0:
    proportion = None
else:
    proportion = float(readmes['copyright'].sum()) / float(len(readmes))

result = {
    'num_no_python_readmes': int(len(readmes)),
    'num_with_copyright': int(readmes['has_copyright'].sum()),
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_34HHhLcljg18vrjUFGxyzDJW': 'file_storage/call_34HHhLcljg18vrjUFGxyzDJW.json', 'var_call_EHN3wv6vZsbUSfJUEgkvef8J': 'file_storage/call_EHN3wv6vZsbUSfJUEgkvef8J.json'}

exec(code, env_args)
