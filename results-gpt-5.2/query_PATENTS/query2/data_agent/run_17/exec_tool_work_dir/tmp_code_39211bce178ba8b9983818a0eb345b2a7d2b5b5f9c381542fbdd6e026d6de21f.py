code = """import json, re, pandas as pd
from datetime import datetime

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pub = load_records(var_call_AGeESMvXTTKrzlhVvMbGaR7r)
cpc_def = load_records(var_call_7zI21EtI5qOHZc12dZ5NSux4)

def parse_country(patents_info:str):
    if not patents_info:
        return None
    m = re.search(r'\bfrom\s+([A-Z]{2})\b', patents_info)
    return m.group(1) if m else None

month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}
mon_abbr = {m.lower():i for i,m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_date_any(s):
    if not s:
        return None
    t = s.strip()
    t = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', t, flags=re.I)
    t = t.replace(',', ' ')
    t = re.sub(r'\bon\b', ' ', t, flags=re.I)
    t = re.sub(r'\bthe\b', ' ', t, flags=re.I)
    t = re.sub(r'\s+', ' ', t).strip()
    # patterns
    # 2019 Jul 12
    m = re.search(r'\b(\d{4})\s+([A-Za-z]{3,9})\s+(\d{1,2})\b', t)
    if m:
        y=int(m.group(1)); mon=m.group(2).lower(); d=int(m.group(3))
        mo = month_map.get(mon) or mon_abbr.get(mon[:3])
        if mo:
            return datetime(y,mo,d).date()
    # Jul 12 2019
    m = re.search(r'\b([A-Za-z]{3,9})\s+(\d{1,2})\s+(\d{4})\b', t)
    if m:
        mon=m.group(1).lower(); d=int(m.group(2)); y=int(m.group(3))
        mo = month_map.get(mon) or mon_abbr.get(mon[:3])
        if mo:
            return datetime(y,mo,d).date()
    # 14 Mar 2019
    m = re.search(r'\b(\d{1,2})\s+([A-Za-z]{3,9})\s+(\d{4})\b', t)
    if m:
        d=int(m.group(1)); mon=m.group(2).lower(); y=int(m.group(3))
        mo = month_map.get(mon) or mon_abbr.get(mon[:3])
        if mo:
            return datetime(y,mo,d).date()
    # 2019 05 30
    m = re.search(r'\b(\d{4})\s+(\d{1,2})\s+(\d{1,2})\b', t)
    if m:
        y=int(m.group(1)); mo=int(m.group(2)); d=int(m.group(3))
        if 1<=mo<=12 and 1<=d<=31:
            return datetime(y,mo,d).date()
    return None

rows=[]
for r in pub:
    if parse_country(r.get('Patents_info'))!='DE':
        continue
    gd=parse_date_any(r.get('grant_date'))
    if not gd:
        continue
    if not (gd.year==2019 and gd.month>=7):
        continue
    fd=parse_date_any(r.get('filing_date'))
    if not fd:
        continue
    filing_year=fd.year
    # parse cpc list
    cpc_raw=r.get('cpc')
    codes=[]
    if cpc_raw:
        try:
            cpc_list=json.loads(cpc_raw)
            for e in cpc_list:
                code=e.get('code') if isinstance(e,dict) else None
                if code:
                    codes.append(code)
        except Exception:
            pass
    # level4 group from code: first 4 chars (letter+2 digits) e.g., G06F
    for code in set(codes):
        m=re.match(r'^([A-HY]\d\d[A-Z])', code)
        if m:
            grp=m.group(1)
            rows.append((grp, filing_year))

df=pd.DataFrame(rows, columns=['group4','year'])
if df.empty:
    out=[]
else:
    counts=df.groupby(['group4','year']).size().reset_index(name='filings')
    # compute EMA per group over years sorted
    alpha=0.1
    ema_rows=[]
    for grp, g in counts.groupby('group4'):
        g2=g.sort_values('year')
        ema=None
        for _,row in g2.iterrows():
            x=float(row['filings'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            ema_rows.append({'group4':grp,'year':int(row['year']),'ema':ema,'filings':int(row['filings'])})
    ema_df=pd.DataFrame(ema_rows)
    # best year per group: max ema, tie -> latest year
    best = ema_df.sort_values(['group4','ema','year'], ascending=[True,False,False]).groupby('group4').head(1)
    # pick global maximum EMA among groups
    max_ema=best['ema'].max()
    top=best[best['ema']==max_ema].copy()
    # join titles
    def_df=pd.DataFrame(cpc_def)
    def_df['level']=def_df['level'].astype(float)
    def_df=def_df[def_df['level']==4.0][['symbol','titleFull']]
    top=top.merge(def_df, left_on='group4', right_on='symbol', how='left')
    top=top.sort_values(['ema','group4'], ascending=[False,True])
    out=top[['titleFull','group4','year','ema']].rename(columns={'group4':'cpc_group_code','year':'best_year','titleFull':'full_title'}).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_AGeESMvXTTKrzlhVvMbGaR7r': 'file_storage/call_AGeESMvXTTKrzlhVvMbGaR7r.json', 'var_call_7zI21EtI5qOHZc12dZ5NSux4': 'file_storage/call_7zI21EtI5qOHZc12dZ5NSux4.json'}

exec(code, env_args)
