code = """import json, pandas as pd, re

# load latest NPM package versions
path_latest = var_call_k7fTG0DADa9BlcxEkolQSVLZ
with open(path_latest) as f:
    latest = pd.DataFrame(json.load(f))

# load NPM GitHub project mappings
path_pkgproj = var_call_MaFRQXk2ytbZgVdx1cnXHz1b
with open(path_pkgproj) as f:
    pkgproj = pd.DataFrame(json.load(f))

# keep only mappings for latest versions
merged = pkgproj.merge(latest, on=['System','Name','Version'], how='inner')

# read project_info table to get star counts embedded in Project_Information
# We'll query all rows via SQL separately, but here assume it's passed as var_call_project_info

print("__RESULT__:")
print(json.dumps({"count_latest": int(len(latest)), "count_mapped": int(len(merged))}))"""

env_args = {'var_call_dPgVOSdxo3BEWb3C9qHFSwGZ': 'file_storage/call_dPgVOSdxo3BEWb3C9qHFSwGZ.json', 'var_call_zcurF4o6Wv4G3zX2pC4DFbCU': ['project_info', 'project_packageversion'], 'var_call_MaFRQXk2ytbZgVdx1cnXHz1b': 'file_storage/call_MaFRQXk2ytbZgVdx1cnXHz1b.json', 'var_call_k7fTG0DADa9BlcxEkolQSVLZ': 'file_storage/call_k7fTG0DADa9BlcxEkolQSVLZ.json'}

exec(code, env_args)
