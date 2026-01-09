code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        import pathlib
        p = pathlib.Path(v)
        txt = p.read_text(encoding='utf-8')
        return json.loads(txt)
    return v

pkg = load_records(var_call_S49ZDdLXD5ZF5LZibedJDv3h)
ppv = load_records(var_call_G4E37r7NLceEhdVKOgGYANdU)
pi = load_records(var_call_Gymm2DVVppNXFqoh37iGEO6M)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package (by VersionInfo.Ordinal among IsRelease=true; tie-breaker UpstreamPublishedAt)

def parse_versioninfo(s):
    if s is None:
        return (None, None)
    try:
        o = json.loads(s)
        return (bool(o.get('IsRelease')), o.get('Ordinal'))
    except Exception:
        return (None, None)

vi = pkg_df['VersionInfo'].apply(parse_versioninfo)
pkg_df['IsRelease'] = vi.apply(lambda x: x[0])
pkg_df['Ordinal'] = vi.apply(lambda x: x[1])

rel = pkg_df[pkg_df['IsRelease'] == True].copy()
# UpstreamPublishedAt may be str
rel['UpstreamPublishedAt_num'] = pd.to_numeric(rel['UpstreamPublishedAt'], errors='coerce')
rel['Ordinal_num'] = pd.to_numeric(rel['Ordinal'], errors='coerce')

rel = rel.sort_values(['Name','Ordinal_num','UpstreamPublishedAt_num','Version'], ascending=[True,False,False,False])
latest = rel.drop_duplicates(subset=['Name'], keep='first')[['System','Name','Version']]

# join to github project mapping
m = latest.merge(ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# parse project name and stars from Project_Information text
info = pi_df['Project_Information'].dropna().astype(str)
proj = info.str.extract(r'project\s+(?P<ProjectName>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
# some have "The project is hosted on GitHub under the name X" -> still matches
stars = info.str.extract(r'(?P<Stars>\d[\d,]*)\s+stars')
proj['Stars'] = stars['Stars']
proj = proj.dropna(subset=['ProjectName','Stars']).copy()
proj['Stars'] = proj['Stars'].str.replace(',','', regex=False).astype(int)

m2 = m.merge(proj, on='ProjectName', how='left')
m2 = m2.dropna(subset=['Stars'])

# if multiple ProjectName per package/version, take max stars
m2 = m2.sort_values(['Name','Stars'], ascending=[True,False])
m2 = m2.drop_duplicates(subset=['Name'], keep='first')

# top 5 by stars
out = m2.sort_values('Stars', ascending=False).head(5)[['Name','Version','ProjectName','Stars']]
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_S49ZDdLXD5ZF5LZibedJDv3h': 'file_storage/call_S49ZDdLXD5ZF5LZibedJDv3h.json', 'var_call_G4E37r7NLceEhdVKOgGYANdU': 'file_storage/call_G4E37r7NLceEhdVKOgGYANdU.json', 'var_call_Gymm2DVVppNXFqoh37iGEO6M': 'file_storage/call_Gymm2DVVppNXFqoh37iGEO6M.json'}

exec(code, env_args)
