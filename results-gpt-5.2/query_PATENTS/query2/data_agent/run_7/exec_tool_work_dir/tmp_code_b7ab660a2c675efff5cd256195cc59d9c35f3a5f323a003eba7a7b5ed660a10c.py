code = """import json, re
import pandas as pd

# Load publication records (may be file path)
pub_src = var_call_wJ2DYma3EEOa0L0YfFXkDdOv
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

# Load CPC level4 definitions (empty from query due to status field mismatch); we'll re-query later if needed.
level4_defs = var_call_JzdjrwWti86NsnkHOjVecNUw

month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

# Parse month/year from natural language date string
mon_re = re.compile(r'(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*', re.I)
year_re = re.compile(r'(19|20)\d{2}')

def parse_month_year(s):
    if not s:
        return None, None
    s2 = str(s)
    ym = year_re.search(s2)
    year = int(ym.group()) if ym else None
    mm = mon_re.search(s2)
    mon = None
    if mm:
        key = mm.group(0).lower()[:3]
        mon = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}.get(key)
    return mon, year

def is_germany(pat_info):
    return isinstance(pat_info,str) and re.search(r'\bfrom\s+DE\b|\bIn\s+DE\b|\bDE-\d', pat_info) is not None

rows=[]
for r in pubs:
    if not is_germany(r.get('Patents_info')):
        continue
    gmon, gyear = parse_month_year(r.get('grant_date'))
    if gyear!=2019 or gmon is None or gmon<7 or gmon>12:
        continue
    fmon, fyear = parse_month_year(r.get('filing_date'))
    if fyear is None:
        continue
    # parse cpc list
    cpc_str = r.get('cpc')
    try:
        cpcs = json.loads(cpc_str) if isinstance(cpc_str,str) else []
    except Exception:
        cpcs=[]
    codes=[]
    for c in cpcs:
        code = c.get('code') if isinstance(c,dict) else None
        if not code:
            continue
        # CPC level4 group: take part before '/' plus first char after '/' (subclass group)
        if '/' in code:
            pre, post = code.split('/',1)
            lvl4 = pre + '/' + post[:1]
        else:
            lvl4 = code
        codes.append(lvl4)
    # unique per patent
    for lvl4 in sorted(set(codes)):
        rows.append({'lvl4':lvl4,'filing_year':int(fyear)})

df = pd.DataFrame(rows)
if df.empty:
    out = []
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

# yearly counts per lvl4
counts = df.groupby(['lvl4','filing_year']).size().reset_index(name='n')

alpha=0.1
# compute EMA per group over years sorted
ema_records=[]
for lvl4, g in counts.groupby('lvl4'):
    g2 = g.sort_values('filing_year')
    ema=None
    for _,row in g2.iterrows():
        x=row['n']
        ema = x if ema is None else (alpha*x + (1-alpha)*ema)
        ema_records.append({'lvl4':lvl4,'year':int(row['filing_year']),'ema':float(ema)})
ema_df = pd.DataFrame(ema_records)
# best year per lvl4
best = ema_df.sort_values(['lvl4','ema','year'], ascending=[True,False,False]).groupby('lvl4').head(1)
# pick global highest EMA across lvl4
max_ema = best['ema'].max()
top = best[best['ema']==max_ema].copy()
# if multiple ties, keep all
out = top[['lvl4','year','ema']].sort_values(['ema','lvl4'], ascending=[False,True]).to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wJ2DYma3EEOa0L0YfFXkDdOv': 'file_storage/call_wJ2DYma3EEOa0L0YfFXkDdOv.json', 'var_call_JzdjrwWti86NsnkHOjVecNUw': []}

exec(code, env_args)
