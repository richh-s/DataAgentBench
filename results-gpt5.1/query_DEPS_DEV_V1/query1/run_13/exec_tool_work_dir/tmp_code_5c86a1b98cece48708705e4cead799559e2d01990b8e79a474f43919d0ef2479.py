code = """import json, pandas as pd
import os

# Load full NPM package list from file
path = var_call_IaPCtaNdkDCd1NLG8PLWOOeb
with open(path, 'r') as f:
    npm_packages = json.load(f)

pkg_df = pd.DataFrame(npm_packages)

# Keep only latest version per (System, Name). Assume lexical max of Version approximates latest.
# If Ordinal/IsRelease existed we'd use them, but not selected.
latest_pkg = pkg_df.sort_values('Version').groupby(['System','Name'], as_index=False).tail(1)

result = latest_pkg.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_IaPCtaNdkDCd1NLG8PLWOOeb': 'file_storage/call_IaPCtaNdkDCd1NLG8PLWOOeb.json', 'var_call_ombGlHUWTJ5HLFCdkGbhraJs': ['project_info', 'project_packageversion'], 'var_call_1n32ekisfd9So9lyi46cJH5j': 'file_storage/call_1n32ekisfd9So9lyi46cJH5j.json'}

exec(code, env_args)
