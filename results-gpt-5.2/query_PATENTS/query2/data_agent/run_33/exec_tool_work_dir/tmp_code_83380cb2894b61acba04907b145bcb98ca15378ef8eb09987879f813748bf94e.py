code = """import json, re
import pandas as pd

# load publication records (large)
path = var_call_K1WBvBcfBTbjF2tiKJoOeiiN
with open(path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

def parse_country(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'\bfrom\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\bIn\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    return None

month_map = {"jan":1,"january":1,"feb":2,"february":2,"mar":3,"march":3,"apr":4,"april":4,"may":5,"jun":6,"june":6,"jul":7,"july":7,"aug":8,"august":8,"sep":9,"sept":9,"september":9,"oct":10,"october":10,"nov":11,"november":11,"dec":12,"december":12}

def parse_year_month(date_str: str):
    if not date_str:
        return (None,None)
    s = date_str.strip().lower()
    y = None
    m = None
    ym = re.search(r'(19|20)\d{2}', s)
    if ym:
        y = int(ym.group(0))
    for k,v in month_map.items():
        if k in s:
            m = v
            break
    # also handle numeric like 2013, June 17th already ok; handle '2019, May 30th'
    return (y,m)

def cpc_to_level4(code: str):
    if not code:
        return None
    code = code.strip()
    if '/' not in code:
        return None
    pre, suf = code.split('/',1)
    # level4 group: first 4 digits after slash if available
    digits = re.sub(r'\D','',suf)
    if len(digits)==0:
        return None
    group = digits[:4] if len(digits)>=4 else digits
    return f"{pre}/{group}"

rows=[]
for r in pubs:
    country = parse_country(r.get('Patents_info'))
    if country!='DE':
        continue
    gy, gm = parse_year_month(r.get('grant_date'))
    if gy!=2019 or gm is None or gm<7:
        continue
    fy, fm = parse_year_month(r.get('filing_date'))
    if fy is None:
        continue
    # parse CPC json list
    cpc_raw = r.get('cpc')
    try:
        cpcs = json.loads(cpc_raw) if cpc_raw else []
    except Exception:
        cpcs=[]
    codes=set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        lvl4 = cpc_to_level4(code) if code else None
        if lvl4:
            codes.add(lvl4)
    for lvl4 in codes:
        rows.append({'cpc_lvl4': lvl4, 'filing_year': int(fy)})

df = pd.DataFrame(rows)
if df.empty:
    out = {"error":"No matching German patents granted in H2 2019 found."}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

# yearly counts per cpc_lvl4
cnt = df.groupby(['cpc_lvl4','filing_year']).size().reset_index(name='n').sort_values(['cpc_lvl4','filing_year'])

alpha=0.1
best=[]
for cpc, g in cnt.groupby('cpc_lvl4'):
    g = g.sort_values('filing_year')
    ema=None
    best_year=None
    best_ema=None
    for _, row in g.iterrows():
        n=row['n']
        ema = n if ema is None else alpha*n + (1-alpha)*ema
        if best_ema is None or ema>best_ema:
            best_ema=float(ema)
            best_year=int(row['filing_year'])
    best.append({'cpc_lvl4':cpc,'best_year':best_year,'best_ema':best_ema})

best_df=pd.DataFrame(best)
# highest per year? interpret as overall highest EMA; return top CPC areas
best_df=best_df.sort_values('best_ema', ascending=False)

# get titles: query result empty, so cannot map; return without titles if missing
# attempt to map titles from definition db result
cpc_defs = var_call_Hhixp9xgi1QHwvAgpgAdLWkx
map_title = {r['symbol']: r.get('titleFull') for r in cpc_defs} if isinstance(cpc_defs,list) else {}

best_df['titleFull']=best_df['cpc_lvl4'].map(map_title)

# keep those with titles if available else null
res = best_df.head(20).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res, ensure_ascii=False))"""

env_args = {'var_call_K1WBvBcfBTbjF2tiKJoOeiiN': 'file_storage/call_K1WBvBcfBTbjF2tiKJoOeiiN.json', 'var_call_Hhixp9xgi1QHwvAgpgAdLWkx': []}

exec(code, env_args)
