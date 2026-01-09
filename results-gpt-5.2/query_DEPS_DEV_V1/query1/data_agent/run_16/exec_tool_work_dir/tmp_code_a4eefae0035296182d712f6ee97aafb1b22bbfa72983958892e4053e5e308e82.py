code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_vVTedYEeyA93pTM4D7nyddjD)
ppv = load_records(var_call_7CeD8kWTMlOMnrBB4s5SkHVD)
pi = load_records(var_call_fmHalBocCD0R65wp6JZZgWWV)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package Name by max UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest = (pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'])
          .groupby('Name', as_index=False)
          .tail(1)[['Name','Version','UpstreamPublishedAt']])

# map package version to github project
latest_ppv = latest.merge(ppv_df[['Name','Version','ProjectName']], on=['Name','Version'], how='inner')

# parse ProjectName and stars from Project_Information
pattern_name = re.compile(r'project\s+([^\s]+/[^\s]+)')
pattern_stars = re.compile(r'(?:stars count of|has garnered .*?with a total of|currently has|has an open issues count of \d+,\s+along with a stars count of|on GitHub has an open issues count of \d+, a stars count of)\s*([0-9][0-9,]*)\s+stars')
# simpler: just find "([0-9,]+) stars" first occurrence
pattern_stars2 = re.compile(r'([0-9][0-9,]*)\s+stars')

names=[]
stars=[]
for s in pi_df['Project_Information'].dropna().astype(str):
    m = pattern_name.search(s)
    if not m:
        continue
    repo = m.group(1).strip().strip(',').strip('.')
    ms = pattern_stars2.search(s)
    if not ms:
        continue
    star = int(ms.group(1).replace(',',''))
    names.append(repo)
    stars.append(star)

stars_df = pd.DataFrame({'ProjectName': names, 'Stars': stars}).drop_duplicates('ProjectName')

joined = latest_ppv.merge(stars_df, on='ProjectName', how='left')
joined = joined.dropna(subset=['Stars'])

# if multiple repos per package (unlikely at single version), take max stars
best = (joined.groupby(['Name','Version'], as_index=False)
        .agg({'Stars':'max','ProjectName':'first'}))

out = best.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
result = out[['Name','Version','Stars','ProjectName']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vVTedYEeyA93pTM4D7nyddjD': 'file_storage/call_vVTedYEeyA93pTM4D7nyddjD.json', 'var_call_7CeD8kWTMlOMnrBB4s5SkHVD': 'file_storage/call_7CeD8kWTMlOMnrBB4s5SkHVD.json', 'var_call_fmHalBocCD0R65wp6JZZgWWV': 'file_storage/call_fmHalBocCD0R65wp6JZZgWWV.json'}

exec(code, env_args)
