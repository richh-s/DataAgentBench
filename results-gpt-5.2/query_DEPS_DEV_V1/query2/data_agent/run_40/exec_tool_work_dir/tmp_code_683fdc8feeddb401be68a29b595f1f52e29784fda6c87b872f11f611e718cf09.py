code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_maybe_path(var_call_ZE9KN9DOlI7j7zVOCa3r3FqT)
ppv = load_maybe_path(var_call_ww7i2MXMtA5uvgeQwPLi9f81)
pi = load_maybe_path(var_call_FhD4S8krAStrLmiGyy7r2oUI)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].dropna().drop_duplicates()

df = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
proj_names = set(df['ProjectName'].astype(str))

name_pat = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
fork_pat1 = re.compile(r"\b([0-9][0-9,]*)\s+forks\b", re.IGNORECASE)
fork_pat2 = re.compile(r"forks\s+count\s+of\s+([0-9][0-9,]*)", re.IGNORECASE)
fork_pat3 = re.compile(r"been\s+forked\s+([0-9][0-9,]*)\s+times", re.IGNORECASE)

rows=[]
for rec in pi:
    t = rec.get('Project_Information')
    if not isinstance(t,str):
        continue
    m = name_pat.search(t)
    if not m:
        continue
    pname = m.group(1)
    if pname not in proj_names:
        continue
    mf = fork_pat1.search(t) or fork_pat2.search(t) or fork_pat3.search(t)
    if not mf:
        continue
    forks = int(mf.group(1).replace(',',''))
    rows.append({'ProjectName': pname, 'Forks': forks})

df_f = pd.DataFrame(rows)
if len(df_f)==0:
    result=[]
else:
    df_f = df_f.drop_duplicates('ProjectName')
    top5 = df_f.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZE9KN9DOlI7j7zVOCa3r3FqT': 'file_storage/call_ZE9KN9DOlI7j7zVOCa3r3FqT.json', 'var_call_ww7i2MXMtA5uvgeQwPLi9f81': 'file_storage/call_ww7i2MXMtA5uvgeQwPLi9f81.json', 'var_call_FhD4S8krAStrLmiGyy7r2oUI': 'file_storage/call_FhD4S8krAStrLmiGyy7r2oUI.json', 'var_call_VhucjoAshOLRzdU24ovCtJHi': [], 'var_call_t1kUjKcXcmnAzEy8sgbAN9kG': [], 'var_call_djVKSWnPW9SczZVTuvT0971t': ['The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'], 'var_call_KnPghQKbzV3OsIYnqbwQTgD3': {'matched_projects': 5289, 'parsed_projects': 0, 'top5': []}, 'var_call_SMXWvC5ViWe6WCeGi3ngpwr3': {'proj_names': 5289, 'names_in_pi': 0, 'intersection': 0, 'intersection_sample': []}, 'var_call_RlQJB7blYfuDoOBigtmTkYa7': {'cnt_cs': 0, 'cnt_ci': 0, 'checked': 5000}, 'var_call_7aABM2WQJHA53YvbLpIeYp4n': {'matches': 0, 'unique_names': 0, 'sample': []}, 'var_call_X8xrxZJxKL0gReZ9XmtYc6iQ': {'idx': 1, 'text': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, 'var_call_mqBMfxwusTz7XFObGb0GAzJL': {'match': None}, 'var_call_3t8mM6IOXIE2TxKc9qmI9H1T': {'pos': 4, 'slice': 'project leaflet/leaflet on GitHub is a p', 'codes': [112, 114, 111, 106, 101, 99, 116, 32, 108, 101, 97, 102, 108, 101, 116]}, 'var_call_mMHG4currcCfanCwg8kIguiu': {'found': True, 'grp': 'leaflet/leaflet'}}

exec(code, env_args)
