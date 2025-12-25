code = """import json, pandas as pd

# Load full NPM packageinfo result
path_pkg = var_call_yVihHw8OryaPo0wdoSVFAjNi
with open(path_pkg, 'r') as f:
    pkg = json.load(f)

pkg_df = pd.DataFrame(pkg)

# Filter MIT license and IsRelease true
import ast

def has_mit(licenses_str):
    try:
        arr = ast.literal_eval(licenses_str) if isinstance(licenses_str, str) else []
        return any(str(x).strip().upper() == 'MIT' for x in arr)
    except Exception:
        return False

def is_release(vinfo_str):
    try:
        obj = ast.literal_eval(vinfo_str) if isinstance(vinfo_str, str) else {}
        return bool(obj.get('IsRelease'))
    except Exception:
        return False

pkg_df = pkg_df[pkg_df['Licenses'].apply(has_mit) & pkg_df['VersionInfo'].apply(is_release)]

# Load project_packageversion for NPM
path_ppv = var_call_XpBNYaDrfdSqpqKA3XzG1dSK
with open(path_ppv, 'r') as f:
    ppv = json.load(f)
ppv_df = pd.DataFrame(ppv)
ppv_df = ppv_df[ppv_df['ProjectType'] == 'GITHUB']

# Join on System, Name, Version
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Extract ProjectName list
projects = merged['ProjectName'].dropna().unique().tolist()

result = json.dumps(projects[:500])
print('__RESULT__:')
print(result)"""

env_args = {'var_call_yVihHw8OryaPo0wdoSVFAjNi': 'file_storage/call_yVihHw8OryaPo0wdoSVFAjNi.json', 'var_call_hLGwiIiy4m9TB8RgRsUNwI2T': ['project_info', 'project_packageversion'], 'var_call_XpBNYaDrfdSqpqKA3XzG1dSK': 'file_storage/call_XpBNYaDrfdSqpqKA3XzG1dSK.json', 'var_call_E0lfntVbjWdb2k9Lr3FsIhDv': 'file_storage/call_E0lfntVbjWdb2k9Lr3FsIhDv.json'}

exec(code, env_args)
