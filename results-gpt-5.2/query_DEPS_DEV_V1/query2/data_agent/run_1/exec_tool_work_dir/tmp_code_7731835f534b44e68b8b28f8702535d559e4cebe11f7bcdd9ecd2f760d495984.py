code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        # file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_BbdzBgwIjVhhOJRjiCVJgMbu)
ppv = load_records(var_call_hfCYVjcn9dTYbpxIkKGqd2L6)
pi = load_records(var_call_7tTlqZunTNKW2GTccm3hTGQo)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
# unique projects
projects = m[['ProjectName']].drop_duplicates()

pi_df = pd.DataFrame(pi)
# extract owner/repo from Project_Information
pi_df['ProjectName'] = pi_df['Project_Information'].str.extract(r'The project (?:named )?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', expand=False)
# fallback patterns
mask = pi_df['ProjectName'].isna()
pi_df.loc[mask, 'ProjectName'] = pi_df.loc[mask, 'Project_Information'].str.extract(r'project (?:is )?hosted on GitHub (?:under the name )?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', expand=False)
mask = pi_df['ProjectName'].isna()
pi_df.loc[mask, 'ProjectName'] = pi_df.loc[mask, 'Project_Information'].str.extract(r'GitHub project (?:named )?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', expand=False)

# extract forks
pi_df['forks'] = pi_df['Project_Information'].str.extract(r'([0-9][0-9,]*) forks', expand=False)
pi_df['forks'] = pi_df['forks'].str.replace(',','', regex=False)
pi_df['forks'] = pd.to_numeric(pi_df['forks'], errors='coerce')

joined = projects.merge(pi_df[['ProjectName','forks']], on='ProjectName', how='left')
joined = joined.dropna(subset=['forks'])
# In case multiple entries per project, take max forks
joined = joined.groupby('ProjectName', as_index=False)['forks'].max()

top5 = joined.sort_values(['forks','ProjectName'], ascending=[False, True]).head(5)
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BbdzBgwIjVhhOJRjiCVJgMbu': 'file_storage/call_BbdzBgwIjVhhOJRjiCVJgMbu.json', 'var_call_hfCYVjcn9dTYbpxIkKGqd2L6': 'file_storage/call_hfCYVjcn9dTYbpxIkKGqd2L6.json', 'var_call_7tTlqZunTNKW2GTccm3hTGQo': 'file_storage/call_7tTlqZunTNKW2GTccm3hTGQo.json'}

exec(code, env_args)
