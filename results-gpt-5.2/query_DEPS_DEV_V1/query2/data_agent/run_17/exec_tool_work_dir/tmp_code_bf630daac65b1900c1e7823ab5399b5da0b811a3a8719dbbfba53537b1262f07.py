code = """import json, re, pandas as pd

def load_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_result(var_call_P9FifnzBgVOC3Iki6zeVsKzt)
ppv = load_result(var_call_aNfImAahPVjOw6IzIDFj0aBD)
pi = load_result(var_call_YafI0Gdx9DCFBdpfV70lN2Z7)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = merged['ProjectName'].dropna().drop_duplicates()

fork_re = re.compile(r"(?:project(?: is)?(?: named)?\s+)?([\w.-]+/[\w.-]+).*?([0-9][0-9,]*)\s+fork", re.IGNORECASE)

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    m = fork_re.search(s)
    if not m:
        return None, None
    proj = m.group(1)
    forks = int(m.group(2).replace(',', ''))
    return proj, forks

rows = []
for rec in pi:
    proj, forks = parse_info(rec.get('Project_Information'))
    if proj is not None:
        rows.append({'ProjectName': proj, 'Forks': forks})

info_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

cand = pd.DataFrame({'ProjectName': list(projects)})
cand = cand.merge(info_df, on='ProjectName', how='left')
cand = cand.dropna(subset=['Forks'])

top5 = cand.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

out_lines = []
for i, r in enumerate(top5.itertuples(index=False), start=1):
    out_lines.append(f"{i}. {r.ProjectName} — {int(r.Forks)} forks")

result = "\\n".join(out_lines)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_P9FifnzBgVOC3Iki6zeVsKzt': 'file_storage/call_P9FifnzBgVOC3Iki6zeVsKzt.json', 'var_call_aNfImAahPVjOw6IzIDFj0aBD': 'file_storage/call_aNfImAahPVjOw6IzIDFj0aBD.json', 'var_call_YafI0Gdx9DCFBdpfV70lN2Z7': 'file_storage/call_YafI0Gdx9DCFBdpfV70lN2Z7.json'}

exec(code, env_args)
