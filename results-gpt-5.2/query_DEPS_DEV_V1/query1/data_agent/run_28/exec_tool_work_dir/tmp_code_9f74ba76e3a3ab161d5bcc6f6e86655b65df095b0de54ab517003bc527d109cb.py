code = """import json, re, pandas as pd
from pathlib import Path

def load_records(v):
    if isinstance(v, str) and v.endswith('.json') and Path(v).exists():
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_ssWG0BxdegPlpparFOW7Xy9Z)
ppv = load_records(var_call_coMkZH2gMcoC0z3oKU9cE4eG)
pi = load_records(var_call_kGYRXe1VOOBegMZPMBLdse9v)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# parse IsRelease and Ordinal
import ast

def parse_versioninfo(s):
    if s is None:
        return (None, None)
    try:
        obj = json.loads(s)
        return (obj.get('IsRelease'), obj.get('Ordinal'))
    except Exception:
        try:
            obj = ast.literal_eval(s)
            if isinstance(obj, dict):
                return (obj.get('IsRelease'), obj.get('Ordinal'))
        except Exception:
            pass
    return (None, None)

vi = pkg_df['VersionInfo'].apply(parse_versioninfo)
pkg_df['IsRelease'] = vi.apply(lambda x: x[0])
pkg_df['Ordinal'] = vi.apply(lambda x: x[1])

# keep only release versions
pkg_rel = pkg_df[pkg_df['IsRelease'] == True].copy()

# choose latest release per package: max Ordinal, tie-breaker max UpstreamPublishedAt
pkg_rel['UpstreamPublishedAt_num'] = pd.to_numeric(pkg_rel['UpstreamPublishedAt'], errors='coerce')
# ensure ordinal numeric
pkg_rel['Ordinal_num'] = pd.to_numeric(pkg_rel['Ordinal'], errors='coerce')

pkg_rel = pkg_rel.sort_values(['Name','Ordinal_num','UpstreamPublishedAt_num'], ascending=[True, False, False])
latest = pkg_rel.drop_duplicates(subset=['Name'], keep='first')[['Name','Version']].copy()
latest['System'] = 'NPM'

# join to project_packageversion to get ProjectName (prefer SOURCE_REPO_TYPE if multiple)
ppv_df = ppv_df[ppv_df['ProjectType'].fillna('')=='GITHUB'].copy()
merged = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')
# prioritize SOURCE_REPO_TYPE, then any
merged['src_prio'] = (merged['RelationType'] == 'SOURCE_REPO_TYPE').astype(int)
merged = merged.sort_values(['Name','src_prio'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')

# extract projectname and stars from project_info
# build mapping project -> stars by parsing Project_Information
pattern1 = re.compile(r"project\s+([^\s]+/[^\s]+)\s+.*?has\s+(?:garnered\s+significant\s+attention,\s+with\s+a\s+total\s+of\s+)?([0-9][0-9,]*)\s+stars", re.IGNORECASE)
pattern2 = re.compile(r"project\s+([^\s]+/[^\s]+).*?([0-9][0-9,]*)\s+stars", re.IGNORECASE)

def parse_pi(text):
    if not isinstance(text, str):
        return (None, None)
    m = pattern1.search(text)
    if not m:
        m = pattern2.search(text)
    if not m:
        return (None, None)
    proj = m.group(1).strip().strip('.,')
    stars = int(m.group(2).replace(',',''))
    return (proj, stars)

proj_stars = pi_df['Project_Information'].apply(parse_pi)
pi_df['ProjectName'] = proj_stars.apply(lambda x: x[0])
pi_df['Stars'] = proj_stars.apply(lambda x: x[1])
pi_map = pi_df.dropna(subset=['ProjectName','Stars']).drop_duplicates(subset=['ProjectName'])[['ProjectName','Stars']]

merged2 = merged.merge(pi_map, on='ProjectName', how='inner')

# top 5 by stars
out = merged2.sort_values('Stars', ascending=False).head(5)[['Name','Version','ProjectName','Stars']]
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ssWG0BxdegPlpparFOW7Xy9Z': 'file_storage/call_ssWG0BxdegPlpparFOW7Xy9Z.json', 'var_call_coMkZH2gMcoC0z3oKU9cE4eG': 'file_storage/call_coMkZH2gMcoC0z3oKU9cE4eG.json', 'var_call_kGYRXe1VOOBegMZPMBLdse9v': 'file_storage/call_kGYRXe1VOOBegMZPMBLdse9v.json'}

exec(code, env_args)
