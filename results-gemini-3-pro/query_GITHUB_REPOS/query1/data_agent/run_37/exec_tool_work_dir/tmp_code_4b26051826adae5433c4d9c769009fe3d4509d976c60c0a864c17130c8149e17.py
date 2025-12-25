code = """import json
import pandas as pd

# Load languages
with open(locals()['var_function-call-9290647314051344641'], 'r') as f:
    languages_data = json.load(f)

df_lang = pd.DataFrame(languages_data)

# Filter non-python repos
# Check if "Python" is in language_description
def uses_python(desc):
    if not desc: return False
    return "Python" in desc

non_python_repos = set(df_lang[~df_lang['language_description'].apply(uses_python)]['repo_name'])

# Load contents (READMEs)
with open(locals()['var_function-call-9290647314051345500'], 'r') as f:
    contents_data = json.load(f)

df_contents = pd.DataFrame(contents_data)

# Ensure strictly README.md filename (checking basename)
# The SQL query used LIKE '%README.md', which might include 'MyREADME.md'
def is_exact_readme(path):
    if not path: return False
    return path.split('/')[-1] == 'README.md'

df_contents = df_contents[df_contents['sample_path'].apply(is_exact_readme)]

# Filter for non-python repos
df_contents_filtered = df_contents[df_contents['sample_repo_name'].isin(non_python_repos)].copy()

# Calculate proportion
# Convert has_copyright to int
df_contents_filtered['has_copyright'] = df_contents_filtered['has_copyright'].astype(int)

total_readmes = len(df_contents_filtered)
copyright_readmes = df_contents_filtered['has_copyright'].sum()

proportion = 0.0
if total_readmes > 0:
    proportion = copyright_readmes / total_readmes

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-9290647314051344641': 'file_storage/function-call-9290647314051344641.json', 'var_function-call-9290647314051345500': 'file_storage/function-call-9290647314051345500.json'}

exec(code, env_args)
