code = """import json, re
import pandas as pd

readmes_file = var_call_waGOrS8vOJWUASXLH36TnVSG
langs_preview = var_call_adTO73xYBUppzKRtxYJoO3Be
readme_paths_preview = var_call_4yTOxVOaJF17GWqqv3rugeGb

with open(readmes_file) as f:
    readmes = json.load(f)

langs = langs_preview

langs_df = pd.DataFrame(langs)

no_py_repos = langs_df[~langs_df['language_description'].str.contains('Python', case=False, na=False)]['repo_name'].unique()
no_py_set = set(no_py_repos)

readmes_df = pd.DataFrame(readmes)

readmes_no_py = readmes_df[readmes_df['sample_repo_name'].isin(no_py_set)].copy()

pattern = re.compile(r'copyright', re.IGNORECASE)

def has_copyright(text):
    if not isinstance(text, str):
        return False
    return bool(pattern.search(text))

readmes_no_py['has_copyright'] = readmes_no_py['content'].apply(has_copyright)

if len(readmes_no_py) == 0:
    proportion = None
else:
    proportion = float(readmes_no_py['has_copyright'].mean())

result = json.dumps({'proportion': proportion, 'total_readmes_non_python_repos': int(len(readmes_no_py))})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_waGOrS8vOJWUASXLH36TnVSG': 'file_storage/call_waGOrS8vOJWUASXLH36TnVSG.json', 'var_call_adTO73xYBUppzKRtxYJoO3Be': 'file_storage/call_adTO73xYBUppzKRtxYJoO3Be.json', 'var_call_GeNCiYH4xwaKVpIoN9acoVDT': 'file_storage/call_GeNCiYH4xwaKVpIoN9acoVDT.json', 'var_call_rov6Bx75SWFq9dJVPEHXqJn1': 'file_storage/call_rov6Bx75SWFq9dJVPEHXqJn1.json', 'var_call_4yTOxVOaJF17GWqqv3rugeGb': 'file_storage/call_4yTOxVOaJF17GWqqv3rugeGb.json'}

exec(code, env_args)
