code = """import json, pandas as pd
import os

# Load full NPM packageinfo result from file
path = var_call_mBcTaighfX24tg0V9FeH4frF
with open(path, 'r') as f:
    npm_packages = json.load(f)

pkg_df = pd.DataFrame(npm_packages)

# Parse VersionInfo JSON and filter IsRelease == true
pkg_df['VersionInfo_parsed'] = pkg_df['VersionInfo'].apply(lambda x: json.loads(x) if isinstance(x, str) and x.strip() else {})
pkg_df['IsRelease'] = pkg_df['VersionInfo_parsed'].apply(lambda d: d.get('IsRelease'))

# Parse Licenses JSON-like array and check for 'MIT'
def has_mit(lic_str):
    if not isinstance(lic_str, str) or not lic_str.strip():
        return False
    try:
        arr = json.loads(lic_str)
        return any(str(item).upper() == 'MIT' for item in arr)
    except Exception:
        return False

pkg_df['HasMIT'] = pkg_df['Licenses'].apply(has_mit)

filtered_pkg = pkg_df[(pkg_df['IsRelease'] == True) & (pkg_df['HasMIT'])][['System','Name','Version']].drop_duplicates()

result = filtered_pkg.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_mBcTaighfX24tg0V9FeH4frF': 'file_storage/call_mBcTaighfX24tg0V9FeH4frF.json', 'var_call_sZ7hMHoyXjzPnTRx38FRTl5r': ['project_info', 'project_packageversion'], 'var_call_WjbkaoVw80VuuTC5kxhRsmkI': 'file_storage/call_WjbkaoVw80VuuTC5kxhRsmkI.json'}

exec(code, env_args)
