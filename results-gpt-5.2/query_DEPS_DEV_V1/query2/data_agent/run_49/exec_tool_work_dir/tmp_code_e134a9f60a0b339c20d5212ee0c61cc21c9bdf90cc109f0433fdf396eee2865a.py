code = """import json, re, pandas as pd

def load_json(src):
    if isinstance(src, str):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    return src

pkg = load_json(var_call_GlNNnyMb69TWJx4a4R9tuk7Z)
ppv = load_json(var_call_7u2tUvAzKZAQepeZPXNyzJaR)
pi = load_json(var_call_rzRphn15kpLUAwQRT9gPYfG2)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
proj_set = set(merged['ProjectName'].dropna().unique().tolist())

# Parse ProjectName and fork counts from Project_Information strings
rows = []
pat1 = re.compile(r"project\s+(?:named\s+|is hosted on GitHub under the name\s+|is hosted on GitHub and currently has\s+|)([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
pat_forks = re.compile(r"([0-9][0-9,]*)\s+forks?", re.IGNORECASE)

for rec in pi:
    s = rec.get('Project_Information') or ''
    m = pat1.search(s)
    if not m:
        # alternative phrasing: "The project owner/repo on GitHub"
        m = re.search(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\s+on GitHub", s)
    if not m:
        continue
    pname = m.group(1)
    fm = pat_forks.search(s)
    if not fm:
        continue
    forks = int(fm.group(1).replace(',',''))
    rows.append((pname, forks))

pi_df = pd.DataFrame(rows, columns=['ProjectName','Forks'])
# if duplicates, take max forks
pi_df = pi_df.groupby('ProjectName', as_index=False)['Forks'].max()

cand = pi_df[pi_df['ProjectName'].isin(proj_set)].copy()
# top 5 by forks
cand = cand.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = cand.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GlNNnyMb69TWJx4a4R9tuk7Z': 'file_storage/call_GlNNnyMb69TWJx4a4R9tuk7Z.json', 'var_call_7u2tUvAzKZAQepeZPXNyzJaR': 'file_storage/call_7u2tUvAzKZAQepeZPXNyzJaR.json', 'var_call_0JZgEab9DGkJueopROQX0AMe': {'need_project_info': True, 'project_count': 5289}, 'var_call_rzRphn15kpLUAwQRT9gPYfG2': 'file_storage/call_rzRphn15kpLUAwQRT9gPYfG2.json'}

exec(code, env_args)
