code = """import json, pandas as pd

# Load full contents result
path_contents = var_call_W94TLaaRTrceFmu0eSC77i8r
with open(path_contents, 'r') as f:
    contents = json.load(f)

# Load full languages result
path_langs = var_call_Mf4c3WMTmqbDjYTKO6q5p3Vl
with open(path_langs, 'r') as f:
    langs = json.load(f)

# Build DataFrames
df_readme = pd.DataFrame(contents)[['repo_name', 'content']]
df_lang = pd.DataFrame(langs)[['repo_name', 'language_description']]

# Identify repos that use Python (language_description contains 'Python (')
df_lang['uses_python'] = df_lang['language_description'].str.contains('Python (', case=False, na=False)

# Keep only repos that do NOT use Python
df_no_py = df_lang[~df_lang['uses_python']][['repo_name']]

# Join with README content
merged = df_no_py.merge(df_readme, on='repo_name', how='inner')

# Define heuristic for "copyright information" in README
patterns = ['copyright', '©', 'all rights reserved']
content_lower = merged['content'].str.lower().fillna('')

has_cr = content_lower.str.contains('|'.join(patterns), na=False)

num_total = int(len(merged))
num_with_cr = int(has_cr.sum())
prop = float(num_with_cr / num_total) if num_total > 0 else None

result = {
    'num_no_python_repos_with_readme': num_total,
    'num_with_copyright_info': num_with_cr,
    'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_W94TLaaRTrceFmu0eSC77i8r': 'file_storage/call_W94TLaaRTrceFmu0eSC77i8r.json', 'var_call_Mf4c3WMTmqbDjYTKO6q5p3Vl': 'file_storage/call_Mf4c3WMTmqbDjYTKO6q5p3Vl.json'}

exec(code, env_args)
