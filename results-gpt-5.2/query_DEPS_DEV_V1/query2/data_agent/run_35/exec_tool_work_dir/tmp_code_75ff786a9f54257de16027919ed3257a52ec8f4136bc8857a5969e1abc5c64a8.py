code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_RuRJ0ihdyOQjUfFPbmQpiQAO)
mapr = load_records(var_call_O12RpxraQP16WyZaqbkllL0N)
projinfo = load_records(var_call_fIux9Z2WSqXAUyj3QdjrIiAA)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version','Licenses','VersionInfo']].drop_duplicates()
map_df = pd.DataFrame(mapr)[['System','Name','Version','ProjectName']].drop_duplicates()

# Join package versions to github projects
j = pkg_df.merge(map_df, on=['System','Name','Version'], how='inner')

# normalize MIT license check using package Licenses string
j = j[j['Licenses'].astype(str).str.contains('"MIT"', regex=False)]

# Get unique projects
projects = j[['ProjectName']].drop_duplicates()

# Parse forks count from Project_Information strings; also extract project name
rows=[]
for rec in projinfo:
    s = rec.get('Project_Information','') or ''
    mname = re.search(r'project\s+([^\s]+/[^\s]+)', s, re.IGNORECASE)
    if not mname:
        mname = re.search(r'project\s+named\s+([^\s]+/[^\s]+)', s, re.IGNORECASE)
    if not mname:
        mname = re.search(r'GitHub\s+under\s+the\s+name\s+([^\s]+/[^\s,]+)', s, re.IGNORECASE)
    if not mname:
        continue
    pname = mname.group(1).strip().rstrip(',').rstrip('.')
    mforks = re.search(r'([0-9,]+)\s+forks?', s, re.IGNORECASE)
    forks = int(mforks.group(1).replace(',','')) if mforks else None
    rows.append({'ProjectName': pname, 'forks': forks})

pi_df = pd.DataFrame(rows).dropna(subset=['forks']).drop_duplicates(subset=['ProjectName'])

merged = projects.merge(pi_df, on='ProjectName', how='inner')

top5 = merged.sort_values(['forks','ProjectName'], ascending=[False, True]).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_jcEYELdQvblFXsHWYwdPXoDt': ['packageinfo'], 'var_call_yvHb2QUM7GdSANCH1Z0YCkFP': ['project_info', 'project_packageversion'], 'var_call_RuRJ0ihdyOQjUfFPbmQpiQAO': 'file_storage/call_RuRJ0ihdyOQjUfFPbmQpiQAO.json', 'var_call_O12RpxraQP16WyZaqbkllL0N': 'file_storage/call_O12RpxraQP16WyZaqbkllL0N.json', 'var_call_fIux9Z2WSqXAUyj3QdjrIiAA': 'file_storage/call_fIux9Z2WSqXAUyj3QdjrIiAA.json'}

exec(code, env_args)
