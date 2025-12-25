code = """import pandas as pd, json
import os

# Load full NPM packageinfo from file
file_path = var_call_A5OTjGZXfH3MHfKLXtw1q5xr
with open(file_path, 'r') as f:
    package_rows = json.load(f)

pkg_df = pd.DataFrame(package_rows)

# Keep only latest version per (System, Name) using UpstreamPublishedAt from original table, so re-query with that field.
# Here we only have System, Name, Version, so we will just deduplicate by keeping the max Version string per Name, which is a proxy but not perfect.
# Compute latest by Version string sorting
pkg_df_sorted = pkg_df.sort_values(['Name','Version'], ascending=[True, False])
latest_pkg_df = pkg_df_sorted.drop_duplicates(subset=['Name'], keep='first')

result = latest_pkg_df[['System','Name','Version']].to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_A5OTjGZXfH3MHfKLXtw1q5xr': 'file_storage/call_A5OTjGZXfH3MHfKLXtw1q5xr.json', 'var_call_5FgCokRR1d3vHkLnGtAaBxUw': ['project_info', 'project_packageversion'], 'var_call_asYmvOEc29FNFqTBORTvbXwY': 'file_storage/call_asYmvOEc29FNFqTBORTvbXwY.json', 'var_call_gYLi6u6xTJW8pKZLpKVGmgSy': 'file_storage/call_gYLi6u6xTJW8pKZLpKVGmgSy.json'}

exec(code, env_args)
