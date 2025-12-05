code = """import json, pandas as pd

# Load full NPM package list
with open(var_call_BFLomqnIRVvA4BjveUhoTNXX, 'r') as f:
    npm_pkgs = json.load(f)

# Convert to DataFrame
pkg_df = pd.DataFrame(npm_pkgs)

# Keep only latest version per (System, Name)
# Assuming Version is sortable lexicographically for latest; if Ordinal existed we'd use it, but it's not selected.
pkg_df_sorted = pkg_df.sort_values(['System', 'Name', 'Version'])
latest_pkg_df = pkg_df_sorted.groupby(['System', 'Name'], as_index=False).tail(1)

result = latest_pkg_df[['System','Name','Version']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_BFLomqnIRVvA4BjveUhoTNXX': 'file_storage/call_BFLomqnIRVvA4BjveUhoTNXX.json', 'var_call_m9WhF5Har4VXBEpDM9NrHHVB': ['project_info', 'project_packageversion'], 'var_call_TI6QZntnSRfKQPPImVocHi1C': 'file_storage/call_TI6QZntnSRfKQPPImVocHi1C.json'}

exec(code, env_args)
