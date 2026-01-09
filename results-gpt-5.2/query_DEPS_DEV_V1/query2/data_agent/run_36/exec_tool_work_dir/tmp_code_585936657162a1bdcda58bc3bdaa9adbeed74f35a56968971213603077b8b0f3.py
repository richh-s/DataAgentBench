code = """import json, re, pandas as pd

# Load big results

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_5Qe4dj4fOAFrcgI4sOB6v29l)
ppv = load_var(var_call_tqBHMarwa6P40Vg6HrWiln4R)
pi = load_var(var_call_EXjhlxvyKQ63EkQ2ePLkzOw2)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

# join on package version -> github project
j = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
# unique projects
projects = j[['ProjectName']].drop_duplicates()

# parse project_info to extract ProjectName and forks
rows=[]
pat = re.compile(r"project\s+([^\s]+/[^\s]+)")
pat2 = re.compile(r"(\d[\d,]*)\s+forks")
for rec in pi:
    info = rec.get('Project_Information') or ''
    m = pat.search(info)
    if not m:
        continue
    pname = m.group(1).strip().rstrip('.,;')
    m2 = pat2.search(info)
    forks = None
    if m2:
        forks = int(m2.group(1).replace(',',''))
    rows.append({'ProjectName': pname, 'Forks': forks})

pi_df = pd.DataFrame(rows).dropna(subset=['Forks']).drop_duplicates(subset=['ProjectName'])

merged = projects.merge(pi_df, on='ProjectName', how='inner')

top5 = merged.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5Qe4dj4fOAFrcgI4sOB6v29l': 'file_storage/call_5Qe4dj4fOAFrcgI4sOB6v29l.json', 'var_call_tqBHMarwa6P40Vg6HrWiln4R': 'file_storage/call_tqBHMarwa6P40Vg6HrWiln4R.json', 'var_call_EXjhlxvyKQ63EkQ2ePLkzOw2': 'file_storage/call_EXjhlxvyKQ63EkQ2ePLkzOw2.json'}

exec(code, env_args)
