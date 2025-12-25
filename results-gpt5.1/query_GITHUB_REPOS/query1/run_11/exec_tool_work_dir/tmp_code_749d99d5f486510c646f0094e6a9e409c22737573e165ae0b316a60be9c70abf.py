code = """import json, re, pandas as pd

# Load data from storage
readmes_file = var_call_nXvrlBuPfsPwZFhuWgjOiGK1
langs_file = var_call_XKwa6jO58gHG6z7vFDlhBCo8

with open(readmes_file) as f:
    readmes = json.load(f)
with open(langs_file) as f:
    langs = json.load(f)

# DataFrames
df_readmes = pd.DataFrame(readmes)
df_langs = pd.DataFrame(langs)

# Identify repos that use Python
# language_description is natural language, so simple substring match for 'Python' should work
python_repos = df_langs[df_langs['language_description'].str.contains('Python', case=False, na=False)]['repo_name'].unique()
python_repos_set = set(python_repos)

# Repos with README.md
repos_with_readme = df_readmes['repo_name'].unique()

# Non-Python repos with README
non_python_repos_with_readme = [r for r in repos_with_readme if r not in python_repos_set]

# Filter readmes to non-Python repos
df_nonpy_readmes = df_readmes[df_readmes['repo_name'].isin(non_python_repos_with_readme)].copy()

# Simple heuristic for copyright info: look for 'copyright' or '(c)' (common in notices)
pattern = re.compile(r"copyright|\(c\)", re.IGNORECASE)

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

# Determine per-repo if any README.md blob contains copyright info
repo_group = df_nonpy_readmes.groupby('repo_name')['content']
repo_has_copyright = repo_group.apply(lambda series: any(copyright(text) if False else any(pattern.search(t or '') for t in series)))

# Compute proportion
num_repos = len(non_python_repos_with_readme)
num_with_copyright = int(repo_has_copyright.sum())
proportion = float(num_with_copyright) / num_repos if num_repos else None

result = {
    'non_python_repos_with_readme_count': int(num_repos),
    'non_python_repos_with_copyright_readme_count': int(num_with_copyright),
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nXvrlBuPfsPwZFhuWgjOiGK1': 'file_storage/call_nXvrlBuPfsPwZFhuWgjOiGK1.json', 'var_call_XKwa6jO58gHG6z7vFDlhBCo8': 'file_storage/call_XKwa6jO58gHG6z7vFDlhBCo8.json', 'var_call_GXEAkbyXIlVAjb9HPqNbNmkX': 'file_storage/call_GXEAkbyXIlVAjb9HPqNbNmkX.json', 'var_call_toDw1VdvgwTOVWbWBY4Qdx70': 'file_storage/call_toDw1VdvgwTOVWbWBY4Qdx70.json', 'var_call_qv8cN9iEOa3nDRHaNYaAshsH': 'file_storage/call_qv8cN9iEOa3nDRHaNYaAshsH.json', 'var_call_lzhCouq57r3whHO3FugKDBRq': 'file_storage/call_lzhCouq57r3whHO3FugKDBRq.json', 'var_call_IWsrbMiWBzFQLCjZuXqrNPiu': 'file_storage/call_IWsrbMiWBzFQLCjZuXqrNPiu.json'}

exec(code, env_args)
