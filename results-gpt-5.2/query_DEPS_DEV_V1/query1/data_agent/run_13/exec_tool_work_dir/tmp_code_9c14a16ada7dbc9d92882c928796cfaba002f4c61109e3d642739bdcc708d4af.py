code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

ppv = load(var_call_b3Q6G8EbikjOVOTwsBAODZIR)
pkg = load(var_call_pG9KzfNBBJFWOPaTQPj6Pp6E)
pi = load(var_call_v6hfimIZ3hZvoStfUJ6kRVaf)

ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].dropna()
pkg_df = pd.DataFrame(pkg)[['System','Name','Version','UpstreamPublishedAt']].dropna()

# ensure numeric
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')

# latest version per (System,Name) by max UpstreamPublishedAt (ties -> max Version lex)
latest = pkg_df.sort_values(['System','Name','UpstreamPublishedAt','Version'], ascending=[True,True,False,False]) \
              .drop_duplicates(['System','Name'], keep='first')[['System','Name','Version']]

# map to github project for that exact version
m = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')

# project_info parsing stars
pi_df = pd.DataFrame(pi)

def extract_repo_and_stars(text):
    if not isinstance(text, str):
        return (None, None)
    m1 = re.search(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', text)
    repo = m1.group(1) if m1 else None
    m2 = re.search(r'(?:has|with|of)\s+([0-9][0-9,]*)\s+stars', text)
    stars = int(m2.group(1).replace(',','')) if m2 else None
    return repo, stars

repos = []
stars = []
for t in pi_df.get('Project_Information', []):
    r,s = extract_repo_and_stars(t)
    repos.append(r)
    stars.append(s)
pi_df['_repo'] = repos
pi_df['_stars'] = stars
pi_map = pi_df.dropna(subset=['_repo']).groupby('_repo', as_index=False)['_stars'].max()

m2 = m.merge(pi_map, left_on='ProjectName', right_on='_repo', how='left')
m2 = m2.dropna(subset=['_stars'])

# if multiple projects per package/version, keep max stars
agg = m2.groupby(['Name','Version'], as_index=False).agg(github_stars=('_stars','max'), project=('ProjectName','first'))

top5 = agg.sort_values(['github_stars','Name'], ascending=[False,True]).head(5)

result = top5[['Name','Version','github_stars','project']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_b3Q6G8EbikjOVOTwsBAODZIR': 'file_storage/call_b3Q6G8EbikjOVOTwsBAODZIR.json', 'var_call_pG9KzfNBBJFWOPaTQPj6Pp6E': 'file_storage/call_pG9KzfNBBJFWOPaTQPj6Pp6E.json', 'var_call_v6hfimIZ3hZvoStfUJ6kRVaf': 'file_storage/call_v6hfimIZ3hZvoStfUJ6kRVaf.json'}

exec(code, env_args)
