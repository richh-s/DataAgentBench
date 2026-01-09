code = """import json, re, pandas as pd

# load large results
import os

def load_result(x):
    if isinstance(x, str) and x.endswith('.json') and os.path.exists(x):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pkg_rows = load_result(var_call_FFGnWhsl4aithTdxcwiEObL6)
ppv_rows = load_result(var_call_E2zjekrruq2FvZsjEFZMDQi2)
pi_rows = load_result(var_call_S5NEJjU1aWRU4G6svpECyTJU)

pkg = pd.DataFrame(pkg_rows)
ppv = pd.DataFrame(ppv_rows)
pi = pd.DataFrame(pi_rows)

# latest release per package based on VersionInfo.IsRelease==true; if missing parse fails treat as False

def is_release(vinfo):
    if vinfo is None:
        return False
    try:
        obj = json.loads(vinfo)
        return bool(obj.get('IsRelease', False))
    except Exception:
        return False

pkg['IsRelease'] = pkg['VersionInfo'].apply(is_release)
# UpstreamPublishedAt stored as string/float microseconds? ensure numeric
pkg['UpstreamPublishedAt_num'] = pd.to_numeric(pkg['UpstreamPublishedAt'], errors='coerce')

# filter to release versions
rel = pkg[pkg['IsRelease']].copy()
# if no timestamp, fallback 0
rel['UpstreamPublishedAt_num'] = rel['UpstreamPublishedAt_num'].fillna(0)

# choose latest by timestamp; tie-breaker by VersionInfo Ordinal if present

def ordinal(vinfo):
    try:
        return int(json.loads(vinfo).get('Ordinal', 0))
    except Exception:
        return 0

rel['Ordinal'] = rel['VersionInfo'].apply(ordinal)
rel = rel.sort_values(['System','Name','UpstreamPublishedAt_num','Ordinal','Version'], ascending=[True,True,False,False,False])
latest = rel.drop_duplicates(subset=['System','Name'], keep='first')[['System','Name','Version']]

# join to github project mapping
m = pd.merge(latest, ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
# pick one project per package (if multiple, keep first)
m = m.dropna(subset=['ProjectName']).sort_values(['Name','ProjectName']).drop_duplicates(subset=['System','Name','Version'], keep='first')

# parse stars from Project_Information
# build mapping from ProjectName to stars by extracting first token owner/repo
# project_info lacks ProjectName column; parse from text: 'project <name> ...'

def parse_proj_and_stars(text):
    if not isinstance(text, str):
        return (None, None)
    m1 = re.search(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', text)
    proj = m1.group(1) if m1 else None
    m2 = re.search(r'([0-9][0-9,]*)\s+stars', text)
    stars = int(m2.group(1).replace(',','')) if m2 else None
    return (proj, stars)

pi[['ProjectName','Stars']] = pi['Project_Information'].apply(lambda t: pd.Series(parse_proj_and_stars(t)))
pi2 = pi.dropna(subset=['ProjectName','Stars'])[['ProjectName','Stars']]
pi2 = pi2.sort_values(['ProjectName','Stars'], ascending=[True,False]).drop_duplicates('ProjectName', keep='first')

res = pd.merge(m, pi2, on='ProjectName', how='inner')

# top 5 by stars
res = res.sort_values('Stars', ascending=False).head(5)

out = res[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FFGnWhsl4aithTdxcwiEObL6': 'file_storage/call_FFGnWhsl4aithTdxcwiEObL6.json', 'var_call_E2zjekrruq2FvZsjEFZMDQi2': 'file_storage/call_E2zjekrruq2FvZsjEFZMDQi2.json', 'var_call_S5NEJjU1aWRU4G6svpECyTJU': 'file_storage/call_S5NEJjU1aWRU4G6svpECyTJU.json'}

exec(code, env_args)
