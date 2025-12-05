code = """import json, pandas as pd
from pathlib import Path

proj_pkg_path = Path(var_call_f4LnjOGibCJFwKWjgSXlIFya)
with proj_pkg_path.open() as f:
    proj_pkg = json.load(f)

df = pd.DataFrame(proj_pkg)
cols = df.columns.tolist()

print("__RESULT__:")
print(json.dumps(cols))"""

env_args = {'var_call_igw0vnQyiIWpC8CwsHKHnA96': 'file_storage/call_igw0vnQyiIWpC8CwsHKHnA96.json', 'var_call_gEXA7kVIEwvWGLakqqnPG8rB': ['project_info', 'project_packageversion'], 'var_call_f4LnjOGibCJFwKWjgSXlIFya': 'file_storage/call_f4LnjOGibCJFwKWjgSXlIFya.json', 'var_call_n263Yzq5PfY7My5835HUv9Hm': 'file_storage/call_n263Yzq5PfY7My5835HUv9Hm.json', 'var_call_6L6Yfy4FSZNi3NG65oMJhM7Y': []}

exec(code, env_args)
