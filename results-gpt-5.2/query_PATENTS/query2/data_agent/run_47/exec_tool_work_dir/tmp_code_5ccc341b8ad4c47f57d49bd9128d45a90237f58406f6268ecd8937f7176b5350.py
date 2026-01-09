code = """import json, re, pandas as pd
from datetime import datetime

# load data
path = var_call_cnNoynNR4xW0vhvRiavHqmMK
with open(path,'r',encoding='utf-8') as f:
    rows = json.load(f)

def parse_year(date_str):
    if not date_str: return None
    m = re.search(r'(19|20)\d{2}', date_str)
    return int(m.group(0)) if m else None

def is_germany(patents_info):
    if not patents_info: return False
    # patterns: 'The DE patent application', 'In DE,' 'from DE'
    return bool(re.search(r'\bDE\b', patents_info) or re.search(r'The\s+DE\s+patent\s+application', patents_info) or re.search(r'In\s+DE\b', patents_info))

def grant_in_H2_2019(grant_date):
    if not grant_date: return False
    if '2019' not in grant_date: return False
    # month names
    return any(mon in grant_date for mon in ['July','August','September','October','November','December'])

def cpc_level4(code):
    if not code: return None
    code = code.strip()
    if '/' in code:
        left,right = code.split('/',1)
        main = right
    else:
        left, main = code, ''
    # keep first 4 digits after class letter(s)
    m = re.match(r'^([A-HY]\d{2})([A-Z]?)(\d{1,4})', left)
    if not m:
        return None
    sec = m.group(1)
    sub = m.group(2)
    digits = m.group(3).ljust(4,'0')[:4]
    return f"{sec}{sub}{digits}/00"

records=[]
for r in rows:
    if not grant_in_H2_2019(r.get('grant_date')): 
        continue
    if not is_germany(r.get('Patents_info','')):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    cpc_str = r.get('cpc')
    if not cpc_str:
        continue
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        continue
    codes=set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry,dict) else None
        lvl4 = cpc_level4(code)
        if lvl4:
            codes.add(lvl4)
    for lvl4 in codes:
        records.append({'cpc4':lvl4,'filing_year':fy})

df=pd.DataFrame(records)
if df.empty:
    out=[]
else:
    counts=df.groupby(['cpc4','filing_year']).size().reset_index(name='filings')

    alpha=0.1
    res=[]
    for cpc4, g in counts.groupby('cpc4'):
        g=g.sort_values('filing_year')
        ema=None
        for _,row in g.iterrows():
            x=float(row['filings'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            res.append({'cpc4':cpc4,'year':int(row['filing_year']),'ema':ema})
    ema_df=pd.DataFrame(res)
    # choose best year per group
    best=ema_df.sort_values(['cpc4','ema','year'],ascending=[True,False,True]).groupby('cpc4').head(1)
    # find max ema across groups
    max_ema=best['ema'].max() if not best.empty else None
    top=best[best['ema']==max_ema].copy() if max_ema is not None else best
    out=top.sort_values('cpc4').to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FZU99h3OjA35Qt6iUoghhjZN': ['publicationinfo'], 'var_call_rOqnuIgr3dqs27or592Xe22L': ['cpc_definition'], 'var_call_cnNoynNR4xW0vhvRiavHqmMK': 'file_storage/call_cnNoynNR4xW0vhvRiavHqmMK.json'}

exec(code, env_args)
