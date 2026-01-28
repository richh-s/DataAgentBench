code = """import json, re, pandas as pd
from datetime import datetime

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub_recs = load_records(var_call_Q5RwjP76W25Ze8SWqnMyE4KJ)
def_recs = load_records(var_call_ylBLFrRJinVungfgH2dHmjUx)

def parse_year(date_str):
    if not date_str:
        return None
    m = re.search(r'(19|20)\\d{2}', date_str)
    return int(m.group(0)) if m else None

def parse_cpc_list(cpc_str):
    if not cpc_str:
        return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for e in data:
            code = e.get('code')
            if code:
                codes.append(code)
        return codes
    except Exception:
        return []

def to_level4(code):
    # take first 3 chars as subclass (e.g., H04W), but level-4 in provided CPC definitions is 3 chars like H04
    # Here requirement: CPC group at level 4; given table shows symbols like H04, A61, etc.
    # We'll map any CPC code to first 3 characters (letter+2 digits).
    m = re.match(r'^([A-HY]\\d{2})', code)
    return m.group(1) if m else None

rows=[]
for r in pub_recs:
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    cpcs = parse_cpc_list(r.get('cpc'))
    if not cpcs:
        continue
    lvl4s = {to_level4(c) for c in cpcs}
    lvl4s.discard(None)
    for g in lvl4s:
        rows.append((g, fy))

df = pd.DataFrame(rows, columns=['cpc4','year'])
# counts per year per cpc4
cnt = df.groupby(['cpc4','year']).size().reset_index(name='filings')

alpha=0.1
best_rows=[]
for cpc4, sub in cnt.groupby('cpc4'):
    sub = sub.sort_values('year')
    ema=None
    best_ema=-1
    best_year=None
    for _, row in sub.iterrows():
        x = float(row['filings'])
        ema = x if ema is None else alpha*x + (1-alpha)*ema
        if ema>best_ema:
            best_ema=ema
            best_year=int(row['year'])
    best_rows.append({'cpc_group_code':cpc4,'best_year':best_year,'max_ema_filings':best_ema})

best_df = pd.DataFrame(best_rows)
# join titles
cdf = pd.DataFrame(def_recs)
cdf['level']=cdf['level'].astype(float).astype(int)
cdf = cdf.rename(columns={'symbol':'cpc_group_code','titleFull':'full_title'})[['cpc_group_code','full_title']]
res = best_df.merge(cdf, on='cpc_group_code', how='left')
res = res.sort_values(['max_ema_filings','cpc_group_code'], ascending=[False, True])
# highest EMA areas (ties). take top 10 for readability
out = res.head(10)
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ANhBjmqgwDqx8RoSrAr360aE': [], 'var_call_i0alISgd3YJRa5wDAt2KgX8G': [], 'var_call_ps8eoGeTv1CTJ5PXFxKHDzf9': [{'cnt': '277813'}], 'var_call_n0SIrlHnEJg5R2j2QU6BFnX2': [{'grant_date': '3rd August 2021'}, {'grant_date': 'dated 6th October 2020'}, {'grant_date': '21st of September, 2021'}, {'grant_date': 'on April 7th, 2020'}, {'grant_date': 'Mar 23rd, 2021'}, {'grant_date': '2021 on Mar 2nd'}, {'grant_date': 'November 9th, 2021'}, {'grant_date': '30th Jun 2020'}, {'grant_date': 'on March 16th, 2021'}, {'grant_date': '2021 on Nov 9th'}, {'grant_date': 'December 1st, 2020'}, {'grant_date': '2021 on Oct 5th'}, {'grant_date': 'July the 27th, 2021'}, {'grant_date': '2021 on Jan 26th'}, {'grant_date': 'November the 23rd, 2021'}, {'grant_date': 'September the 28th, 2021'}, {'grant_date': 'on July 21st, 2020'}, {'grant_date': '2021 on Oct 12th'}, {'grant_date': 'dated 16th February 2021'}, {'grant_date': '7th of March, 2023'}], 'var_call_PgJ1Kv458p3pMxQjKP1iJjTd': 'file_storage/call_PgJ1Kv458p3pMxQjKP1iJjTd.json', 'var_call_ynJwJSaVPvIxsCkiZUDaC74j': [], 'var_call_VE87FudSLkEMNxi2KyfIjIow': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.'}, {'Patents_info': 'Patent filing (application no. DE-10200192-A) from DE, held by COPERION GMBH, with publication no. DE-10200192-B4.'}, {'Patents_info': 'Patent filing (application no. DE-10201217-A) from DE, assigned to NEUBAUER KURT MASCHF, with publication no. DE-10201217-B4.'}], 'var_call_Q5RwjP76W25Ze8SWqnMyE4KJ': 'file_storage/call_Q5RwjP76W25Ze8SWqnMyE4KJ.json', 'var_call_N4vnGv5LH1VPblICkgchkoya': [{'cnt': '260808'}], 'var_call_kvy4UnTEzlky19EZ0XmYNEl3': [{'status': 'frozen', 'cnt': '221'}, {'status': 'published', 'cnt': '260587'}], 'var_call_0NS9xd2XcIisjlpH5ueQKyy1': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'status': 'published'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'status': 'published'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'status': 'published'}], 'var_call_ylBLFrRJinVungfgH2dHmjUx': 'file_storage/call_ylBLFrRJinVungfgH2dHmjUx.json'}

exec(code, env_args)
