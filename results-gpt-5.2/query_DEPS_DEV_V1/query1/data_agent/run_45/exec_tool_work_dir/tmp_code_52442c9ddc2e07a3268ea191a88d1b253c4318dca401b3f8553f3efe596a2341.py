code = """import json, re, pandas as pd

def load_result(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_result(var_call_AuV0mriHKUi4cBK0DrFLW3zz)
ppv = load_result(var_call_aZNbA6QzX3c5e4AMBqI0aITG)
pi = load_result(var_call_T8JItSloEUeY5ZwfqSqBI6d7)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest version per package name by max UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest = pkg_df.sort_values(['Name','UpstreamPublishedAt','Version']).groupby('Name', as_index=False).tail(1)
latest = latest[['System','Name','Version']]

# join to get ProjectName
m = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')
# reduce to one ProjectName per package/version
m = m.dropna(subset=['ProjectName']).drop_duplicates(subset=['System','Name','Version','ProjectName'])

# parse stars from Project_Information and also extract repo full name
star_re = re.compile(r"\b(\d[\d,]*)\s+stars\b", re.IGNORECASE)
repo_re = re.compile(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b")

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    sm = star_re.search(s)
    stars = int(sm.group(1).replace(',','')) if sm else None
    # choose first owner/repo occurrence
    rm = repo_re.search(s)
    repo = rm.group(1) if rm else None
    return repo, stars

pi_df[['ProjectName','Stars']] = pi_df['Project_Information'].apply(lambda x: pd.Series(parse_info(x)))
pi_df = pi_df.dropna(subset=['ProjectName'])

# join stars by ProjectName
m2 = m.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='left')
# per package, take max stars across possible repos
m2['Stars'] = pd.to_numeric(m2['Stars'], errors='coerce')
agg = m2.groupby(['Name','Version'], as_index=False)['Stars'].max()
agg = agg.dropna(subset=['Stars'])

top5 = agg.sort_values('Stars', ascending=False).head(5)
res = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_AuV0mriHKUi4cBK0DrFLW3zz': 'file_storage/call_AuV0mriHKUi4cBK0DrFLW3zz.json', 'var_call_aZNbA6QzX3c5e4AMBqI0aITG': 'file_storage/call_aZNbA6QzX3c5e4AMBqI0aITG.json', 'var_call_T8JItSloEUeY5ZwfqSqBI6d7': 'file_storage/call_T8JItSloEUeY5ZwfqSqBI6d7.json'}

exec(code, env_args)
