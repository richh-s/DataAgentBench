code = """import pandas as pd, json
# load query results from storage variables
pkg_latest = pd.read_json(var_call_wTx4WUlrMN0IMwtp8pOPhILg)
proj_pkg = pd.read_json(var_call_dFPubGgWvKq7qBzs9pPNNtw9)
# Ensure types
pkg_latest['Name'] = pkg_latest['Name'].astype(str)
pkg_latest['Version'] = pkg_latest['Version'].astype(str)
proj_pkg['Name'] = proj_pkg['Name'].astype(str)
proj_pkg['Version'] = proj_pkg['Version'].astype(str)
# Merge to get ProjectName for latest packages
merged = pd.merge(pkg_latest, proj_pkg, on=['Name','Version'], how='left')
# Keep only rows with a ProjectName
merged = merged[merged['ProjectName'].notnull()]
# Build mapping list
mapping = merged[['Name','Version','ProjectName']].drop_duplicates().to_dict(orient='records')
# distinct project names
project_names = sorted(list(merged['ProjectName'].dropna().unique()))
result = {'mapping': mapping, 'project_names': project_names}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wTx4WUlrMN0IMwtp8pOPhILg': 'file_storage/call_wTx4WUlrMN0IMwtp8pOPhILg.json', 'var_call_dFPubGgWvKq7qBzs9pPNNtw9': 'file_storage/call_dFPubGgWvKq7qBzs9pPNNtw9.json'}

exec(code, env_args)
