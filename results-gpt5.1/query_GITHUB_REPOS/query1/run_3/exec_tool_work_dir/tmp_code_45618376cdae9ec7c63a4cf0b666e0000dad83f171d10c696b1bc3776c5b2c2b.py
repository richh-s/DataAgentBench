code = """import pandas as pd, json

readmes_path = var_call_7vdV3owndFC0oQbf4a17ryGD
langs_path = var_call_lr45Otjrse1M17kJnJTt1pBF
repos_with_langs_path = var_call_YjGZjRT0xbb0GxKoJPDPfr6X
all_artifact_repos_path = var_call_ISI7JcQQSmeOJiN3JbUdF4t0
repos_table_path = var_call_2VVWYKlcIdzzZ8ekDLdy9ufw
licenses_table_path = var_call_OKFholfYOEMIZei3ypTur2bE

import os, json

def load(path):
    if isinstance(path, str) and os.path.isfile(path):
        with open(path) as f:
            return json.load(f)
    return path

readmes = load(readmes_path)
langs = load(langs_path)

# Determine repos that do not use Python
langs_df = pd.DataFrame(langs)
langs_df['uses_python'] = langs_df['language_description'].str.contains('Python', case=False, na=False)

# For repos absent from languages table, we cannot know languages; exclude them
non_python_repos = langs_df[~langs_df['uses_python']]['repo_name'].unique()

readmes_df = pd.DataFrame(readmes)

# restrict to non-python repos
readmes_non_py = readmes_df[readmes_df['repo_name'].isin(non_python_repos)].copy()

# simple heuristic for copyright info
patterns = ['copyright', '©', 'copyleft', 'all rights reserved']
pat = '|'.join(patterns)
readmes_non_py['has_copyright'] = readmes_non_py['content'].str.contains(pat, case=False, na=False)

if len(readmes_non_py)==0:
    result = {"proportion": None, "note": "No README.md files for non-Python repos in dataset"}
else:
    proportion = float(readmes_non_py['has_copyright'].mean())
    result = {"proportion": proportion, "numerator": int(readmes_non_py['has_copyright'].sum()), "denominator": int(len(readmes_non_py))}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7vdV3owndFC0oQbf4a17ryGD': 'file_storage/call_7vdV3owndFC0oQbf4a17ryGD.json', 'var_call_lr45Otjrse1M17kJnJTt1pBF': 'file_storage/call_lr45Otjrse1M17kJnJTt1pBF.json', 'var_call_ISI7JcQQSmeOJiN3JbUdF4t0': 'file_storage/call_ISI7JcQQSmeOJiN3JbUdF4t0.json', 'var_call_YjGZjRT0xbb0GxKoJPDPfr6X': 'file_storage/call_YjGZjRT0xbb0GxKoJPDPfr6X.json', 'var_call_OKFholfYOEMIZei3ypTur2bE': 'file_storage/call_OKFholfYOEMIZei3ypTur2bE.json', 'var_call_2VVWYKlcIdzzZ8ekDLdy9ufw': 'file_storage/call_2VVWYKlcIdzzZ8ekDLdy9ufw.json'}

exec(code, env_args)
