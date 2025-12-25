code = """import json, pandas as pd

readmes_file = var_call_UqPUmlK7HdquqSbO67nvcwpl
langs_file = var_call_VMOnRGkMt2Au5tjWZnFRcuZ2

readmes = pd.read_json(readmes_file)
langs = pd.read_json(langs_file)

# repos that do NOT use Python (language_description does not contain 'Python')
no_py_repos = langs[~langs['language_description'].str.contains('Python', case=False, na=False)]['repo_name'].unique()
no_py_repos_set = set(no_py_repos)

# README.md files and their repos
readmes['has_copyright'] = readmes['content'].str.contains('copyright', case=False, na=False) | readmes['content'].str.contains('©', na=False)

# filter to readmes whose repo is in languages table
readmes = readmes[readmes['sample_repo_name'].isin(langs['repo_name'])]

# among those, restrict to repos that do NOT use Python
readmes_no_py = readmes[readmes['sample_repo_name'].isin(no_py_repos_set)]

if len(readmes_no_py) == 0:
    proportion = None
else:
    proportion = float(readmes_no_py['has_copyright'].mean())

result = json.dumps({"proportion_non_python_readmes_with_copyright": proportion})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_UqPUmlK7HdquqSbO67nvcwpl': 'file_storage/call_UqPUmlK7HdquqSbO67nvcwpl.json', 'var_call_VMOnRGkMt2Au5tjWZnFRcuZ2': 'file_storage/call_VMOnRGkMt2Au5tjWZnFRcuZ2.json', 'var_call_Zylvr87bQxHKfEqdGUGt4uhg': 'file_storage/call_Zylvr87bQxHKfEqdGUGt4uhg.json', 'var_call_kJI87aUU8Vp35EwxBmCIjTPj': 'file_storage/call_kJI87aUU8Vp35EwxBmCIjTPj.json', 'var_call_T6uAWazbRSFosrUGGJjLhzBb': 'file_storage/call_T6uAWazbRSFosrUGGJjLhzBb.json', 'var_call_GjRhvCpO3vAXMnEYXrmZm97O': 'file_storage/call_GjRhvCpO3vAXMnEYXrmZm97O.json', 'var_call_7QS5mKplDKp4FgECJhWD6o7w': 'file_storage/call_7QS5mKplDKp4FgECJhWD6o7w.json'}

exec(code, env_args)
