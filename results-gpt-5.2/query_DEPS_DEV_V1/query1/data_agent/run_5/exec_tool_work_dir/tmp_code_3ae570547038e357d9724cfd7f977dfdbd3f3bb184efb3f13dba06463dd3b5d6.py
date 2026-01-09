code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_61sip2jDRaAkvEj55sAOoDtX)
ppv = load_records(var_call_B0y1lnC5vCGtJvLEAJ2V5KBb)
pi = load_records(var_call_RyPKc1cGEaGCBESzLcXEnKyy)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package by UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
pkg_df = pkg_df.dropna(subset=['UpstreamPublishedAt'])
# sort and pick last per Name
latest = (pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'])
          .groupby('Name', as_index=False)
          .tail(1))

# join to github project mapping
m = latest.merge(ppv_df, on=['Name','Version'], how='inner')

# extract ProjectName from Project_Information and stars
pat = re.compile(r"(?:project\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).+?([0-9][0-9,]*)\s+stars", re.IGNORECASE)

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    m = pat.search(s)
    if not m:
        return None, None
    proj = m.group(1)
    stars = int(m.group(2).replace(',',''))
    return proj, stars

pi_df[['ProjectName','Stars']] = pi_df['Project_Information'].apply(lambda s: pd.Series(parse_info(s)))
pi_df = pi_df.dropna(subset=['ProjectName','Stars'])

m2 = m.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='left')
m2 = m2.dropna(subset=['Stars'])

# for each package, if multiple repos, take max stars
best = (m2.groupby(['Name','Version'], as_index=False)
        .agg({'Stars':'max','ProjectName':'first'}))

best = best.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

out = best[['Name','Version','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_61sip2jDRaAkvEj55sAOoDtX': 'file_storage/call_61sip2jDRaAkvEj55sAOoDtX.json', 'var_call_B0y1lnC5vCGtJvLEAJ2V5KBb': 'file_storage/call_B0y1lnC5vCGtJvLEAJ2V5KBb.json', 'var_call_RyPKc1cGEaGCBESzLcXEnKyy': 'file_storage/call_RyPKc1cGEaGCBESzLcXEnKyy.json'}

exec(code, env_args)
