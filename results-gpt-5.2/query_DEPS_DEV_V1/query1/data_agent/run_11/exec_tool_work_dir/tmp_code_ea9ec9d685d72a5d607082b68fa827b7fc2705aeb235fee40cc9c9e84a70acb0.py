code = """import json, re, pandas as pd

# Load packageinfo result (may be file path)
pi_src = var_call_RIYcCOdoLLu1gxZThVtbsKau
if isinstance(pi_src, str):
    with open(pi_src, 'r', encoding='utf-8') as f:
        pi = json.load(f)
else:
    pi = pi_src

ppv_src = var_call_UJZ6a9Mgixf7T2LuzAWCqzsJ
if isinstance(ppv_src, str):
    with open(ppv_src, 'r', encoding='utf-8') as f:
        ppv = json.load(f)
else:
    ppv = ppv_src

pi_df = pd.DataFrame(pi)
ppv_df = pd.DataFrame(ppv)

# latest version per package by max UpstreamPublishedAt
pi_df['UpstreamPublishedAt'] = pd.to_numeric(pi_df['UpstreamPublishedAt'], errors='coerce')
pi_latest = pi_df.sort_values(['Name','UpstreamPublishedAt','Version']).groupby('Name', as_index=False).tail(1)
pi_latest = pi_latest[['System','Name','Version','UpstreamPublishedAt']]

# join to github mapping
m = pi_latest.merge(ppv_df, on=['System','Name','Version'], how='inner')
# if multiple ProjectName per package-version, keep one (prefer non-null)
m = m.dropna(subset=['ProjectName'])

# extract stars from Project_Information embedded in ProjectName? can't; need query project_info with Project_Information containing ProjectName.
# We'll later query DB for needed ProjectNames.
project_names = sorted(m['ProjectName'].unique().tolist())

out = {
    'latest_mapped_count': int(len(m)),
    'distinct_projects': int(len(project_names)),
    'project_names_sample': project_names[:50]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_RIYcCOdoLLu1gxZThVtbsKau': 'file_storage/call_RIYcCOdoLLu1gxZThVtbsKau.json', 'var_call_UJZ6a9Mgixf7T2LuzAWCqzsJ': 'file_storage/call_UJZ6a9Mgixf7T2LuzAWCqzsJ.json'}

exec(code, env_args)
