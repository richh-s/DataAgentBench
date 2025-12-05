code = """import json, pandas as pd
from pathlib import Path

file_path = Path(var_call_pnp94NQ29MHbsJsrCVLX9UB1)
with open(file_path, 'r') as f:
    pkg = json.load(f)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()

file_path2 = Path(var_call_xYek0gsDsC21oGaEvsZCFOyA)
with open(file_path2, 'r') as f:
    projmap = json.load(f)

df_map = pd.DataFrame(projmap)

merged = df_pkg.merge(df_map, on=['System','Name','Version'])
projects = merged[['ProjectName']].drop_duplicates().head(200)

result = projects.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_pnp94NQ29MHbsJsrCVLX9UB1': 'file_storage/call_pnp94NQ29MHbsJsrCVLX9UB1.json', 'var_call_H7yKWyDvT54j0KeHSJeDuet3': ['project_info', 'project_packageversion'], 'var_call_xYek0gsDsC21oGaEvsZCFOyA': 'file_storage/call_xYek0gsDsC21oGaEvsZCFOyA.json'}

exec(code, env_args)
