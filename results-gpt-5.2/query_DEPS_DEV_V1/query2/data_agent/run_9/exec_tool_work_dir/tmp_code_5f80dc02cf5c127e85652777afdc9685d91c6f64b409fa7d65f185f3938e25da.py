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

pat_name = re.compile(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b")
pat_forks = re.compile(r"(\d[\d,]*)\s+forks?\b", re.IGNORECASE)

rows=[]
for rec in pi:
    s = rec.get('Project_Information') or ''
    nm = pat_name.search(s)
    fm = pat_forks.search(s)
    if nm and fm:
        pname = nm.group(1)
        forks = int(fm.group(1).replace(',',''))
        rows.append({'ProjectName': pname, 'Forks': forks})

pi_df = pd.DataFrame(rows)

print('__RESULT__:')
print(json.dumps({'projects_cols': list(projects.columns), 'projects_n': int(len(projects)), 'pi_cols': list(pi_df.columns), 'pi_n': int(len(pi_df))}))"""

env_args = {'var_call_TyKo4w4PFjsjBMRx6p9huDCN': 'file_storage/call_TyKo4w4PFjsjBMRx6p9huDCN.json', 'var_call_Tqlka6yRDyF2ECJ6dmMSBY7j': 'file_storage/call_Tqlka6yRDyF2ECJ6dmMSBY7j.json', 'var_call_sgeHDZIFraeMQbE4GAAfgvfM': 'file_storage/call_sgeHDZIFraeMQbE4GAAfgvfM.json', 'var_call_94aZZ4ZZzjyHL8DPIpCBn7vH': {'matched_projects': 5289, 'parsed_projectinfo': 0, 'top5': []}, 'var_call_fk0nI4Y3bxKhZ3pa7NVhE0RA': {'pat1': [], 'pat2': [], 'pat3': []}, 'var_call_fhPEOrXZRAKgtLlGP1vfg46O': {'sample': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'fork_index': 129, 'context': ' 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized too', 'numforks': ['5782']}}

exec(code, env_args)
