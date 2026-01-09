code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_SF2gOP4IN48fNKlnKM9sXKOC)
ppv = load_records(var_call_IwE5HzAxCnJOblCeWUcvFTnb)
pi = load_records(var_call_SGcjR7wXK6MpsTjIpyK83EAo)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
df_map = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
projects_set = set(df_map['ProjectName'].dropna().astype(str))

# parse project_info text
rows=[]
pat_repo = re.compile(r"project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
pat_repo2 = re.compile(r"under\s+the\s+name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
pat_forks = re.compile(r"([0-9][0-9,]*)\s+forks?", re.IGNORECASE)

for rec in pi:
    text = rec.get('Project_Information') or ''
    m = pat_repo.search(text) or pat_repo2.search(text)
    if not m:
        continue
    repo = m.group(1)
    mf = pat_forks.search(text)
    if not mf:
        continue
    forks = int(mf.group(1).replace(',',''))
    rows.append((repo, forks, text))

df_pi = pd.DataFrame(rows, columns=['ProjectName','Forks','Project_Information'])

# keep only projects referenced by MIT-release npm packages
df_filt = df_pi[df_pi['ProjectName'].isin(projects_set)].copy()

# for each project, take max forks (should be same)
df_best = df_filt.groupby('ProjectName', as_index=False)['Forks'].max()

df_top = df_best.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = df_top.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_SF2gOP4IN48fNKlnKM9sXKOC': 'file_storage/call_SF2gOP4IN48fNKlnKM9sXKOC.json', 'var_call_IwE5HzAxCnJOblCeWUcvFTnb': 'file_storage/call_IwE5HzAxCnJOblCeWUcvFTnb.json', 'var_call_EbJDWs7fGebXj6YL2NdX3QTd': {'need_project_info_query': True, 'unique_projects_count': 5289, 'sample_projects': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0xsalah/tete', '1394/manipula', '1728954833/project-manager', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4catalyzer/theme', '4x-sas/create-react-app', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client']}, 'var_call_SGcjR7wXK6MpsTjIpyK83EAo': 'file_storage/call_SGcjR7wXK6MpsTjIpyK83EAo.json'}

exec(code, env_args)
