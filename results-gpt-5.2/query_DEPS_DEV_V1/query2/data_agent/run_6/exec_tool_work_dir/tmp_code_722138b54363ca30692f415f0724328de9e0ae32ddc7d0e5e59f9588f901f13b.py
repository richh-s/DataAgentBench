code = """import json, re, pandas as pd

pk = var_call_1Gse5ns860u3oQTsnqkupzVL
if isinstance(pk, str):
    with open(pk, 'r') as f:
        pk = json.load(f)
ppv = var_call_ksUGv0abpzsSpI0EUAJjH1j6
if isinstance(ppv, str):
    with open(ppv, 'r') as f:
        ppv = json.load(f)
pi = var_call_mGQrkmtTznKa6WjviUtwL0Fb
if isinstance(pi, str):
    with open(pi, 'r') as f:
        pi = json.load(f)

pk_df = pd.DataFrame(pk).drop_duplicates(subset=['System','Name','Version'])
ppv_df = pd.DataFrame(ppv).drop_duplicates(subset=['System','Name','Version','ProjectName'])

m_df = pk_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
proj_names = set(m_df['ProjectName'].dropna().unique().tolist())

rows = []
pat_proj = re.compile(r'project\s+([^\s]+/[^\s]+)')
pat_forks = re.compile(r'(\d[\d,]*)\s+forks?')

for rec in pi:
    s = rec.get('Project_Information') or ''
    m1 = pat_proj.search(s)
    m2 = pat_forks.search(s)
    if not m1 or not m2:
        continue
    pname = m1.group(1).rstrip('.,)')
    forks = int(m2.group(1).replace(',', ''))
    if pname in proj_names:
        rows.append({'ProjectName': pname, 'Forks': forks})

info_df = pd.DataFrame(rows)
if info_df.empty:
    ans = 'No matching projects found.'
else:
    info_df = info_df.groupby('ProjectName', as_index=False)['Forks'].max()
    mp = m_df[['ProjectName','Name']].dropna().drop_duplicates()
    joined = info_df.merge(mp, on='ProjectName', how='left')
    joined = joined.sort_values(['Forks','ProjectName'], ascending=[False, True])
    joined['pkg_rank'] = joined.groupby('ProjectName')['Name'].rank(method='first')
    rep = joined[joined['pkg_rank'] == 1][['ProjectName','Forks','Name']].rename(columns={'Name':'ExampleNpmPackage'})
    rep = rep.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    lines = []
    for i, r in enumerate(rep.itertuples(index=False), 1):
        lines.append(str(i) + '. ' + r.ProjectName + ' — forks: ' + str(int(r.Forks)) + ' (example NPM package: ' + str(r.ExampleNpmPackage) + ')')
    ans = '\n'.join(lines)

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_1Gse5ns860u3oQTsnqkupzVL': 'file_storage/call_1Gse5ns860u3oQTsnqkupzVL.json', 'var_call_ksUGv0abpzsSpI0EUAJjH1j6': 'file_storage/call_ksUGv0abpzsSpI0EUAJjH1j6.json', 'var_call_mGQrkmtTznKa6WjviUtwL0Fb': 'file_storage/call_mGQrkmtTznKa6WjviUtwL0Fb.json'}

exec(code, env_args)
