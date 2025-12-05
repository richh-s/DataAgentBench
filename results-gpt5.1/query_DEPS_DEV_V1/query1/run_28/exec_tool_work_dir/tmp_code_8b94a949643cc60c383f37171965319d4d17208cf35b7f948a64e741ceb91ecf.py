code = """import json, pandas as pd
from pathlib import Path

pkg_path = Path(var_call_igw0vnQyiIWpC8CwsHKHnA96)
proj_pkg_path = Path(var_call_f4LnjOGibCJFwKWjgSXlIFya)
proj_info_path = Path(var_call_n263Yzq5PfY7My5835HUv9Hm)

with pkg_path.open() as f:
    pkg = json.load(f)
with proj_pkg_path.open() as f:
    proj_pkg = json.load(f)
with proj_info_path.open() as f:
    proj_info_raw = json.load(f)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version','VersionInfo']]

pkg_df['VersionInfo'] = pkg_df['VersionInfo'].apply(lambda x: json.loads(x) if isinstance(x,str) else x)
pkg_df = pkg_df[pkg_df['VersionInfo'].apply(lambda d: d.get('IsRelease', False))]

pkg_df['Ordinal'] = pkg_df['VersionInfo'].apply(lambda d: d.get('Ordinal', 0))
latest_pkg = pkg_df.sort_values('Ordinal', ascending=False).drop_duplicates(subset=['System','Name'], keep='first')
latest_pkg = latest_pkg[['System','Name','Version']]

proj_pkg_df = pd.DataFrame(proj_pkg)
print(proj_pkg_df.columns.tolist())

print("__RESULT__:")
print(json.dumps([]))"""

env_args = {'var_call_igw0vnQyiIWpC8CwsHKHnA96': 'file_storage/call_igw0vnQyiIWpC8CwsHKHnA96.json', 'var_call_gEXA7kVIEwvWGLakqqnPG8rB': ['project_info', 'project_packageversion'], 'var_call_f4LnjOGibCJFwKWjgSXlIFya': 'file_storage/call_f4LnjOGibCJFwKWjgSXlIFya.json', 'var_call_n263Yzq5PfY7My5835HUv9Hm': 'file_storage/call_n263Yzq5PfY7My5835HUv9Hm.json'}

exec(code, env_args)
