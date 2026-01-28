code = """import json, re, pandas as pd

# load large query results

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_gDchBaqjbySr3BAFqgMM3wUP)
ppv = load_records(var_call_zKwKZBs4CtdnxcHRSHR7glgn)
pi = load_records(var_call_rnMzhMkqvrl5famlsRVhXIfK)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

# latest release per package by UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
# drop missing timestamps
pkg_df = pkg_df.dropna(subset=['UpstreamPublishedAt'])
idx = pkg_df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest_df = pkg_df.loc[idx, ['Name','Version','UpstreamPublishedAt']].copy()

# map latest package version to a github project (choose first projectname if multiple)
merged = latest_df.merge(ppv_df[['Name','Version','ProjectName']], on=['Name','Version'], how='inner')
merged = merged.dropna(subset=['ProjectName'])
merged = merged.drop_duplicates(subset=['Name','Version'])

# parse project_info to extract owner/repo and stars
info_rows = []
pat = re.compile(r"(?:project\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).+?(\d[\d,]*)\s+stars", re.IGNORECASE)
for r in pi:
    s = r.get('Project_Information') or ''
    m = pat.search(s)
    if not m:
        continue
    repo = m.group(1)
    stars = int(m.group(2).replace(',',''))
    info_rows.append({'ProjectName': repo, 'Stars': stars})
info_df = pd.DataFrame(info_rows).drop_duplicates(subset=['ProjectName'])

merged2 = merged.merge(info_df, on='ProjectName', how='inner')

# top 5 packages by stars
out = merged2.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
out_records = out[['Name','Version','ProjectName','Stars']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out_records))"""

env_args = {'var_call_gDchBaqjbySr3BAFqgMM3wUP': 'file_storage/call_gDchBaqjbySr3BAFqgMM3wUP.json', 'var_call_zKwKZBs4CtdnxcHRSHR7glgn': 'file_storage/call_zKwKZBs4CtdnxcHRSHR7glgn.json', 'var_call_rnMzhMkqvrl5famlsRVhXIfK': 'file_storage/call_rnMzhMkqvrl5famlsRVhXIfK.json'}

exec(code, env_args)
