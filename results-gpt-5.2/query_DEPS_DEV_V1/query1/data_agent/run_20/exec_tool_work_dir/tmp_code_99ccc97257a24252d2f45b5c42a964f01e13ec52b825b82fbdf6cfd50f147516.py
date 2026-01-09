code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_8Fx8Vn1AOSrMChm6hXCVFBnk)
ppv = load_records(var_call_5saD1bqCF7a39oEAdMlIadqb)
pi = load_records(var_call_PwAthYaNjSI4zlHCvT2eVNqa)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package using VersionInfo.IsRelease==true and max(UpstreamPublishedAt)
# parse VersionInfo json
is_release = []
for s in pkg_df['VersionInfo'].fillna('{}'):
    try:
        o = json.loads(s)
        is_release.append(bool(o.get('IsRelease', False)))
    except Exception:
        is_release.append(False)
pkg_df['IsRelease'] = is_release
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')

rel_df = pkg_df[pkg_df['IsRelease'] == True].copy()
# if none, fallback all; but keep as is
if rel_df.empty:
    rel_df = pkg_df.copy()

rel_df = rel_df.sort_values(['Name','UpstreamPublishedAt'], ascending=[True, False])
latest = rel_df.drop_duplicates(subset=['Name'], keep='first')[['System','Name','Version']]

# join to github project mapping
m = pd.merge(latest, ppv_df, on=['System','Name','Version'], how='inner')
# take one project per package (most frequent)
if not m.empty:
    # prefer relation with non-null ProjectName
    m = m.dropna(subset=['ProjectName'])
    m = m.groupby(['System','Name','Version'], as_index=False).agg({'ProjectName':'first'})

# parse project info strings for owner/repo and stars
proj_rows = []
pattern_repo = re.compile(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
pattern_stars = re.compile(r'(\d{1,3}(?:,\d{3})*)\s+stars')
for txt in pi_df['Project_Information'].dropna().astype(str):
    mr = pattern_repo.search(txt)
    ms = pattern_stars.search(txt)
    if mr and ms:
        repo = mr.group(1)
        stars = int(ms.group(1).replace(',',''))
        proj_rows.append({'ProjectName': repo, 'Stars': stars})
proj_df = pd.DataFrame(proj_rows).drop_duplicates(subset=['ProjectName'], keep='first')

res = pd.merge(m, proj_df, on='ProjectName', how='inner')
res = res.sort_values('Stars', ascending=False).head(5)

out = res[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8Fx8Vn1AOSrMChm6hXCVFBnk': 'file_storage/call_8Fx8Vn1AOSrMChm6hXCVFBnk.json', 'var_call_5saD1bqCF7a39oEAdMlIadqb': 'file_storage/call_5saD1bqCF7a39oEAdMlIadqb.json', 'var_call_PwAthYaNjSI4zlHCvT2eVNqa': 'file_storage/call_PwAthYaNjSI4zlHCvT2eVNqa.json'}

exec(code, env_args)
