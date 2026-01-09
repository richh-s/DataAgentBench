code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        # file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_GXRGsllSKE6Q54hfG18UYfLV)
ppv = load_records(var_call_09TLFgPxbCe1lZmF7Zsvon1V)
pi = load_records(var_call_4xLEkAzxwr4JbhLGV5oillDe)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release versions per package based on VersionInfo.IsRelease and max Ordinal

def is_release(vinfo):
    try:
        o = json.loads(vinfo)
        return bool(o.get('IsRelease', False)), o.get('Ordinal', None)
    except Exception:
        return False, None

rel_flags = pkg_df['VersionInfo'].apply(is_release)
pkg_df['IsRelease'] = rel_flags.apply(lambda x: x[0])
pkg_df['Ordinal'] = rel_flags.apply(lambda x: x[1])

rel_df = pkg_df[pkg_df['IsRelease'] == True].copy()
rel_df = rel_df.dropna(subset=['Ordinal'])
# in case of duplicates, take max ordinal per Name
idx = rel_df.groupby('Name')['Ordinal'].idxmax()
latest_rel = rel_df.loc[idx, ['Name','Version']]

# map to github project via project_packageversion on latest release version
m = latest_rel.merge(ppv_df, on=['Name','Version'], how='inner')
# if multiple ProjectName per package/version, keep the first
m = m.drop_duplicates(subset=['Name','Version'])

# parse project_info Project_Information to get repo and stars
info = pi_df['Project_Information'].dropna().astype(str)
repo_re = re.compile(r'project\s+([^\s]+/[^\s]+)')
stars_re = re.compile(r'(\d[\d,]*)\s+stars')
rows = []
for s in info:
    rm = repo_re.search(s)
    sm = stars_re.search(s)
    if rm and sm:
        repo = rm.group(1).strip().rstrip('.,;')
        stars = int(sm.group(1).replace(',',''))
        rows.append((repo, stars))
pi_parsed = pd.DataFrame(rows, columns=['ProjectName','Stars']).drop_duplicates('ProjectName')

m2 = m.merge(pi_parsed, on='ProjectName', how='inner')

# top 5 by stars
out = m2.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
result = out[['Name','Version','ProjectName','Stars']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GXRGsllSKE6Q54hfG18UYfLV': 'file_storage/call_GXRGsllSKE6Q54hfG18UYfLV.json', 'var_call_09TLFgPxbCe1lZmF7Zsvon1V': 'file_storage/call_09TLFgPxbCe1lZmF7Zsvon1V.json', 'var_call_4xLEkAzxwr4JbhLGV5oillDe': 'file_storage/call_4xLEkAzxwr4JbhLGV5oillDe.json'}

exec(code, env_args)
