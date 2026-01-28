code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load(var_call_XjtycDmY3d8OQChj3WXp0GRr)
ppv = load(var_call_wd6v0RFfTFK6Cddbq56Q5a6U)
pi = load(var_call_QQnCoxURPgCQ14T5nUg5VCTT)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = set(m['ProjectName'].dropna().unique().tolist())

pat = re.compile(r"project\s+([^\s]+/[^\s]+).*?([0-9,]+)\s+fork", re.IGNORECASE)
rows=[]
for rec in pi:
    s = rec.get('Project_Information') or ''
    m2 = pat.search(s)
    if not m2:
        continue
    proj = m2.group(1).strip().rstrip('.,')
    forks = int(m2.group(2).replace(',',''))
    if proj in projects:
        rows.append({'ProjectName':proj,'Forks':forks})

res_df = pd.DataFrame(rows)
if res_df.empty:
    out = json.dumps([])
else:
    res_df = res_df.sort_values('Forks', ascending=False).drop_duplicates('ProjectName')
    top5 = res_df.head(5).to_dict('records')
    out = json.dumps(top5)

print('__RESULT__:')
print(out)"""

env_args = {'var_call_XjtycDmY3d8OQChj3WXp0GRr': 'file_storage/call_XjtycDmY3d8OQChj3WXp0GRr.json', 'var_call_wd6v0RFfTFK6Cddbq56Q5a6U': 'file_storage/call_wd6v0RFfTFK6Cddbq56Q5a6U.json', 'var_call_QQnCoxURPgCQ14T5nUg5VCTT': 'file_storage/call_QQnCoxURPgCQ14T5nUg5VCTT.json'}

exec(code, env_args)
