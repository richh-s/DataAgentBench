code = """import json, re, pandas as pd

def load_maybe(path_or_list):
    if isinstance(path_or_list, str):
        with open(path_or_list, 'r') as f:
            return json.load(f)
    return path_or_list

latest = load_maybe(var_call_DubdlFnQItEEZCIYOIIkm0qL)
ppv = load_maybe(var_call_9fXPcZH7MdFMHgxYR8gowBRi)
pi = load_maybe(var_call_m2oOs9S92up9gw49KmjLp0JR)

latest_df = pd.DataFrame(latest)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# extract project name and stars from Project_Information
pat = re.compile(r"(?:project\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?(?:has|with|,)?\s*(?:garnered|received|has|along with)?[^\d]*(?:a\s+total\s+of\s+)?([0-9][0-9,]*)\s+stars", re.IGNORECASE)

def extract(row):
    s = row.get('Project_Information') or ''
    m = pat.search(s)
    if not m:
        return pd.Series({'ProjectName': None, 'Stars': None})
    proj = m.group(1)
    stars = int(m.group(2).replace(',', ''))
    return pd.Series({'ProjectName': proj, 'Stars': stars})

ext = pi_df.apply(extract, axis=1)
proj_stars = pd.concat([pi_df, ext], axis=1)
proj_stars = proj_stars.dropna(subset=['ProjectName','Stars'])
# if duplicates, take max stars
proj_stars = proj_stars.groupby('ProjectName', as_index=False)['Stars'].max()

# join latest versions to github project mapping
merged = latest_df.merge(ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
# join to stars
merged = merged.merge(proj_stars, on='ProjectName', how='inner')

# if multiple repos per package version, take max stars
pkg_best = merged.groupby(['Name','Version'], as_index=False).agg({'Stars':'max','ProjectName':'first'})

# top 5 by stars
res = pkg_best.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
res_list = res[['Name','Version','Stars','ProjectName']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res_list))"""

env_args = {'var_call_DubdlFnQItEEZCIYOIIkm0qL': 'file_storage/call_DubdlFnQItEEZCIYOIIkm0qL.json', 'var_call_9fXPcZH7MdFMHgxYR8gowBRi': 'file_storage/call_9fXPcZH7MdFMHgxYR8gowBRi.json', 'var_call_m2oOs9S92up9gw49KmjLp0JR': 'file_storage/call_m2oOs9S92up9gw49KmjLp0JR.json'}

exec(code, env_args)
