code = """import json, re, pandas as pd
from datetime import datetime

path_pub = var_call_TKXxm4Z6bZmQ4doht4XWNzyv
with open(path_pub, 'r') as f:
    pubs = json.load(f)

path_cpcdef = var_call_6kz794bx9CreQsQFakdA3LjM
with open(path_cpcdef, 'r') as f:
    cpcdefs = json.load(f)

# filter Germany by country_code in Patents_info (' DE ' or ' from DE,' or '(DE-')
pat_de = re.compile(r"\bDE\b")

records = []
for r in pubs:
    info = r.get('Patents_info','') or ''
    if not pat_de.search(info):
        continue
    gd = r.get('grant_date','') or ''
    m = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)[^0-9]*([0-9]{1,2})[^0-9]*,?\s*([0-9]{4})", gd)
    if not m:
        m = re.search(r"on\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+([0-9]{1,2})(?:st|nd|rd|th)?,\s*([0-9]{4})", gd)
    if not m:
        m = re.search(r"([0-9]{1,2})(?:st|nd|rd|th)?\s+of\s+(January|February|March|April|May|June|July|August|September|October|November|December),\s*([0-9]{4})", gd)
    if not m:
        continue
    if 'of' in m.group(0) and m.group(1).isdigit():
        day = int(m.group(1)); mon = m.group(2); year = int(m.group(3))
    else:
        mon = m.group(1); day = int(m.group(2)); year = int(m.group(3))
    try:
        d = datetime.strptime(f"{day} {mon} {year}", "%d %B %Y")
    except:
        continue
    if not (d.year==2019 and d.month>=7 and d.month<=12):
        continue
    cpc_raw = r.get('cpc') or '[]'
    try:
        entries = json.loads(cpc_raw)
    except:
        continue
    for e in entries:
        code = e.get('code')
        if not code:
            continue
        sect = re.match(r"^[A-HY][0-9]{2}", code)
        if not sect:
            continue
        group4 = sect.group(0)
        records.append({'year': d.year, 'cpc4': group4})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['cpc4','year']).size().reset_index(name='filings')
    # need history over years for EMA; approximate from available years in data (per query it's 2019H2 only)
    # Without earlier years, EMA reduces to filings of that year for alpha=0.1
    alpha = 0.1
    ema_rows = []
    for cpc, grp in counts.groupby('cpc4'):
        grp = grp.sort_values('year')
        ema = None
        for _, row in grp.iterrows():
            y = row['year']; fcnt = row['filings']
            if ema is None:
                ema = fcnt
            else:
                ema = alpha*fcnt + (1-alpha)*ema
            ema_rows.append({'cpc4': cpc, 'year': int(y), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    best = ema_df.sort_values(['cpc4','ema','year'], ascending=[True,False,True]).groupby('cpc4').first().reset_index()
    # attach titles
    dfdefs = pd.DataFrame(cpcdefs)
    dfdefs['symbol'] = dfdefs['symbol'].astype(str)
    merged = best.merge(dfdefs[['symbol','titleFull']], left_on='cpc4', right_on='symbol', how='left')
    merged = merged.sort_values('ema', ascending=False)
    result = []
    for _, row in merged.iterrows():
        result.append({
            'CPC_group_level4': row['cpc4'],
            'titleFull': row.get('titleFull'),
            'best_year': int(row['year']),
            'EMA_filings': row['ema']
        })

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TKXxm4Z6bZmQ4doht4XWNzyv': 'file_storage/call_TKXxm4Z6bZmQ4doht4XWNzyv.json', 'var_call_6kz794bx9CreQsQFakdA3LjM': 'file_storage/call_6kz794bx9CreQsQFakdA3LjM.json'}

exec(code, env_args)
