code = """import json, pandas as pd
import re

# Load full results from files
import_path_pkg = var_call_Os96Ro0WCvduiy8cpOCYMkJg
import_path_map = var_call_8wuGEJO8RIudYTua4TW33fxX

with open(import_path_pkg, 'r') as f:
    pkg_rows = json.load(f)
with open(import_path_map, 'r') as f:
    map_rows = json.load(f)

pkg_df = pd.DataFrame(pkg_rows)
map_df = pd.DataFrame(map_rows)

# Parse VersionInfo JSON and keep only latest release per (System, Name)
vi = pkg_df['VersionInfo'].apply(json.loads)
pkg_df['IsRelease'] = vi.apply(lambda x: x.get('IsRelease'))
pkg_df['Ordinal'] = vi.apply(lambda x: x.get('Ordinal'))

release_df = pkg_df[pkg_df['IsRelease'] == True].copy()
idx = release_df.groupby(['System','Name'])['Ordinal'].idxmax()
latest_release = release_df.loc[idx, ['System','Name','Version']]

# Join with mapping on System, Name, Version
merged = latest_release.merge(map_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Extract GitHub stars from Project_Information later after joining with project_info via repo name from text
# For now, keep unique ProjectName per package (some may have multiple, just pick first)
merged = merged.sort_values(['System','Name'])
merged_unique = merged.groupby(['System','Name']).first().reset_index()

result = merged_unique.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Os96Ro0WCvduiy8cpOCYMkJg': 'file_storage/call_Os96Ro0WCvduiy8cpOCYMkJg.json', 'var_call_8wuGEJO8RIudYTua4TW33fxX': 'file_storage/call_8wuGEJO8RIudYTua4TW33fxX.json', 'var_call_qHMPZs3KTUwsOFWyf6wAv2tF': 'file_storage/call_qHMPZs3KTUwsOFWyf6wAv2tF.json'}

exec(code, env_args)
