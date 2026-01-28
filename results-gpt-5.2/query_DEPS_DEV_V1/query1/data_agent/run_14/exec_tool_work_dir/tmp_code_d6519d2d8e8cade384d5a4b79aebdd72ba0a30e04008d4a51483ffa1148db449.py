code = """import json, re, pandas as pd

# Load large results
import os

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

pkg_rows = load_records(var_call_KjWxTRBfFNUeiLw6HclfesP0)
ppv_rows = load_records(var_call_ohHzeQhy1J1UdCVbokse1FmZ)

pkg = pd.DataFrame(pkg_rows)
ppv = pd.DataFrame(ppv_rows)

# Parse VersionInfo.IsRelease

def is_release(v):
    if v is None:
        return False
    if isinstance(v, dict):
        return bool(v.get('IsRelease'))
    try:
        d = json.loads(v)
        return bool(d.get('IsRelease'))
    except Exception:
        return False

pkg['IsRelease'] = pkg['VersionInfo'].map(is_release)

# Latest release per package by UpstreamPublishedAt (fallback to max ordinal if needed)
# Convert UpstreamPublishedAt to numeric
pkg['UpstreamPublishedAt_num'] = pd.to_numeric(pkg['UpstreamPublishedAt'], errors='coerce')

latest = (pkg[pkg['IsRelease'] == True]
          .sort_values(['Name','UpstreamPublishedAt_num'], ascending=[True, False])
          .drop_duplicates(subset=['Name'], keep='first')
          [['System','Name','Version']])

# Join to project mapping to get GitHub repo
latest_ppv = latest.merge(ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# For packages that map to multiple repos, keep one (first)
latest_ppv = latest_ppv.drop_duplicates(subset=['Name'], keep='first')

# Need stars from project_info.Project_Information, but table lacks ProjectName.
# So we can't map; attempt to extract stars directly from ProjectName? Not possible.
# Return top 5 by stars cannot be computed with missing join key.

result = {
    'error': 'Cannot join project_info to project_packageversion because project_info table has no ProjectName column per schema. Please provide mapping key/column (e.g., ProjectName) in project_info.'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KjWxTRBfFNUeiLw6HclfesP0': 'file_storage/call_KjWxTRBfFNUeiLw6HclfesP0.json', 'var_call_ohHzeQhy1J1UdCVbokse1FmZ': 'file_storage/call_ohHzeQhy1J1UdCVbokse1FmZ.json'}

exec(code, env_args)
