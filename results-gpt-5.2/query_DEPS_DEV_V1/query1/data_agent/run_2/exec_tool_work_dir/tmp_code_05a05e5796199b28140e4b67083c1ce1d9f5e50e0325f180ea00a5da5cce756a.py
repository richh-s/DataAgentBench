code = """import json, re, pandas as pd

# Load large tool outputs (may be file paths)

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

pkg = load_records(var_call_nEUrbuTdcJs1dnPZ0OrgHz9Y)
ppv = load_records(var_call_ysqtpLByKkZyD3m4sXIr5nZB)
projinfo = load_records(var_call_XDfTzA5i2xixAOfspV8GvEAH)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
proj_df = pd.DataFrame(projinfo)

# latest release per package by UpstreamPublishedAt (ties -> max timestamp, then max Version lexicographically)
# ensure numeric
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')

# drop missing names/versions
pkg_df = pkg_df.dropna(subset=['Name','Version','UpstreamPublishedAt'])

pkg_df = pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True, False, False])
latest = pkg_df.groupby('Name', as_index=False).head(1)[['System','Name','Version']]

# join to project mapping
merged = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse projectname and stars from Project_Information
pat = re.compile(r"project\s+([^\s]+/[^\s]+).*?\b([0-9][0-9,]*)\s+stars\b", re.IGNORECASE)

proj_df['ProjectName'] = proj_df['Project_Information'].str.extract(r"project\s+([^\s]+/[^\s]+)", expand=False)
proj_df['Stars'] = proj_df['Project_Information'].apply(lambda s: int(pat.search(s).group(2).replace(',','')) if isinstance(s,str) and pat.search(s) else None)

merged2 = merged.merge(proj_df[['ProjectName','Stars']], on='ProjectName', how='left')
merged2 = merged2.dropna(subset=['Stars'])

# In case multiple repos per package/version, take max stars
best = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()

# top 5
best = best.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

lines = []
for _, r in best.iterrows():
    lines.append(f"{r['Name']}@{r['Version']} — {int(r['Stars'])} GitHub stars")

out = "\n".join(lines)
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nEUrbuTdcJs1dnPZ0OrgHz9Y': 'file_storage/call_nEUrbuTdcJs1dnPZ0OrgHz9Y.json', 'var_call_ysqtpLByKkZyD3m4sXIr5nZB': 'file_storage/call_ysqtpLByKkZyD3m4sXIr5nZB.json', 'var_call_XDfTzA5i2xixAOfspV8GvEAH': 'file_storage/call_XDfTzA5i2xixAOfspV8GvEAH.json'}

exec(code, env_args)
