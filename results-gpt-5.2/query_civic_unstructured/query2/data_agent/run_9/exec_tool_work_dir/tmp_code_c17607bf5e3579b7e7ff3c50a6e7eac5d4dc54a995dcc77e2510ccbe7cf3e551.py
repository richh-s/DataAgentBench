code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_G9PPPAAnLCfzTegQL8L8MWn2)
fund = load_records(var_call_OpiSgCFi4ICBYwei30tOcC07)

df_fund = pd.DataFrame(fund)
df_fund['Amount'] = pd.to_numeric(df_fund['Amount'], errors='coerce').fillna(0).astype(int)

all_text = "\n".join([d.get('text','') for d in docs])
project_names = df_fund['Project_Name'].dropna().unique().tolist()

park_kw = re.compile(r"\bpark\b|playground|bluffs|skate", re.I)

months = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
pattern = r"(Construction was completed|was completed|completed)[^\n\.]{0,100}(" + months + r"\s+2022|2022)"
completed_2022 = re.compile(pattern, re.I)

final_projects = set()
for pn in project_names:
    if not pn or len(pn) < 4:
        continue
    if not park_kw.search(pn):
        continue
    for m in re.finditer(re.escape(pn), all_text):
        window = all_text[m.start():m.start()+500]
        if completed_2022.search(window):
            final_projects.add(pn)
            break

mask = df_fund['Project_Name'].isin(sorted(final_projects))
total = int(df_fund.loc[mask, 'Amount'].sum())

out = {"total_funding": total, "projects": sorted(final_projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_G9PPPAAnLCfzTegQL8L8MWn2': 'file_storage/call_G9PPPAAnLCfzTegQL8L8MWn2.json', 'var_call_OpiSgCFi4ICBYwei30tOcC07': 'file_storage/call_OpiSgCFi4ICBYwei30tOcC07.json'}

exec(code, env_args)
