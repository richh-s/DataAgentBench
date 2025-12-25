code = """import pandas as pd, json
import os

file_path = var_call_n3hHVcOaNDEvIoNK6zRDhj1J
with open(file_path, 'r') as f:
    npm_packages = json.load(f)

pkg_df = pd.DataFrame(npm_packages)

# If VersionInfo exists in the data, try to use it to determine latest releases.
# But our preview only showed System, Name, Version, so we fall back to using UpstreamPublishedAt when available.

# Fetch full packageinfo data for NPM with relevant fields via a heuristic: we already loaded all NPM rows.
# Determine latest by (Name, max UpstreamPublishedAt), falling back to lexical max Version when timestamp is missing.

if 'UpstreamPublishedAt' in pkg_df.columns:
    pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
else:
    pkg_df['UpstreamPublishedAt'] = pd.NA

# group by Name to find index of latest release

def pick_latest(group):
    if group['UpstreamPublishedAt'].notna().any():
        idx = group['UpstreamPublishedAt'].idxmax()
    else:
        # lexical max version fallback
        idx = group['Version'].astype(str).idxmax()
    return group.loc[idx]

latest_pkg_df = pkg_df.groupby('Name', as_index=False).apply(pick_latest).reset_index(drop=True)

latest_pkg_df = latest_pkg_df[['System','Name','Version']]

result = latest_pkg_df.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_n3hHVcOaNDEvIoNK6zRDhj1J': 'file_storage/call_n3hHVcOaNDEvIoNK6zRDhj1J.json', 'var_call_dld2sHB5YJisR0GdydadjFPq': ['project_info', 'project_packageversion'], 'var_call_wVcuCjNnDqo8wehZKF0ZdTp6': 'file_storage/call_wVcuCjNnDqo8wehZKF0ZdTp6.json', 'var_call_siP8WXBH2VKuziRKdXl5RWxF': 'file_storage/call_siP8WXBH2VKuziRKdXl5RWxF.json'}

exec(code, env_args)
