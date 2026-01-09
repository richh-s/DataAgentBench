code = """import json, re, pandas as pd

# load package rows
pkg_src = var_call_0pcdKayhxvcrynnDCx115Yfq
if isinstance(pkg_src, str):
    with open(pkg_src, 'r') as f:
        pkg_rows = json.load(f)
else:
    pkg_rows = pkg_src

ppv_src = var_call_TpAs4zLCeG1KAWDDMKpk2cGP
if isinstance(ppv_src, str):
    with open(ppv_src, 'r') as f:
        ppv_rows = json.load(f)
else:
    ppv_rows = ppv_src

pkg_df = pd.DataFrame(pkg_rows)
ppv_df = pd.DataFrame(ppv_rows)

# inner join on System,Name,Version to keep only MIT+release package versions that have github mapping
m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# unique projects
projects = sorted(set(m['ProjectName'].dropna().astype(str)))

# regex to extract fork count from Project_Information text
fork_re = re.compile(r'Forks\s*[:=]\s*([0-9][0-9,]*)', re.IGNORECASE)

# query project_info in chunks using LIKE on Project_Information (contains owner/repo)
chunks = [projects[i:i+200] for i in range(0, len(projects), 200)]
queries = []
for ch in chunks:
    cond = ' OR '.join([f"Project_Information LIKE '%{p.replace("'","''")}%'" for p in ch])
    q = f"SELECT Project_Information FROM project_info WHERE {cond};"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'n_pkg_versions': int(len(pkg_df)), 'n_mapped_versions': int(len(m)), 'n_projects': int(len(projects)), 'sample_query': queries[0][:500]}))"""

env_args = {'var_call_0pcdKayhxvcrynnDCx115Yfq': 'file_storage/call_0pcdKayhxvcrynnDCx115Yfq.json', 'var_call_TpAs4zLCeG1KAWDDMKpk2cGP': 'file_storage/call_TpAs4zLCeG1KAWDDMKpk2cGP.json'}

exec(code, env_args)
