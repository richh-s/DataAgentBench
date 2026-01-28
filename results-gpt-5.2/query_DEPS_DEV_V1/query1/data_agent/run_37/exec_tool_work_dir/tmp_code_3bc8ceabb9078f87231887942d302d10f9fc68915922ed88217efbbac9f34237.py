code = """import json, re, pandas as pd

# Load big JSON lists from file paths

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_recs = load_records(var_call_PXI4s1eMnRtGMLBjpZNK860r)
map_recs = load_records(var_call_LIoNgV3gLAKOAT5Xs8ArJmij)
proj_recs = load_records(var_call_IgaSe7HS9nvsQxU2AKpHkLWp)

pkg = pd.DataFrame(pkg_recs)
mp = pd.DataFrame(map_recs)
pi = pd.DataFrame(proj_recs)

# Latest release per package based on UpstreamPublishedAt
pkg['UpstreamPublishedAt'] = pd.to_numeric(pkg['UpstreamPublishedAt'], errors='coerce')
idx = pkg.sort_values(['Name','UpstreamPublishedAt','Version']).groupby('Name', as_index=False).tail(1).index
latest = pkg.loc[idx, ['Name','Version','UpstreamPublishedAt']].copy()

# Join to mapping to get github project name
latest_mp = latest.merge(mp[['Name','Version','ProjectName']], on=['Name','Version'], how='inner')

# Extract owner/repo and stars from Project_Information
pat = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?([0-9,]+)\s+stars", re.IGNORECASE)

def parse_info(s):
    if s is None:
        return None, None
    m = pat.search(s)
    if not m:
        return None, None
    proj = m.group(1)
    stars = int(m.group(2).replace(',',''))
    return proj, stars

parsed = pi['Project_Information'].apply(parse_info)
pi2 = pd.DataFrame(parsed.tolist(), columns=['ProjectName','Stars'])
pi2 = pi2.dropna(subset=['ProjectName','Stars'])

# Join to get stars
full = latest_mp.merge(pi2, on='ProjectName', how='inner')

# For packages that map to multiple repos, take max stars
agg = full.groupby(['Name','Version'], as_index=False).agg(ProjectName=('ProjectName','first'), Stars=('Stars','max'))

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

result = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PXI4s1eMnRtGMLBjpZNK860r': 'file_storage/call_PXI4s1eMnRtGMLBjpZNK860r.json', 'var_call_LIoNgV3gLAKOAT5Xs8ArJmij': 'file_storage/call_LIoNgV3gLAKOAT5Xs8ArJmij.json', 'var_call_IgaSe7HS9nvsQxU2AKpHkLWp': 'file_storage/call_IgaSe7HS9nvsQxU2AKpHkLWp.json'}

exec(code, env_args)
