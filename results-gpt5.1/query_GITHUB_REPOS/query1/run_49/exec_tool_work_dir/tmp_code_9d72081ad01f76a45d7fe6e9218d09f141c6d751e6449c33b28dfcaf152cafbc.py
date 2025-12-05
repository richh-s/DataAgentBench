code = """import json, re
import pandas as pd

# Load full README contents from file
path_readmes = var_call_RzvBybYAD9tz8Kep2chdd2bQ
with open(path_readmes, 'r') as f:
    readmes = json.load(f)

# Load full languages data
path_lang = var_call_vK603OKrBWpUFKnatrkR0A6s
with open(path_lang, 'r') as f:
    langs = json.load(f)

# Build DataFrames
readme_df = pd.DataFrame(readmes)
langs_df = pd.DataFrame(langs)

# Normalize columns
readme_df = readme_df.rename(columns={'sample_repo_name':'repo_name'})

# Filter languages to repos that do NOT use Python (case-insensitive search for 'python')
mask_no_python = ~langs_df['language_description'].str.contains('python', case=False, na=False)
no_py_langs = langs_df[mask_no_python][['repo_name']].drop_duplicates()

# Repos with README.md
readme_repos = readme_df[['repo_name','content']].dropna(subset=['content'])

# Restrict to repos that do not use Python
no_py_readmes = readme_repos.merge(no_py_langs, on='repo_name', how='inner')

# Define heuristic for copyright info
pattern = re.compile(r'copyright\s*(?:\u00a9|\(c\)|c)', re.IGNORECASE)

no_py_readmes['has_copyright'] = no_py_readmes['content'].fillna('').apply(lambda t: bool(pattern.search(t)))

# Compute proportion
if len(no_py_readmes) == 0:
    proportion = None
else:
    proportion = float(no_py_readmes['copyright'].sum())

result = {
    'num_no_python_repos_with_readme': int(len(no_py_readmes)),
    'num_with_copyright': int(no_py_readmes['has_copyright'].sum()),
    'proportion': None if len(no_py_readmes)==0 else float(no_py_readmes['has_copyright'].mean())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RzvBybYAD9tz8Kep2chdd2bQ': 'file_storage/call_RzvBybYAD9tz8Kep2chdd2bQ.json', 'var_call_vK603OKrBWpUFKnatrkR0A6s': 'file_storage/call_vK603OKrBWpUFKnatrkR0A6s.json', 'var_call_nAxG3O0uWItBiDDcwti17sJp': 'file_storage/call_nAxG3O0uWItBiDDcwti17sJp.json'}

exec(code, env_args)
