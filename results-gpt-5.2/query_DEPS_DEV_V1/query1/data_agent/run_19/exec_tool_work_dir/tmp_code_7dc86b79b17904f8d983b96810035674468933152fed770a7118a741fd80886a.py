code = """import json, re
import pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = pd.DataFrame(load(var_call_Argk8Yy8CnPWBD9d4htS4urI))
ppv = pd.DataFrame(load(var_call_z3i1T7WbBwyJn7fbPcBWrtBm))
pi = pd.DataFrame(load(var_call_dyI4UHNuuO9PnhLunIrqpImY))

# latest version per package name by max UpstreamPublishedAt
pkg['UpstreamPublishedAt'] = pd.to_numeric(pkg['UpstreamPublishedAt'], errors='coerce')
pkg = pkg.dropna(subset=['UpstreamPublishedAt'])
idx = pkg.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = pkg.loc[idx, ['Name','Version']].reset_index(drop=True)

# map latest package versions to github projects
m = latest.merge(ppv[['Name','Version','ProjectName']], on=['Name','Version'], how='inner').dropna(subset=['ProjectName'])

# extract projectname and stars from Project_Information
# pattern: "project owner/repo" and "<stars> stars"
info = pi.copy()
info['ProjectName'] = info['Project_Information'].str.extract(r'project\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)')
info['Stars'] = info['Project_Information'].str.extract(r'([0-9][0-9,]*)\s+stars')[0]
info['Stars'] = info['Stars'].str.replace(',','', regex=False)
info['Stars'] = pd.to_numeric(info['Stars'], errors='coerce')
info = info.dropna(subset=['ProjectName','Stars'])

# join to get stars
j = m.merge(info[['ProjectName','Stars']], on='ProjectName', how='inner')

# for packages that map to multiple repos, take max stars
agg = j.groupby(['Name','Version'], as_index=False)['Stars'].max()

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Argk8Yy8CnPWBD9d4htS4urI': 'file_storage/call_Argk8Yy8CnPWBD9d4htS4urI.json', 'var_call_z3i1T7WbBwyJn7fbPcBWrtBm': 'file_storage/call_z3i1T7WbBwyJn7fbPcBWrtBm.json', 'var_call_dyI4UHNuuO9PnhLunIrqpImY': 'file_storage/call_dyI4UHNuuO9PnhLunIrqpImY.json'}

exec(code, env_args)
