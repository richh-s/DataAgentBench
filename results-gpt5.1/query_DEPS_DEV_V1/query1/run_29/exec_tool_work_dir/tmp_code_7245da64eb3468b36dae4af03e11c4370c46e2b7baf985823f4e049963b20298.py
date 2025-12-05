code = """import json, pandas as pd

# load latest NPM packages
with open(var_call_thUZGQO7cklBnqSPETgcLstB, 'r') as f:
    latest_pkgs = json.load(f)
latest_df = pd.DataFrame(latest_pkgs)

# load NPM project-package mappings
with open(var_call_TI6QZntnSRfKQPPImVocHi1C, 'r') as f:
    proj_pkg = json.load(f)
pp_df = pd.DataFrame(proj_pkg)

# join latest packages with project mappings on System, Name, Version
merged = latest_df.merge(pp_df, on=['System','Name','Version'], how='inner')

# get distinct ProjectNames
projects = merged['ProjectName'].dropna().unique().tolist()

# prepare result (limited list of project names to query later)
result = projects

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_BFLomqnIRVvA4BjveUhoTNXX': 'file_storage/call_BFLomqnIRVvA4BjveUhoTNXX.json', 'var_call_m9WhF5Har4VXBEpDM9NrHHVB': ['project_info', 'project_packageversion'], 'var_call_TI6QZntnSRfKQPPImVocHi1C': 'file_storage/call_TI6QZntnSRfKQPPImVocHi1C.json', 'var_call_thUZGQO7cklBnqSPETgcLstB': 'file_storage/call_thUZGQO7cklBnqSPETgcLstB.json'}

exec(code, env_args)
