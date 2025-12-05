code = """import json, re
import pandas as pd

path = var_call_30P3Fz53Q3kNEZcKzQmRsmRN
with open(path, 'r') as f:
    data = json.load(f)

rows = []
for rec in data:
    info = rec.get('Patents_info','')
    m = re.search(r'assignee_harmonized: ([^,.;]+)', info)
    if not m:
        continue
    assignee = m.group(1).strip()
    if assignee == 'UNIV CALIFORNIA':
        continue
    if 'UNIV CALIFORNIA' not in rec.get('citation',''):
        continue
    cpc_raw = rec.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    primary_codes = [e['code'] for e in cpc_list if e.get('first')]
    if not primary_codes and cpc_list:
        primary_codes = [cpc_list[0].get('code')]
    for code in primary_codes:
        rows.append({'assignee': assignee, 'cpc_code': code})

if rows:
    df = pd.DataFrame(rows).drop_duplicates()
else:
    df = pd.DataFrame(columns=['assignee','cpc_code'])

codes = df['cpc_code'].dropna().unique().tolist()

result = {'assignee_cpc': df.to_dict(orient='records'), 'codes': codes}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zksCAshBsPZxjsg07ddn9ZuA': [], 'var_call_30P3Fz53Q3kNEZcKzQmRsmRN': 'file_storage/call_30P3Fz53Q3kNEZcKzQmRsmRN.json'}

exec(code, env_args)
