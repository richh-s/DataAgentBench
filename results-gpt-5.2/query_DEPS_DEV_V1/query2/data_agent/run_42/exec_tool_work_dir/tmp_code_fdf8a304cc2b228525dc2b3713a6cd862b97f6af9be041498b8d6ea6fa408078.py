code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_4RF5jxNNoQ9G6uZ4A2s1250o)
ppv = load_records(var_call_jUATAf6ZLN3t0p9wOYN20HdX)
pi = load_records(var_call_QAOKnjLKBuEqShIFi5eCoXHL)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
# join on System/Name/Version to get projectname for MIT release packages
j = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
# unique projects
projects = j[['ProjectName']].drop_duplicates()

# parse project_info Project_Information to extract owner/repo and forks
info_rows = []
pat_repo = re.compile(r'project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', re.IGNORECASE)
pat_forks = re.compile(r'(?:and\s+)?(\d[\d,]*)\s+forks', re.IGNORECASE)
for rec in pi:
    s = rec.get('Project_Information') if isinstance(rec, dict) else None
    if not s or not isinstance(s, str):
        continue
    mrepo = pat_repo.search(s)
    mforks = pat_forks.search(s)
    if not mrepo or not mforks:
        continue
    repo = mrepo.group(1)
    forks = int(mforks.group(1).replace(',',''))
    info_rows.append({'ProjectName': repo, 'Forks': forks, 'Project_Information': s})

df_info = pd.DataFrame(info_rows).drop_duplicates(subset=['ProjectName'])

# filter to projects from MIT release packages
cand = projects.merge(df_info, on='ProjectName', how='inner')

# get top 5 by forks
cand_sorted = cand.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

out = cand_sorted[['ProjectName','Forks']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4RF5jxNNoQ9G6uZ4A2s1250o': 'file_storage/call_4RF5jxNNoQ9G6uZ4A2s1250o.json', 'var_call_jUATAf6ZLN3t0p9wOYN20HdX': 'file_storage/call_jUATAf6ZLN3t0p9wOYN20HdX.json', 'var_call_QAOKnjLKBuEqShIFi5eCoXHL': 'file_storage/call_QAOKnjLKBuEqShIFi5eCoXHL.json'}

exec(code, env_args)
