code = """import json, re, pandas as pd

# load possibly large json lists

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_WtqedTw3avLStkfUd11QCdi5)
ppv = load_records(var_call_eeMCQOpeY4Tgp5khVAP9eOG1)
pi = load_records(var_call_iGJyQCu7tkfHFylUBsMXVHYk)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']]
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']]

# join package versions -> github projects
j = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
if j.empty:
    out = []
else:
    projects = j['ProjectName'].dropna().drop_duplicates()

    # parse project_info text for repo and fork count
    info_df = pd.DataFrame(pi)
    def parse_repo_forks(txt):
        if not isinstance(txt, str):
            return None, None
        # repo patterns: 'project owner/repo', 'project named owner/repo', 'project is hosted on GitHub under the name owner/repo'
        m = re.search(r'project(?: named|)\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', txt)
        if not m:
            m = re.search(r'name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', txt)
        if not m:
            m = re.search(r'The project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\s+on GitHub', txt)
        repo = m.group(1) if m else None
        fm = re.search(r'([0-9][0-9,]*)\s+forks?\b', txt)
        forks = int(fm.group(1).replace(',','')) if fm else None
        return repo, forks

    parsed = info_df['Project_Information'].apply(parse_repo_forks)
    info_df['ProjectName'] = parsed.apply(lambda x: x[0])
    info_df['Forks'] = parsed.apply(lambda x: x[1])

    info_df = info_df.dropna(subset=['ProjectName','Forks'])
    info_df = info_df[info_df['ProjectName'].isin(set(projects))]

    # some repos may appear multiple times; take max forks
    agg = info_df.groupby('ProjectName', as_index=False)['Forks'].max()
    top5 = agg.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    out = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WtqedTw3avLStkfUd11QCdi5': 'file_storage/call_WtqedTw3avLStkfUd11QCdi5.json', 'var_call_eeMCQOpeY4Tgp5khVAP9eOG1': 'file_storage/call_eeMCQOpeY4Tgp5khVAP9eOG1.json', 'var_call_iGJyQCu7tkfHFylUBsMXVHYk': 'file_storage/call_iGJyQCu7tkfHFylUBsMXVHYk.json'}

exec(code, env_args)
