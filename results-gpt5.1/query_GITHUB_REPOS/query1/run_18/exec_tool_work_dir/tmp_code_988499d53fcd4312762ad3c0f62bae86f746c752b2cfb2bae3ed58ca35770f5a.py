code = """import json, pandas as pd

non_py_repos_file = var_call_s900LPkQtmCopfTIUAhLXfv9
readmes_file = var_call_FwDBvirP6V2wLlFoOp6VtrNj

non_py_repos = pd.read_json(non_py_repos_file)
readmes = pd.read_json(readmes_file)

readmes = readmes[readmes['sample_path'].str.lower() == 'readme.md']

non_py_set = set(non_py_repos['repo_name'])
readmes_non_py = readmes[readmes['sample_repo_name'].isin(non_py_set)]

readmes_non_py = readmes_non_py.drop_duplicates(subset=['sample_repo_name'])

contains_copyright = readmes_non_py['content'].str.contains('copyright', case=False, na=False)

proportion = float(contains_copyright.sum()) / float(len(readmes_non_py)) if len(readmes_non_py) > 0 else None

result = json.dumps({'proportion': proportion, 'total_non_python_repos_with_readme': int(len(readmes_non_py)), 'count_with_copyright': int(contains_copyright.sum())})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_s900LPkQtmCopfTIUAhLXfv9': 'file_storage/call_s900LPkQtmCopfTIUAhLXfv9.json', 'var_call_FwDBvirP6V2wLlFoOp6VtrNj': 'file_storage/call_FwDBvirP6V2wLlFoOp6VtrNj.json'}

exec(code, env_args)
