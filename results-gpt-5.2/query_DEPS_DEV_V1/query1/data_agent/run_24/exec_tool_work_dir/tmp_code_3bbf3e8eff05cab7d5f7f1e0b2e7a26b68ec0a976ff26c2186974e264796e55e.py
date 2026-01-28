code = """import json, re, pandas as pd

def load_result(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

latest = load_result(var_call_6jYNkMr24FkmOwigCrOIVgAy)
ppv = load_result(var_call_7WLzc2yghlHCLYGId1f5qTkF)
pi = load_result(var_call_mAbrUXH7aDLbHR5G0zEIxXsc)

latest_df = pd.DataFrame(latest)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# Map project -> stars parsed from Project_Information
star_re = re.compile(r'\b([0-9,]+)\s+stars\b', re.IGNORECASE)
proj_re = re.compile(r'\bproject\s+([^\s]+/[^\s]+)\b', re.IGNORECASE)

def parse_proj_stars(text):
    if not isinstance(text, str):
        return None, None
    mproj = proj_re.search(text)
    mstar = star_re.search(text)
    proj = mproj.group(1).strip('.,') if mproj else None
    stars = int(mstar.group(1).replace(',', '')) if mstar else None
    return proj, stars

rows = []
for t in pi_df['Project_Information'].tolist():
    proj, stars = parse_proj_stars(t)
    if proj is not None and stars is not None:
        rows.append((proj, stars))

proj_stars_df = pd.DataFrame(rows, columns=['ProjectName','Stars']).drop_duplicates('ProjectName')

# Join latest package versions to github project mapping
merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
# If multiple projects per package version, keep the one with max stars
merged = merged.merge(proj_stars_df, on='ProjectName', how='inner')

pkg_best = (merged.sort_values(['Name','Stars'], ascending=[True, False])
            .drop_duplicates(['System','Name'], keep='first'))

top5 = pkg_best.sort_values('Stars', ascending=False).head(5)

result = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6jYNkMr24FkmOwigCrOIVgAy': 'file_storage/call_6jYNkMr24FkmOwigCrOIVgAy.json', 'var_call_7WLzc2yghlHCLYGId1f5qTkF': 'file_storage/call_7WLzc2yghlHCLYGId1f5qTkF.json', 'var_call_mAbrUXH7aDLbHR5G0zEIxXsc': 'file_storage/call_mAbrUXH7aDLbHR5G0zEIxXsc.json'}

exec(code, env_args)
