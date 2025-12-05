code = """import json, pandas as pd
import re

with open(var_call_hKbGwPDBSvpBdtv8wxc1ndH0) as f:
    readme_exact = json.load(f)
with open(var_call_1KZvRzaeB7GOGDpaFniZFYxc) as f:
    readme_like = json.load(f)
with open(var_call_wnpChL5X3shHn7gw9tkPA3Dr) as f:
    lang_rows = json.load(f)

readmes = pd.DataFrame(readme_like)
readmes['path_lower'] = readmes['sample_path'].str.lower()
readmes = readmes[readmes['path_lower'].str.endswith('readme.md')]

langs = pd.DataFrame(lang_rows)
langs['has_python'] = langs['language_description'].str.contains('Python', case=False, na=False)

non_py_repos = set(langs.loc[~langs['has_python'], 'repo_name'].unique())

readmes_non_py = readmes[readmes['sample_repo_name'].isin(non_py_repos)].copy()

pattern = re.compile(r"copyright|\(c\) \d{4}|©", re.IGNORECASE)

def has_copyright_fn(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

readmes_non_py['has_copyright'] = readmes_non_py['content'].apply(has_copyright_fn)

total = int(len(readmes_non_py))
with_copyright = int(readmes_non_py['has_copyright'].sum())
proportion = with_copyright / total if total > 0 else None

result = {
    'total_non_python_readmes': total,
    'with_copyright': with_copyright,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_hKbGwPDBSvpBdtv8wxc1ndH0': 'file_storage/call_hKbGwPDBSvpBdtv8wxc1ndH0.json', 'var_call_wnpChL5X3shHn7gw9tkPA3Dr': 'file_storage/call_wnpChL5X3shHn7gw9tkPA3Dr.json', 'var_call_4BVvVrfPzmPalbfIvT3HRLEH': 'file_storage/call_4BVvVrfPzmPalbfIvT3HRLEH.json', 'var_call_v1Fx2fZmL8Hcn7JTgGo0uW5E': 'file_storage/call_v1Fx2fZmL8Hcn7JTgGo0uW5E.json', 'var_call_aJGCjIbEQLUMWArhrHaEbKO3': 'file_storage/call_aJGCjIbEQLUMWArhrHaEbKO3.json', 'var_call_1KZvRzaeB7GOGDpaFniZFYxc': 'file_storage/call_1KZvRzaeB7GOGDpaFniZFYxc.json'}

exec(code, env_args)
