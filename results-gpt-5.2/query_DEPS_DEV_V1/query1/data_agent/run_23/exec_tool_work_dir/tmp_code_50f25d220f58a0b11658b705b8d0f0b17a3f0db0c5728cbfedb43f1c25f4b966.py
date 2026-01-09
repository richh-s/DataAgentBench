code = """import json, re, pandas as pd

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

ppv = load_var(var_call_lVm2xaQMQLWuYMZhfkibkHBa)
pkg = load_var(var_call_IFxhAc0Yo0zIu6YpiSYB7PR2)
pi = load_var(var_call_TnMYw5cv7bdkTfTzPeEDNUII)

ppv_df = pd.DataFrame(ppv)
pkg_df = pd.DataFrame(pkg)
pi_df = pd.DataFrame(pi)

# latest version per package by UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
pkg_df = pkg_df.dropna(subset=['UpstreamPublishedAt'])
idx = pkg_df.groupby(['System','Name'])['UpstreamPublishedAt'].idxmax()
latest_pkg = pkg_df.loc[idx, ['System','Name','Version','UpstreamPublishedAt']].copy()

# map latest package version to github project
latest_ppv = pd.merge(latest_pkg, ppv_df, on=['System','Name','Version'], how='inner')

# parse stars from Project_Information and extract ProjectName
pattern = re.compile(r"project\s+([^\s]+)\s+(?:is hosted on GitHub|on GitHub).*?has\s+(?:\d+[\w\s,]*?,\s*)?(\d{1,3}(?:,\d{3})*)\s+stars", re.IGNORECASE)

proj_rows = []
for s in pi_df['Project_Information'].dropna().astype(str):
    m = pattern.search(s)
    if m:
        project = m.group(1).strip().rstrip('.')
        stars = int(m.group(2).replace(',',''))
        proj_rows.append((project, stars))

proj_df = pd.DataFrame(proj_rows, columns=['ProjectName','Stars']).drop_duplicates(subset=['ProjectName'], keep='last')

latest_ppv = latest_ppv.dropna(subset=['ProjectName'])
joined = pd.merge(latest_ppv, proj_df, on='ProjectName', how='inner')

# If multiple repos per package/version, keep max stars
agg = joined.groupby(['Name','Version'], as_index=False)['Stars'].max()

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lVm2xaQMQLWuYMZhfkibkHBa': 'file_storage/call_lVm2xaQMQLWuYMZhfkibkHBa.json', 'var_call_IFxhAc0Yo0zIu6YpiSYB7PR2': 'file_storage/call_IFxhAc0Yo0zIu6YpiSYB7PR2.json', 'var_call_TnMYw5cv7bdkTfTzPeEDNUII': 'file_storage/call_TnMYw5cv7bdkTfTzPeEDNUII.json'}

exec(code, env_args)
