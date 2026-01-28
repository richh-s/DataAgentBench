code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

latest = load_records(var_call_Vs97uIw6keALIEPbndC1k5qj)
ppv = load_records(var_call_hR4LXFVaVqRK9ZtPbdBLKvCY)
pi = load_records(var_call_gdZJ3nPwFz9136ieAhgvOsRR)

latest_df = pd.DataFrame(latest)
ppv_df = pd.DataFrame(ppv)

# Parse project_info text into (ProjectName, stars)
rows = []
pat = re.compile(r"project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?([0-9,]+)\s+stars", re.IGNORECASE)
for r in pi:
    txt = r.get('Project_Information') or ''
    m = pat.search(txt)
    if m:
        proj = m.group(1)
        stars = int(m.group(2).replace(',', ''))
        rows.append({'ProjectName': proj, 'Stars': stars})
proj_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

# Join latest package versions -> github repo mapping -> stars
merged = latest_df.merge(ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
merged = merged.merge(proj_df, on='ProjectName', how='inner')

# If multiple repos per package/version, keep max stars
pkg_best = merged.groupby(['Name','Version'], as_index=False).agg({'Stars':'max'})

top5 = pkg_best.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Vs97uIw6keALIEPbndC1k5qj': 'file_storage/call_Vs97uIw6keALIEPbndC1k5qj.json', 'var_call_hR4LXFVaVqRK9ZtPbdBLKvCY': 'file_storage/call_hR4LXFVaVqRK9ZtPbdBLKvCY.json', 'var_call_gdZJ3nPwFz9136ieAhgvOsRR': 'file_storage/call_gdZJ3nPwFz9136ieAhgvOsRR.json'}

exec(code, env_args)
