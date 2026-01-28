code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load(var_call_RVwaV2L2OvFnh9R0bVuR4tos)
ppv = load(var_call_BHhocw6sm87PwMHNmWbmxfMc)
pi = load(var_call_77QdymA9rlNoFeElaKhXd4MQ)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per NPM package by max UpstreamPublishedAt
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest = pkg_df.sort_values(['Name','UpstreamPublishedAt']).groupby('Name', as_index=False).tail(1)
latest = latest[['Name','Version','UpstreamPublishedAt']].copy()

# map to github project via project_packageversion
m = latest.merge(ppv_df[['Name','Version','ProjectName']], on=['Name','Version'], how='inner')
# if multiple repos per package@version, keep one (arbitrary) but prefer non-null
m = m.dropna(subset=['ProjectName']).drop_duplicates(subset=['Name','Version','ProjectName'])

# parse stars from Project_Information and extract repo
pi_df['ProjectName'] = pi_df['Project_Information'].str.extract(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', expand=False)
pi_df['Stars'] = pi_df['Project_Information'].str.extract(r'([0-9][0-9,]*)\s+stars', expand=False)
pi_df['Stars'] = pi_df['Stars'].str.replace(',','', regex=False)
pi_df['Stars'] = pd.to_numeric(pi_df['Stars'], errors='coerce')

m2 = m.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='left')

# for each package, take max stars among associated repos (in case multiple)
agg = m2.groupby(['Name','Version'], as_index=False)['Stars'].max()
agg = agg.dropna(subset=['Stars'])

# top 5 by stars
agg = agg.sort_values('Stars', ascending=False).head(5)

out = agg.rename(columns={'Name':'Package','Version':'LatestVersion','Stars':'GitHubStars'})
out_rec = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out_rec))"""

env_args = {'var_call_RVwaV2L2OvFnh9R0bVuR4tos': 'file_storage/call_RVwaV2L2OvFnh9R0bVuR4tos.json', 'var_call_BHhocw6sm87PwMHNmWbmxfMc': 'file_storage/call_BHhocw6sm87PwMHNmWbmxfMc.json', 'var_call_77QdymA9rlNoFeElaKhXd4MQ': 'file_storage/call_77QdymA9rlNoFeElaKhXd4MQ.json'}

exec(code, env_args)
