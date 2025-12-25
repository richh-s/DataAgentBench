code = """import json, pandas as pd
from pathlib import Path

pkg_path = Path(var_call_n3fr0cSupfMtmKEu3WMVfu4k)
proj_pkg_path = Path(var_call_J50VVUBYAG4j8zfysF0OKsl9)

pkg = pd.read_json(pkg_path)
proj_pkg = pd.read_json(proj_pkg_path)

latest = pkg.sort_values('Version').drop_duplicates(['System','Name'], keep='last')
merged = latest.merge(proj_pkg, on=['System','Name','Version'], how='inner')

infos = merged['ProjectName'].unique().tolist()

result = json.dumps({'project_names': infos})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_n3fr0cSupfMtmKEu3WMVfu4k': 'file_storage/call_n3fr0cSupfMtmKEu3WMVfu4k.json', 'var_call_J50VVUBYAG4j8zfysF0OKsl9': 'file_storage/call_J50VVUBYAG4j8zfysF0OKsl9.json'}

exec(code, env_args)
