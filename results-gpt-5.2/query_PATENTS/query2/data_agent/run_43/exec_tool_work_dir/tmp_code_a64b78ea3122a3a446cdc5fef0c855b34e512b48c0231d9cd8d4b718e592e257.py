code = """import json, re, pandas as pd
from datetime import datetime

path = var_call_BdolZc4KtarDsC5HVdgcXvbO
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def extract_country(patents_info):
    if not patents_info:
        return None
    m = re.search(r"\bfrom\s+([A-Z]{2})\b", patents_info)
    if m:
        return m.group(1)
    m = re.search(r"\bIn\s+([A-Z]{2}),", patents_info)
    if m:
        return m.group(1)
    return None

month_map = {m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

# parse natural-language-ish dates; return datetime.date

def parse_date(s):
    if not s:
        return None
    s = s.strip()
    # normalize separators
    s2 = s.replace(',', ' ')
    s2 = re.sub(r"\b(the|on|of)\b", " ", s2, flags=re.I)
    s2 = re.sub(r"(st|nd|rd|th)", "", s2)
    s2 = re.sub(r"\s+", " ", s2).strip()
    # try patterns
    # 1) dd Mon yyyy
    m = re.search(r"\b(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})\b", s2)
    if m:
        d=int(m.group(1)); mon=m.group(2).lower(); y=int(m.group(3))
        mon = mon[:3]
        mon_num = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}.get(mon)
        if mon_num:
            return datetime(y, mon_num, d).date()
    # 2) Mon dd yyyy
    m = re.search(r"\b([A-Za-z]+)\s+(\d{1,2})\s+(\d{4})\b", s2)
    if m:
        mon=m.group(1).lower(); d=int(m.group(2)); y=int(m.group(3))
        mon = mon[:3]
        mon_num = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}.get(mon)
        if mon_num:
            return datetime(y, mon_num, d).date()
    # 3) yyyy Mon dd
    m = re.search(r"\b(\d{4})\s+([A-Za-z]+)\s+(\d{1,2})\b", s2)
    if m:
        y=int(m.group(1)); mon=m.group(2).lower(); d=int(m.group(3))
        mon = mon[:3]
        mon_num = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}.get(mon)
        if mon_num:
            return datetime(y, mon_num, d).date()
    # 4) yyyy mm dd
    m = re.search(r"\b(\d{4})[-/\s](\d{1,2})[-/\s](\d{1,2})\b", s2)
    if m:
        y=int(m.group(1)); mon=int(m.group(2)); d=int(m.group(3))
        return datetime(y, mon, d).date()
    # 5) fallback: just year
    m = re.search(r"\b(\d{4})\b", s2)
    if m:
        return datetime(int(m.group(1)),1,1).date()
    return None

rows=[]
for r in recs:
    country=extract_country(r.get('Patents_info',''))
    if country!='DE':
        continue
    gd=parse_date(r.get('grant_date'))
    if not gd:
        continue
    if not (gd.year==2019 and gd.month>=7 and gd.month<=12):
        continue
    fd=parse_date(r.get('filing_date'))
    if not fd:
        continue
    filing_year=fd.year
    # parse cpc codes list
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
    # level 4 group: take part up to main group (e.g., G06F9/45)
    for code in set(codes):
        m=re.match(r"^([A-HY]\d{2}[A-Z])\s*(\d+)/(\d+)", code)
        if not m:
            continue
        sec=m.group(1)
        main=m.group(2)
        sub=m.group(3)
        level4 = f"{sec}{main}/{sub[:2]}"  # first two digits of subgroup
        rows.append({'level4':level4, 'filing_year':filing_year})

df=pd.DataFrame(rows)
if df.empty:
    out={'error':'No DE patents granted in H2 2019 after parsing.'}
    print('__RESULT__:')
    print(json.dumps(out))
else:
    counts=df.groupby(['level4','filing_year']).size().reset_index(name='n').sort_values(['level4','filing_year'])
    alpha=0.1
    # compute EMA per group over years present (sorted), starting at first year's count
    def ema_for_group(g):
        g=g.sort_values('filing_year').copy()
        ema=[]
        prev=None
        for n in g['n']:
            if prev is None:
                prev=float(n)
            else:
                prev = alpha*float(n) + (1-alpha)*prev
            ema.append(prev)
        g['ema']=ema
        return g
    ema_df = counts.groupby('level4', group_keys=False).apply(ema_for_group)
    # choose best year by max ema (ties -> earliest year)
    idx = ema_df.sort_values(['level4','ema','filing_year'], ascending=[True,False,True]).groupby('level4').head(1)
    # highest across groups? question: "technology areas ... with the highest EMA ... each year" ambiguous.
    # We'll return each CPC group with its best year and EMA, and rank by that max EMA desc.
    res = idx[['level4','filing_year','ema']].rename(columns={'filing_year':'best_year','ema':'best_year_ema'})
    res = res.sort_values('best_year_ema', ascending=False).reset_index(drop=True)
    print('__RESULT__:')
    print(res.to_json(orient='records'))"""

env_args = {'var_call_JYDlyS12q0EhC2MaYBxCCADu': ['publicationinfo'], 'var_call_FwxVyd3P5CUHhJzhuZSqr7PH': ['cpc_definition'], 'var_call_BdolZc4KtarDsC5HVdgcXvbO': 'file_storage/call_BdolZc4KtarDsC5HVdgcXvbO.json'}

exec(code, env_args)
