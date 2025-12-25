code = """import json, pandas as pd
import os

# Load full NPM packageinfo
with open(var_call_45B38BXbw6bJjoMFnpkQ1lwU, 'r') as f:
    pkg_records = json.load(f)

with open(var_call_p7T5evAZi7IcTqOiOkPg2ElH, 'r') as f:
    projpkg_records = json.load(f)

pkg_df = pd.DataFrame(pkg_records)
projpkg_df = pd.DataFrame(projpkg_records)

# Parse VersionInfo JSON and keep only release versions, if IsRelease present and true; otherwise keep rows without IsRelease flag as releases
vi = pkg_df['VersionInfo'].apply(lambda x: json.loads(x) if isinstance(x, str) and x.strip() != '' else {})
vi_df = pd.json_normalize(vi)
vi_df.columns = [f'vi_{c}' for c in vi_df.columns]
full_df = pd.concat([pkg_df, vi_df], axis=1)

# Determine latest release per (System, Name) using Ordinal when present, else UpstreamPublishedAt
full_df['vi_Ordinal'] = pd.to_numeric(full_df.get('vi_Ordinal'), errors='coerce')

# Filter to NPM system only (already done by SQL but keep safe)
full_df = full_df[full_df['System'] == 'NPM']

# Treat rows with vi_IsRelease == True as releases; if vi_IsRelease is NaN, assume release
is_release = full_df.get('vi_IsRelease')
full_df = full_df[(is_release.isna()) | (is_release == True)]

# For each package, compute a ranking key
full_df['ts'] = pd.to_numeric(full_df.get('UpstreamPublishedAt'), errors='coerce')

# Aggregate to latest per (Name) based on: first Ordinal desc, then ts desc, then Version lexicographically
full_df = full_df.sort_values(['Name','vi_Ordinal','ts','Version'], ascending=[True, False, False, False])
latest_pkg = full_df.groupby('Name', as_index=False).first()[['System','Name','Version']]

# Join with project_packageversion on System, Name, Version, filter GITHUB only
projpkg_df = projpkg_df[(projpkg_df['System']=='NPM') & (projpkg_df['ProjectType']=='GITHUB')]
merged = latest_pkg.merge(projpkg_df, on=['System','Name','Version'], how='inner')

# We now have ProjectName and packages; we'll later join with project_info to extract stars.
result = merged.head(20).to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_45B38BXbw6bJjoMFnpkQ1lwU': 'file_storage/call_45B38BXbw6bJjoMFnpkQ1lwU.json', 'var_call_YGWF1OGnPM78oG4azGQAkr06': ['project_info', 'project_packageversion'], 'var_call_p7T5evAZi7IcTqOiOkPg2ElH': 'file_storage/call_p7T5evAZi7IcTqOiOkPg2ElH.json', 'var_call_suWOovSUhvOKy7ocr9hDUyjR': 'file_storage/call_suWOovSUhvOKy7ocr9hDUyjR.json'}

exec(code, env_args)
