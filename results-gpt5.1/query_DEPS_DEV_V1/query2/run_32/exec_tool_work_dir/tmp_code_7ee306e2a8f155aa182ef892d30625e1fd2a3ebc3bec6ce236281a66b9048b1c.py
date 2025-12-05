code = """import json, pandas as pd
from pathlib import Path

pkg_file = var_call_uR08p5mkTqrbVPrBijEQ2YVS
pkg_rows = json.loads(Path(pkg_file).read_text())
pkg_df = pd.DataFrame(pkg_rows)

proj_pkg_rows = json.loads(Path(var_call_IJfquksVbtcaMOIRxFtN9NCK).read_text())
proj_pkg_df = pd.DataFrame(proj_pkg_rows)

# Join to retain only MIT release NPM packages that have a GitHub project mapping
merged = pkg_df.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

# Get unique project names
projects = merged['ProjectName'].dropna().unique().tolist()

# Build IN clause for project_info
values = [f"'{p.replace("'","''")}'" for p in projects]
if not values:
    result = None
else:
    in_clause = ', '.join(values[:10000])
    query = f"SELECT Project_Information FROM project_info WHERE Project_Information IN ({in_clause});"
    result = query

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uR08p5mkTqrbVPrBijEQ2YVS': 'file_storage/call_uR08p5mkTqrbVPrBijEQ2YVS.json', 'var_call_IFv6RF1yZibhiikNWBcOuHNT': ['project_info', 'project_packageversion'], 'var_call_UQWKVGzWS7wSzPvf8tWqUXbr': [], 'var_call_96fVbYYKbQGnQLDwqnuhdqvT': 'file_storage/call_96fVbYYKbQGnQLDwqnuhdqvT.json', 'var_call_IJfquksVbtcaMOIRxFtN9NCK': 'file_storage/call_IJfquksVbtcaMOIRxFtN9NCK.json'}

exec(code, env_args)
