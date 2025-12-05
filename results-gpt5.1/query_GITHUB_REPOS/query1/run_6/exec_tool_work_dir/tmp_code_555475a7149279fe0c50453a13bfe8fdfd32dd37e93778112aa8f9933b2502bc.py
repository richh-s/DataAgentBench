code = """import json, pandas as pd, re

# var_call_qt2x9bZo87Gd0XmtuE7GuoDp is a JSON file path
with open(var_call_qt2x9bZo87Gd0XmtuE7GuoDp, 'r') as f:
    contents = json.load(f)
readmes = pd.DataFrame(contents)[['sample_repo_name','content']].dropna()

langs = pd.DataFrame(var_call_UmEX1zFe23Jsg0tGwTMEGBp5)
py_repos = pd.DataFrame(var_call_TXLQtAotZjIdzkxBbvzXMEuF)

py_set = set(py_repos['repo_name'])

non_py = readmes[~readmes['sample_repo_name'].isin(py_set)].copy()

pattern = re.compile(r'copyright', re.IGNORECASE)
non_py['has_copyright'] = non_py['content'].astype(str).apply(lambda x: bool(pattern.search(x)))

prop = float(non_py['has_copyright'].mean()) if len(non_py) else None

result = {'total_non_python_readmes': int(len(non_py)),
          'with_copyright_info': int(non_py['has_copyright'].sum()),
          'proportion': prop}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_qt2x9bZo87Gd0XmtuE7GuoDp': 'file_storage/call_qt2x9bZo87Gd0XmtuE7GuoDp.json', 'var_call_UmEX1zFe23Jsg0tGwTMEGBp5': 'file_storage/call_UmEX1zFe23Jsg0tGwTMEGBp5.json', 'var_call_TXLQtAotZjIdzkxBbvzXMEuF': 'file_storage/call_TXLQtAotZjIdzkxBbvzXMEuF.json'}

exec(code, env_args)
