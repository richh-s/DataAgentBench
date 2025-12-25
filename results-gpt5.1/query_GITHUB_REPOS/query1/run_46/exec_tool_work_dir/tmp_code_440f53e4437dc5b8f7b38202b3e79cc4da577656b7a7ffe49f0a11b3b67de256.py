code = """import json, pandas as pd
from pathlib import Path

contents_path = Path(var_call_Zd1qLbtNnqUHlDMY3Y632XK9)
languages_path = Path(var_call_HuXibe9h7IVrQ0rBBi6F4yqA)

with contents_path.open() as f:
    contents = json.load(f)
with languages_path.open() as f:
    languages = json.load(f)

contents_df = pd.DataFrame(contents)
languages_df = pd.DataFrame(languages)

no_python_lang = languages_df[~languages_df['language_description'].str.contains('Python', case=False, na=False)]
no_python_repos = set(no_python_lang['repo_name'])

readmes = contents_df[contents_df['repo_name'].isin(no_python_repos)]

patterns = ['copyright', '\u00a9', 'all rights reserved']

def has_copyright(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    for p in patterns:
        if p in t:
            return True
    return False

readmes = readmes.copy()
readmes['has_copyright'] = readmes['content'].apply(has_copyright)

if len(readmes) == 0:
    proportion = None
else:
    proportion = float(readmes['has_copyright'].mean())

result = {
    'num_no_python_repos_with_readme': int(readmes['repo_name'].nunique()),
    'num_readmes': int(len(readmes)),
    'num_with_copyright': int(readmes['has_copyright'].sum()) if len(readmes) > 0 else 0,
    'proportion': proportion
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Zd1qLbtNnqUHlDMY3Y632XK9': 'file_storage/call_Zd1qLbtNnqUHlDMY3Y632XK9.json', 'var_call_HuXibe9h7IVrQ0rBBi6F4yqA': 'file_storage/call_HuXibe9h7IVrQ0rBBi6F4yqA.json'}

exec(code, env_args)
