code = """import json, re
import pandas as pd
from datetime import datetime

def load_records(x):
    if isinstance(x, str):
        # path
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pub = load_records(var_call_Q0rdLo3jAf4dH9ydFv7V2W5h)
defs = load_records(var_call_YARdJjZIi2o7yQEOrkw3Ly66)

def extract_year(nl_date):
    if not nl_date:
        return None
    m = re.search(r'(19|20)\d{2}', nl_date)
    return int(m.group(0)) if m else None

def extract_ymd(nl_date):
    if not nl_date:
        return None
    # try parse with regex month name
    m = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', nl_date, re.I)
    y = extract_year(nl_date)
    if not m or not y:
        return None
    month = m.group(1).lower().capitalize()
    # day
    dm = re.search(r'(\d{1,2})(?:st|nd|rd|th)?', nl_date)
    if not dm:
        return None
    day = int(dm.group(1))
    try:
        return datetime.strptime(f"{day} {month} {y}", "%d %B %Y").date()
    except Exception:
        return None

def get_country(patents_info):
    if not patents_info:
        return None
    m = re.search(r'\bIn\s+([A-Z]{2})\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'\b([A-Z]{2})\s+patent\b', patents_info)
    if m:
        return m.group(1)
    # sometimes like "holds the US patent" etc.
    m = re.search(r'\bthe\s+([A-Z]{2})\s+patent\b', patents_info)
    if m:
        return m.group(1)
    return None

def parse_cpc_list(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for e in arr:
            code = e.get('code') if isinstance(e, dict) else None
            if code:
                codes.append(code)
        return codes
    except Exception:
        return []

def to_level4(code):
    if not code:
        return None
    code = code.strip()
    # Take first 3 chars like H01, then subgroup part up to 4 digits after '/'
    m = re.match(r'^([A-HY]\d{2}[A-Z])\s*(\d+)/(\d+)', code)
    if not m:
        return None
    main = m.group(1)
    grp = m.group(2)
    sub = m.group(3)
    sub4 = (sub + '0000')[:4]
    return f"{main}{grp}/{sub4}"

# filter Germany + grants in H2 2019
rows=[]
for r in pub:
    if get_country(r.get('Patents_info')) != 'DE':
        continue
    gd = extract_ymd(r.get('grant_date'))
    if not gd:
        continue
    if not (gd.year==2019 and gd.month>=7 and gd.month<=12):
        continue
    fy = extract_year(r.get('filing_date'))
    if not fy:
        continue
    codes = parse_cpc_list(r.get('cpc'))
    lvl4 = {to_level4(c) for c in codes}
    lvl4.discard(None)
    for c4 in lvl4:
        rows.append({'cpc4': c4, 'filing_year': fy})

df = pd.DataFrame(rows)
if df.empty:
    out=[]
else:
    counts = df.groupby(['cpc4','filing_year']).size().reset_index(name='filings')

    # compute EMA per cpc4 over years
    alpha=0.1
    best=[]
    for cpc4, g in counts.groupby('cpc4'):
        g2 = g.sort_values('filing_year')
        ema=None
        best_year=None
        best_ema=-1
        for _, row in g2.iterrows():
            x=row['filings']
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            if ema>best_ema:
                best_ema=ema
                best_year=int(row['filing_year'])
        best.append({'cpc_group_code': cpc4, 'best_year': best_year, 'best_ema_filings': float(best_ema)})
    best_df=pd.DataFrame(best)
    # definitions mapping
    defs_df=pd.DataFrame(defs)
    defs_df['symbol']=defs_df['symbol'].astype(str)
    merged=best_df.merge(defs_df[['symbol','titleFull']], left_on='cpc_group_code', right_on='symbol', how='left')
    merged=merged.drop(columns=['symbol'])
    merged=merged.sort_values(['best_ema_filings','cpc_group_code'], ascending=[False,True])
    out=merged.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_Q0rdLo3jAf4dH9ydFv7V2W5h': 'file_storage/call_Q0rdLo3jAf4dH9ydFv7V2W5h.json', 'var_call_YARdJjZIi2o7yQEOrkw3Ly66': 'file_storage/call_YARdJjZIi2o7yQEOrkw3Ly66.json'}

exec(code, env_args)
