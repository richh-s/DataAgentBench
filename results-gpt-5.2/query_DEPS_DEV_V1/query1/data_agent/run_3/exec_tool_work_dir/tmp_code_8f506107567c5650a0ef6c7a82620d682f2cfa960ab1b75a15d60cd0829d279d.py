code = """import json, re, pandas as pd

# Load large results

def load_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_result(var_call_He9Kjt4XFuuEfU7labA0LVG9)
ppv = load_result(var_call_SOZJHSLhWXbF6G5x9sn97cC3)
pi = load_result(var_call_jjFfeKusGB6aOYxoPkxDr7Vc)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest version per (System, Name) based on max UpstreamPublishedAt
# ensure numeric
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest_idx = pkg_df.groupby(['System','Name'])['UpstreamPublishedAt'].idxmax()
latest_df = pkg_df.loc[latest_idx, ['System','Name','Version']].dropna()

# map to github project via project_packageversion
# there may be multiple ProjectName; pick first non-null
merged = pd.merge(latest_df, ppv_df, on=['System','Name','Version'], how='inner')
# choose one ProjectName per package
merged = merged.dropna(subset=['ProjectName'])
merged = merged.sort_values(['System','Name','Version','ProjectName'])
merged = merged.drop_duplicates(subset=['System','Name'], keep='first')

# parse stars from Project_Information and projectname from text
stars_pat = re.compile(r'(?:has|with)\s+([0-9][0-9,]*)\s+stars', re.IGNORECASE)
proj_pat = re.compile(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')

def extract_project_and_stars(text):
    if not isinstance(text, str):
        return None, None
    mproj = proj_pat.search(text)
    proj = mproj.group(1) if mproj else None
    mstars = stars_pat.search(text)
    stars = int(mstars.group(1).replace(',','')) if mstars else None
    return proj, stars

pi_df[['ProjectName','Stars']] = pi_df['Project_Information'].apply(lambda t: pd.Series(extract_project_and_stars(t)))
pi_df = pi_df.dropna(subset=['ProjectName','Stars'])
pi_df['Stars'] = pd.to_numeric(pi_df['Stars'], errors='coerce')
# in case duplicates, keep max stars
pi_df = pi_df.groupby('ProjectName', as_index=False)['Stars'].max()

merged2 = pd.merge(merged, pi_df, on='ProjectName', how='left')
merged2 = merged2.dropna(subset=['Stars'])
merged2['Stars'] = merged2['Stars'].astype(int)

# top 5 by stars
out = merged2.sort_values('Stars', ascending=False).head(5)[['Name','Version','ProjectName','Stars']]
result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_He9Kjt4XFuuEfU7labA0LVG9': 'file_storage/call_He9Kjt4XFuuEfU7labA0LVG9.json', 'var_call_SOZJHSLhWXbF6G5x9sn97cC3': 'file_storage/call_SOZJHSLhWXbF6G5x9sn97cC3.json', 'var_call_jjFfeKusGB6aOYxoPkxDr7Vc': 'file_storage/call_jjFfeKusGB6aOYxoPkxDr7Vc.json'}

exec(code, env_args)
