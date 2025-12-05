code = """import json, pandas as pd
from pathlib import Path

# Load full NPM package list from SQLite result file
file_path = Path(var_call_9InKmcugfYrRQK1YePU2sPLH)
package_records = json.loads(file_path.read_text())

# Load full NPM project_packageversion list from DuckDB result file
file_path2 = Path(var_call_nvbQQd5FtL0OtrvGmbYH7WuB)
ppv_records = json.loads(file_path2.read_text())

pkg_df = pd.DataFrame(package_records)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv_records)
ppv_df = ppv_df[ppv_df['ProjectType']=='GITHUB']

# Determine latest version per NPM package using lexicographic max (best-effort)
latest_pkg = pkg_df.sort_values('Version').groupby('Name', as_index=False).tail(1)

# Join latest packages with project_packageversion on System, Name, Version
merged = latest_pkg.merge(ppv_df, on=['System','Name','Version'], how='inner')

# We now need GitHub stars from project_info.Project_Information
# First, get distinct ProjectName list
projects = merged['ProjectName'].dropna().unique().tolist()

result = json.dumps({'num_latest_packages': int(len(latest_pkg)), 'num_joined': int(len(merged)), 'sample_projects': projects[:20]})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_9InKmcugfYrRQK1YePU2sPLH': 'file_storage/call_9InKmcugfYrRQK1YePU2sPLH.json', 'var_call_M9iyqf5KGXNrVqJpgc6g5FVf': ['project_info', 'project_packageversion'], 'var_call_nvbQQd5FtL0OtrvGmbYH7WuB': 'file_storage/call_nvbQQd5FtL0OtrvGmbYH7WuB.json'}

exec(code, env_args)
