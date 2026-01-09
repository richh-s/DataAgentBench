code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_aLcQGJc4kQTV6b7Ltc0SnKpc)
ppv = load_records(var_call_tMNsCnGAv1G9o1BeWXu1xArr)
pi = load_records(var_call_9p0TJ73QlEghVwaZ4RG57GjF)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package by max UpstreamPublishedAt; tie-break by max version (lex) as fallback
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
# sort to get latest first
pkg_df = pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True, False, False])
latest = pkg_df.drop_duplicates(subset=['Name'], keep='first')[['Name','Version']]

# join to github mapping
latest_map = latest.merge(ppv_df, on=['Name','Version'], how='inner')

# parse stars and projectname from Project_Information text
# Build mapping project -> stars from project_info
pat = re.compile(r"project\s+([\w.-]+/[\w.-]+).*?([0-9][0-9,]*)\s+stars", re.IGNORECASE)
proj_stars = []
for s in pi_df['Project_Information'].dropna().astype(str):
    m = pat.search(s)
    if m:
        proj = m.group(1)
        stars = int(m.group(2).replace(',',''))
        proj_stars.append((proj, stars))

stars_df = pd.DataFrame(proj_stars, columns=['ProjectName','Stars']).drop_duplicates(subset=['ProjectName'], keep='last')

joined = latest_map.merge(stars_df, on='ProjectName', how='inner')

# if multiple repos for same package/version, take max stars
best = joined.groupby(['Name','Version'], as_index=False).agg(Stars=('Stars','max'), ProjectName=('ProjectName','first'))

top5 = best.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

result = top5[['Name','Version','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_aLcQGJc4kQTV6b7Ltc0SnKpc': 'file_storage/call_aLcQGJc4kQTV6b7Ltc0SnKpc.json', 'var_call_tMNsCnGAv1G9o1BeWXu1xArr': 'file_storage/call_tMNsCnGAv1G9o1BeWXu1xArr.json', 'var_call_9p0TJ73QlEghVwaZ4RG57GjF': 'file_storage/call_9p0TJ73QlEghVwaZ4RG57GjF.json'}

exec(code, env_args)
