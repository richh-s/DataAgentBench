code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7)
ppv = load_records(var_call_1QGSqqyNDZo8Y66QbYUHuHcC)
pi = load_records(var_call_BNfD7Iir4yoYI4yI3g4ncWcN)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest_df = (pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'])
             .groupby('Name', as_index=False)
             .tail(1)
             .loc[:, ['Name','Version','UpstreamPublishedAt']]
             .copy())
latest_df['System'] = 'NPM'

j = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse Project_Information -> repo + stars
rows=[]
star_re = re.compile(r'\b([0-9][0-9,]*)\s+stars\b', re.IGNORECASE)
repo_re = re.compile(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')
for rec in pi:
    s = rec.get('Project_Information') or ''
    m_repo = repo_re.search(s)
    m_star = star_re.search(s)
    if not (m_repo and m_star):
        continue
    repo = m_repo.group(1)
    stars = int(m_star.group(1).replace(',',''))
    rows.append({'ProjectName': repo, 'Stars': stars})
pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

j2 = j.merge(pi_df, on='ProjectName', how='left')
j2 = j2.dropna(subset=['Stars'])
agg = j2.groupby(['Name','Version'], as_index=False)['Stars'].max()

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7': 'file_storage/call_Z2uGzLu5Ia6ztPh0oPzFXIP7.json', 'var_call_1QGSqqyNDZo8Y66QbYUHuHcC': 'file_storage/call_1QGSqqyNDZo8Y66QbYUHuHcC.json', 'var_call_BNfD7Iir4yoYI4yI3g4ncWcN': 'file_storage/call_BNfD7Iir4yoYI4yI3g4ncWcN.json', 'var_call_H34KjCVgIe3d3GiJKx7oftTE': {'ppv_cols': ['System', 'Name', 'Version', 'ProjectName'], 'pkg_cols': ['Name', 'Version', 'UpstreamPublishedAt']}}

exec(code, env_args)
