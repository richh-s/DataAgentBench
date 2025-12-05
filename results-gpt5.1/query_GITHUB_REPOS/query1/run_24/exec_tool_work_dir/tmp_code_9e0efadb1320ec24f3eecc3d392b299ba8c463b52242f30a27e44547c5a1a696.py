code = """import json, pandas as pd

path_contents = var_call_W94TLaaRTrceFmu0eSC77i8r
with open(path_contents, 'r') as f:
    contents = json.load(f)

path_langs = var_call_Mf4c3WMTmqbDjYTKO6q5p3Vl
with open(path_langs, 'r') as f:
    langs = json.load(f)

# Build DataFrames
df_readme = pd.DataFrame(contents)[['repo_name', 'content']]
df_lang = pd.DataFrame(langs)[['repo_name', 'language_description']]

# Identify repos that use Python
df_lang['uses_python'] = df_lang['language_description'].str.contains('Python (', case=False, na=False)

# Keep only repos that do NOT use Python
no_py_repos = set(df_lang.loc[~df_lang['uses_python'], 'repo_name'])

# Filter readmes to no-python repos
filtered = df_readme[df_readme['repo_name'].isin(no_py_repos)].copy()

# Simple substring checks (no regex) on lowercase content
filtered['content_lower'] = filtered['content'].str.lower().fillna('')

keywords = ['copyright', '©', 'all rights reserved']

def has_copyright(text):
    for kw in keywords:
        if kw in text:
            return True
    return False

filtered['has_copyright'] = filtered['content_lower'].apply(copyright)

num_total = int(len(filtered))
num_with = int(filtered['has_copyright'].sum())
prop = float(num_with / num_total) if num_total > 0 else None

import json
result = {
    'num_no_python_repos_with_readme': num_total,
    'num_with_copyright_info': num_with,
    'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_W94TLaaRTrceFmu0eSC77i8r': 'file_storage/call_W94TLaaRTrceFmu0eSC77i8r.json', 'var_call_Mf4c3WMTmqbDjYTKO6q5p3Vl': 'file_storage/call_Mf4c3WMTmqbDjYTKO6q5p3Vl.json'}

exec(code, env_args)
