code = """import json, re, pandas as pd

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_c44FHu8FHzypC2LdYXy7wI2w)
ppv = load_var(var_call_Z0d5blrM70HGmEz3vNLCaN11)
pi = load_var(var_call_Hy8mQaKlxsugEtSBwEQVBTKH)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package by max UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest = pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True, False, False]).drop_duplicates(['Name'], keep='first')

# map to github projects
merged = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')

# extract projectname and stars from Project_Information
info = pi_df.copy()
# project name pattern: 'project owner/repo' or 'project named owner/repo' or 'project is hosted on GitHub under the name owner/repo'
name_pat = re.compile(r'(?:project\s+(?:named\s+)?)([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)')
alt_pat = re.compile(r'GitHub\s+(?:repository\s+named\s+)?([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)')
under_name_pat = re.compile(r'under the name\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)')

stars_pat = re.compile(r'(\d[\d,]*)\s+stars')

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    m = name_pat.search(s) or alt_pat.search(s) or under_name_pat.search(s)
    proj = m.group(1) if m else None
    sm = stars_pat.search(s)
    stars = int(sm.group(1).replace(',','')) if sm else None
    return proj, stars

parsed = info['Project_Information'].apply(parse_info)
info['ProjectName'] = parsed.apply(lambda x: x[0])
info['Stars'] = parsed.apply(lambda x: x[1])
info = info.dropna(subset=['ProjectName','Stars'])
info = info.sort_values('Stars', ascending=False).drop_duplicates('ProjectName', keep='first')

merged2 = merged.merge(info[['ProjectName','Stars']], on='ProjectName', how='left')
merged2 = merged2.dropna(subset=['Stars'])

# if multiple project mappings per package/version, keep the one with max stars
merged2 = merged2.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates(['Name'], keep='first')

top5 = merged2.sort_values('Stars', ascending=False).head(5)
res = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_c44FHu8FHzypC2LdYXy7wI2w': 'file_storage/call_c44FHu8FHzypC2LdYXy7wI2w.json', 'var_call_Z0d5blrM70HGmEz3vNLCaN11': 'file_storage/call_Z0d5blrM70HGmEz3vNLCaN11.json', 'var_call_Hy8mQaKlxsugEtSBwEQVBTKH': 'file_storage/call_Hy8mQaKlxsugEtSBwEQVBTKH.json'}

exec(code, env_args)
