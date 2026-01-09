code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_TyKo4w4PFjsjBMRx6p9huDCN)
ppv = load_records(var_call_Tqlka6yRDyF2ECJ6dmMSBY7j)
pi = load_records(var_call_sgeHDZIFraeMQbE4GAAfgvfM)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = m[['ProjectName']].drop_duplicates()

pat = re.compile(r"project\s+([^\s]+/[^\s]+).*?\b(\d[\d,]*)\s+forks\b", re.IGNORECASE)
rows=[]
for rec in pi:
    s = rec.get('Project_Information') or ''
    mt = pat.search(s)
    if mt:
        pname = mt.group(1).strip().rstrip('.')
        forks = int(mt.group(2).replace(',',''))
        rows.append({'ProjectName': pname, 'Forks': forks})

pi_df = pd.DataFrame(rows)
if len(pi_df)==0:
    out = []
else:
    pi_df = pi_df.drop_duplicates(subset=['ProjectName'])
    joined = projects.merge(pi_df, on='ProjectName', how='inner')
    res = joined.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    out = res.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps({'matched_projects': int(projects.shape[0]), 'parsed_projectinfo': int(len(pi_df)) if 'pi_df' in locals() else 0, 'top5': out} برد) )"""

env_args = {'var_call_TyKo4w4PFjsjBMRx6p9huDCN': 'file_storage/call_TyKo4w4PFjsjBMRx6p9huDCN.json', 'var_call_Tqlka6yRDyF2ECJ6dmMSBY7j': 'file_storage/call_Tqlka6yRDyF2ECJ6dmMSBY7j.json', 'var_call_sgeHDZIFraeMQbE4GAAfgvfM': 'file_storage/call_sgeHDZIFraeMQbE4GAAfgvfM.json'}

exec(code, env_args)
