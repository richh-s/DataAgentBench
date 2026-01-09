code = """import json, re, pandas as pd

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

pi_src = var_call_CuGasJqqcFtP6qp4SVCjeQvv
if isinstance(pi_src, str):
    with open(pi_src, 'r') as f:
        pi_rows = json.load(f)
else:
    pi_rows = pi_src

pkg_df = pd.DataFrame(pkg_rows)[['System','Name','Version']]
ppv_df = pd.DataFrame(ppv_rows)[['System','Name','Version','ProjectName']]

mapped = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = set(mapped['ProjectName'].dropna().astype(str))

# parse project_info text
fork_re = re.compile(r'(?:forks count of|forked\s+|forks\s*(?:count)?\s*[:=]?\s*)([0-9][0-9,]*)', re.IGNORECASE)
repo_re = re.compile(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')

rows = []
for rec in pi_rows:
    text = rec.get('Project_Information') or ''
    mrepo = repo_re.search(text)
    if not mrepo:
        continue
    repo = mrepo.group(1)
    if repo not in projects:
        continue
    mf = fork_re.search(text)
    if not mf:
        continue
    forks = int(mf.group(1).replace(',',''))
    rows.append((repo, forks))

fork_df = pd.DataFrame(rows, columns=['ProjectName','Forks'])
# if multiple entries per repo, take max
fork_df = fork_df.groupby('ProjectName', as_index=False)['Forks'].max()

# take top 5
fork_df = fork_df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = fork_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0pcdKayhxvcrynnDCx115Yfq': 'file_storage/call_0pcdKayhxvcrynnDCx115Yfq.json', 'var_call_TpAs4zLCeG1KAWDDMKpk2cGP': 'file_storage/call_TpAs4zLCeG1KAWDDMKpk2cGP.json', 'var_call_ZkQJIhcOCJJwrTmrGxxid0I6': {'n_pkg_versions': 176998, 'n_mapped_versions': 378738, 'n_projects': 5336, 'sample_query': "SELECT Project_Information FROM project_info WHERE Project_Information LIKE '%/crislin2046%' OR Project_Information LIKE '%/robpethick%' OR Project_Information LIKE '%0x1ance/soulbound%' OR Project_Information LIKE '%0x1ance/wishport%' OR Project_Information LIKE '%0xsalah/tete%' OR Project_Information LIKE '%1394/manipula%' OR Project_Information LIKE '%1728954833/project-manager%' OR Project_Information LIKE '%20lives/scad-js%' OR Project_Information LIKE '%286810/react-native-switch-box%' OR "}, 'var_call_CuGasJqqcFtP6qp4SVCjeQvv': 'file_storage/call_CuGasJqqcFtP6qp4SVCjeQvv.json'}

exec(code, env_args)
