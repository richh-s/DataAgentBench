code = """import json, re, pandas as pd

# load large json lists

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

pkg = load_records(var_call_zkTTZOllUorykpZ6i1TGa6GY)
ppv = load_records(var_call_VuFMDeZkqVUbCtqFHzj91mIK)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

# ensure numeric
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')

# latest release per package
pkg_df = pkg_df.dropna(subset=['Name','Version','UpstreamPublishedAt'])
idx = pkg_df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = pkg_df.loc[idx, ['Name','Version']].copy()

# join to github mapping
m = latest.merge(ppv_df[['Name','Version','ProjectName']], on=['Name','Version'], how='inner')

# pick one repo per package (most frequent)
repo_choice = (m.groupby(['Name','Version','ProjectName']).size().reset_index(name='n')
               .sort_values(['Name','Version','n'], ascending=[True,True,False]))
repo_choice = repo_choice.drop_duplicates(subset=['Name','Version'])

repos = repo_choice['ProjectName'].dropna().unique().tolist()

# chunk repos for SQL IN
chunks = [repos[i:i+500] for i in range(0, len(repos), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + r.replace("'","''") + "'" for r in ch])
    queries.append(f"SELECT Project_Information FROM project_info WHERE Project_Information IN ({in_list});")

out = {'repo_choice': repo_choice[['Name','Version','ProjectName']].to_dict(orient='records'), 'queries': queries}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zkTTZOllUorykpZ6i1TGa6GY': 'file_storage/call_zkTTZOllUorykpZ6i1TGa6GY.json', 'var_call_VuFMDeZkqVUbCtqFHzj91mIK': 'file_storage/call_VuFMDeZkqVUbCtqFHzj91mIK.json'}

exec(code, env_args)
