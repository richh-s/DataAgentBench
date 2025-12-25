code = """import json, pandas as pd
contents = var_call_4IJltxHE3dzyfT95Siogj0R1
languages = var_call_PLsmQ75lYbUCyaPGNy7WZfc5

if isinstance(contents, str):
    with open(contents) as f:
        contents = json.load(f)
if isinstance(languages, str):
    with open(languages) as f:
        languages = json.load(f)

c_df = pd.DataFrame(contents)
l_df = pd.DataFrame(languages)

l_df['has_python'] = l_df['language_description'].str.contains('Python', case=False, na=False)
non_py_repos = set(l_df.loc[~l_df['has_python'], 'repo_name'])

readmes = c_df.copy()
readmes = readmes[readmes['sample_repo_name'].isin(non_py_repos)]

readmes['has_copyright'] = readmes['content'].str.contains('copyright', case=False, na=False)

total = len(readmes)
with_c = int(readmes['has_copyright'].sum())
prop = with_c / total if total else None

result = json.dumps({'total_non_python_readmes': total, 'with_copyright': with_c, 'proportion': prop})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_4IJltxHE3dzyfT95Siogj0R1': 'file_storage/call_4IJltxHE3dzyfT95Siogj0R1.json', 'var_call_PLsmQ75lYbUCyaPGNy7WZfc5': 'file_storage/call_PLsmQ75lYbUCyaPGNy7WZfc5.json'}

exec(code, env_args)
