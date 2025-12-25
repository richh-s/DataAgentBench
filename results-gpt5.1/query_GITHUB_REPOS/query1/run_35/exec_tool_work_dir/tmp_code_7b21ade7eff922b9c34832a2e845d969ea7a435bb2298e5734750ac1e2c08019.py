code = """import json
import pandas as pd

# Load data from storage
non_python_repos = pd.read_json(var_call_9NV6KzC3O3kJkL4xdZOzvDJu)
readmes = pd.read_json(var_call_L4UvU11sAFLm548VZoTEqDT3)

# Filter README.md files to those in non-Python repos
non_py_readmes = readmes[readmes['sample_repo_name'].isin(non_python_repos['repo_name'])].copy()

# Define a simple heuristic for detecting copyright info
patterns = ['copyright', '©', 'copy right', 'all rights reserved']

def has_copyright(text):
    if not isinstance(text, str):
        return False
    lower = text.lower()
    return any(p in lower for p in patterns)

non_py_readmes['has_copyright'] = non_py_readmes['content'].apply(has_copyright)

if len(non_py_readmes) == 0:
    proportion = None
else:
    proportion = float(non_py_readmes['has_copyright'].mean())

result = json.dumps({'proportion': proportion, 'total_non_python_readmes': int(len(non_py_readmes))})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_9NV6KzC3O3kJkL4xdZOzvDJu': 'file_storage/call_9NV6KzC3O3kJkL4xdZOzvDJu.json', 'var_call_L4UvU11sAFLm548VZoTEqDT3': 'file_storage/call_L4UvU11sAFLm548VZoTEqDT3.json'}

exec(code, env_args)
