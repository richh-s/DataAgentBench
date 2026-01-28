code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = pd.DataFrame(load_records(var_call_bM0FEw5NxqBay84ppfoAfYYd))
ppv = pd.DataFrame(load_records(var_call_zASnPOJ9U0V5nbOZPp0jenez))
pi = pd.DataFrame(load_records(var_call_Vtbnpg7WevHGptUVf7K7d4VM))

# latest version per package by UpstreamPublishedAt
pkg['UpstreamPublishedAt'] = pd.to_numeric(pkg['UpstreamPublishedAt'], errors='coerce')
pkg_latest = pkg.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True,False,False]).drop_duplicates(['Name'], keep='first')

# join to project mapping on (Name, Version)
ppv_small = ppv[['Name','Version','ProjectName']].drop_duplicates()
merged = pkg_latest.merge(ppv_small, on=['Name','Version'], how='inner')

# parse stars from project_info text and repo name
stars_re = re.compile(r'(?i)(?:has|with|at)\s+(?:a\s+total\s+of\s+)?([0-9][0-9,]*)\s+stars')
repo_re = re.compile(r'project\s+([^\s]+/[^\s]+)', re.IGNORECASE)

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    m_repo = repo_re.search(s)
    repo = m_repo.group(1).strip('.,') if m_repo else None
    m = stars_re.search(s)
    stars = int(m.group(1).replace(',','')) if m else None
    return repo, stars

pi[['ProjectName','Stars']] = pi['Project_Information'].apply(lambda s: pd.Series(parse_info(s)))
pi2 = pi.dropna(subset=['ProjectName'])[['ProjectName','Stars']]
pi2['Stars'] = pd.to_numeric(pi2['Stars'], errors='coerce')

merged2 = merged.merge(pi2, on='ProjectName', how='left')
merged2 = merged2.dropna(subset=['Stars'])

# if multiple repos for a package latest version, take max stars
agg = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bM0FEw5NxqBay84ppfoAfYYd': 'file_storage/call_bM0FEw5NxqBay84ppfoAfYYd.json', 'var_call_zASnPOJ9U0V5nbOZPp0jenez': 'file_storage/call_zASnPOJ9U0V5nbOZPp0jenez.json', 'var_call_Vtbnpg7WevHGptUVf7K7d4VM': 'file_storage/call_Vtbnpg7WevHGptUVf7K7d4VM.json'}

exec(code, env_args)
