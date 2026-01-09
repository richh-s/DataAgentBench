code = """import json, re, pandas as pd

# load large results
import os

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_dS7nJeyutcBPkLSD4S8VnKus)
ppv = load_records(var_call_piWi1bSd9xRFUlqM13JZYMz6)
pi = load_records(var_call_ms2DmAV0h0nOpbmZsTq5ow4r)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest version per package by max UpstreamPublishedAt
pkg_df['UpstreamPublishedAt_num'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest = (pkg_df.sort_values(['Name','UpstreamPublishedAt_num','Version'], ascending=[True, False, False])
          .dropna(subset=['UpstreamPublishedAt_num'])
          .drop_duplicates(subset=['Name'], keep='first')[['System','Name','Version']])

# join to github project mapping
m = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse stars from Project_Information and extract repo full name
star_re = re.compile(r'\b([0-9][0-9,]*)\s+stars\b')
repo_re = re.compile(r'project\s+([^\s,]+/[^\s,]+)')

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    repo = None
    m1 = repo_re.search(s)
    if m1:
        repo = m1.group(1)
    stars = None
    m2 = star_re.search(s)
    if m2:
        stars = int(m2.group(1).replace(',',''))
    return repo, stars

pi_df[['ProjectName','Stars']] = pi_df['Project_Information'].apply(lambda x: pd.Series(parse_info(x)))
pi_clean = pi_df.dropna(subset=['ProjectName','Stars']).drop_duplicates(subset=['ProjectName'], keep='first')

m2 = m.merge(pi_clean[['ProjectName','Stars']], on='ProjectName', how='left')

# Some packages might map to multiple repos; take max stars per package latest version
agg = (m2.dropna(subset=['Stars'])
       .groupby(['Name','Version'], as_index=False)['Stars'].max())

Top5 = agg.sort_values('Stars', ascending=False).head(5)
result = Top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_dS7nJeyutcBPkLSD4S8VnKus': 'file_storage/call_dS7nJeyutcBPkLSD4S8VnKus.json', 'var_call_piWi1bSd9xRFUlqM13JZYMz6': 'file_storage/call_piWi1bSd9xRFUlqM13JZYMz6.json', 'var_call_ms2DmAV0h0nOpbmZsTq5ow4r': 'file_storage/call_ms2DmAV0h0nOpbmZsTq5ow4r.json'}

exec(code, env_args)
